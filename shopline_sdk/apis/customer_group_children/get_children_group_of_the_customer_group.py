from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.customer_group import CustomerGroup
from ...models.paginatable import Paginatable
from ...models.server_error import ServerError
from ...models.unprocessable_entity_error import UnprocessableEntityError

class Params(BaseModel):
    """查询参数模型"""
    page: Optional[int] = None
    """Page
      頁數
      (Default: 1)"""
    per_page: Optional[int] = None
    """Numbers of Child Customer Groups per page
      每頁顯示 n 筆資料
      (Default: 24, Max: 999)"""
    sort_by: Optional[str] = None
    """Setting sort by created time
      設定依照建立時間排序
      (Default: desc)"""

class Response(BaseModel):
    """响应体模型"""
    parent: Optional[CustomerGroup] = None
    children: Optional[List[CustomerGroup]] = None
    pagination: Optional[Paginatable] = None

async def call(
    session: aiohttp.ClientSession, parentCustomerGroupId: str, params: Optional[Params] = None
) -> Response:
    """
    Get Children Group of the Customer Group
    
    To get child customer groups of the customer group.
    取得母分群的子分群。
    
    Path: GET /customer_groups/{parentCustomerGroupId}/customer_group_children
    """
    # 构建请求 URL
    url = f"customer_groups/{parentCustomerGroupId}/customer_group_children"

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
        return Response(**response_data)