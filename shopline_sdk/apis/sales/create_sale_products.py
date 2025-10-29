from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.sale_product import SaleProduct
from ...models.server_error import ServerError
from ...models.unprocessable_entity_error import UnprocessableEntityError


class ProductsItem(BaseModel):
    """Item model for products"""
    product_id: str
    custom_numbers: Optional[List[str]] = None
    custom_keys: Optional[List[str]] = None
    variations: Optional[List[Dict[str, Any]]] = None

class Request(BaseModel):
    """请求体模型"""
    products: List[ProductsItem]

class Response(BaseModel):
    """响应体模型"""
    items: Optional[List[SaleProduct]] = None

async def call(
    session: aiohttp.ClientSession, saleId: str, request: Optional[Request] = None
) -> Response:
    """
    Create sale products
    
    To create sale products
    新增直播商品
    
    Path: POST /sales/{saleId}/products
    """
    # 构建请求 URL
    url = f"sales/{saleId}/products"

    # 构建请求头
    headers = {"Content-Type": "application/json"}

    # 构建请求体
    json_data = request.model_dump(exclude_none=True) if request else None

    # 发起 HTTP 请求
    async with session.post(
        url, json=json_data, headers=headers
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