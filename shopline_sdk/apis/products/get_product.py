from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.not_found_error import NotFoundError
from ...models.product import Product
from ...models.server_error import ServerError

class Request(BaseModel):
    """查询参数模型"""
    fields: Optional[List[str]] = None
    """Could only show certain parameters in the response
      結果只顯示哪些參數"""
    excludes: Optional[List[str]] = None
    """Could exclude certain parameters in the response
      結果要排除哪些參數"""
    include_fields: Optional[List[Literal['labels']]] = None
    """Provide additional attributes in the response
      結果添加哪些參數"""

async def call(
    session: aiohttp.ClientSession, id: str, request: Optional[Request] = None
) -> Product:
    """
    Get Product
    
    To get detailed information for a specific product with its ID
    使用商品ID獲取特定一個商品的詳細資料
    
    Path: GET /products/{id}
    """
    # 构建请求 URL
    url = f"products/{id}"

    # 构建查询参数
    params = {}
    if request:
        request_dict = request.model_dump(exclude_none=True)
        for key, value in request_dict.items():
            if value is not None:
                params[key] = value

    # 构建请求头
    headers = {"Content-Type": "application/json"}

    # 发起 HTTP 请求
    async with session.get(
        url, params=params, headers=headers
    ) as response:
        if response.status >= 400:
            error_data = await response.json()
            if response.status == 404:
                error_model = NotFoundError(**error_data)
                raise ShoplineAPIError(
                    status_code=404,
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
        return Product(**response_data)