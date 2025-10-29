from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.bad_request_error import BadRequestError
from ...models.not_found_error import NotFoundError
from ...models.server_error import ServerError

class Response(BaseModel):
    """响应体模型"""
    message: Optional[str] = None

async def call(
    session: aiohttp.ClientSession, product_id: str, id: str
) -> Response:
    """
    Delete Product Variation
    
    To delete a product variation with open API
    透過Open API刪除規格商品
    
    Path: DELETE /products/{product_id}/variations/{id}
    """
    # 构建请求 URL
    url = f"products/{product_id}/variations/{id}"

    # 构建请求头
    headers = {"Content-Type": "application/json"}

    # 发起 HTTP 请求
    async with session.delete(
        url, headers=headers
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
        return Response(**response_data)