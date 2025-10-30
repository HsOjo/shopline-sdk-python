from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.server_error import ServerError
from ...models.unprocessable_entity_error import UnprocessableEntityError
from ...models.wish_list_items import WishListItems

class Params(BaseModel):
    """查询参数模型"""
    customer_id: str
    """The ID of the customer.
      顧客 ID"""
    previous_id: Optional[str] = None
    """The last ID of the wish list item in the previous request.
       上一次請求的最後一筆 wish list item 的 ID"""
    limit: Optional[int] = None
    """Numbers of result
      顯示 n 筆結果"""
    simplified: Optional[bool] = None
    """Is response simplified
      是否簡化回傳結果"""
    product_ids: Optional[List[str]] = None
    """Product IDs
      指定商品ID"""
    order_by: Optional[Literal['desc', 'asc']] = None
    """Specify the sorting order based on the created_at field as either asc or desc.
       依照 created_at 欄位指定排序方式為升冪或降冪"""

async def call(
    session: aiohttp.ClientSession, params: Optional[Params] = None
) -> WishListItems:
    """
    Get wish list items
    
    To get wish list items.
    獲取追蹤清單。
    
    Path: GET /wish_list_items
    """
    # 构建请求 URL
    url = "wish_list_items"

    # 构建查询参数
    query_params = {}
    if params:
        params_dict = params.model_dump(exclude_none=True)
        for key, value in params_dict.items():
            if value is not None:
                query_params[key] = value

    # 构建请求头
    headers = {"Content-Type": "application/json"}

    # 发起 HTTP 请求
    async with session.get(
        url, params=query_params, headers=headers
    ) as response:
        if response.status >= 400:
            error_data = await response.json()
            if response.status == 422:
                error_model = UnprocessableEntityError(**error_data)
                raise ShoplineAPIError(
                    status_code=422,
                    error=error_model,
                    **error_data
                )
            if response.status == 500:
                error_model = ServerError(**error_data)
                raise ShoplineAPIError(
                    status_code=500,
                    error=error_model,
                    **error_data
                )
            # 默认错误处理
            raise ShoplineAPIError(
                status_code=response.status,
                **error_data
            )
        response_data = await response.json()

        # 验证并返回响应数据
        return WishListItems(**response_data)