from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.bad_request_error import BadRequestError
from ...models.gift import Gift
from ...models.not_found_error import NotFoundError
from ...models.product import Product
from ...models.server_error import ServerError
from ...models.unprocessable_entity_error import UnprocessableEntityError

class Request(BaseModel):
    """请求体模型"""
    sku: Optional[str] = None
    """Product or Product Variation sku
      商品或商品規格的商品貨號"""
    quantity: Optional[int] = None
    """This value should be between -9999999 and 9999999.
       數值必須在 -9999999 和 9999999 之間。"""
    replace: Optional[bool] = None
    """Whether replacing the original quantity
      是否取代原本數量
       - 
       true: replace the product's quantity with the number you provided
      取代原本數量
      
       false: increase/decrease the quantity with the number you provided
      增加/減少數量" """

class Response(BaseModel):
    """响应体模型"""
    id: Optional[str] = None
    sku: Optional[str] = None
    quantity: Optional[float] = None
    updated_at: Optional[str] = None
    product_id: Optional[str] = None
    items: Optional[List[Dict[str, Any]]] = None
    errors: Optional[List[Dict[str, Any]]] = None

async def call(
    session: aiohttp.ClientSession, request: Optional[Request] = None
) -> Response:
    """
    Update Quantity by SKU
    
    Update all products or product variations quantity by input SKU
    更新所有相同商品貨號的商品或商品規格庫存數量
    
    Path: PUT /products/update_quantity
    """
    # 构建请求 URL
    url = "products/update_quantity"

    # 构建请求头
    headers = {"Content-Type": "application/json"}

    # 构建请求体
    json_data = request.model_dump(exclude_none=True) if request else None

    # 发起 HTTP 请求
    async with session.put(
        url, json=json_data, headers=headers
    ) as response:
        if response.status >= 400:
            error_data = await response.json()
            if response.status == 400:
                error_model = BadRequestError(**error_data)
                raise ShoplineAPIError(
                    status_code=400,
                    error=error_model,
                    **error_data
                )
            if response.status == 403:
                error_model = BadRequestError(**error_data)
                raise ShoplineAPIError(
                    status_code=403,
                    error=error_model,
                    **error_data
                )
            if response.status == 404:
                error_model = NotFoundError(**error_data)
                raise ShoplineAPIError(
                    status_code=404,
                    error=error_model,
                    **error_data
                )
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