from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.bad_request_error import BadRequestError
from ...models.media_upload_error import MediaUploadError
from ...models.not_found_error import NotFoundError
from ...models.product import Product
from ...models.server_error import ServerError
from ...models.unprocessable_entity_error import UnprocessableEntityError

class Body(BaseModel):
    """请求体模型"""
    urls: Optional[List[str]] = None
    """Urls of the Images
      新增圖片之url"""
    image_type: Optional[Union[Literal['main', 'detail'], str]] = None
    """Image Type
      圖片種類"""
    is_replcae: Optional[bool] = None
    """Whether replacing the original images
      是否取代原本數量"""

async def call(
    session: aiohttp.ClientSession, id: str, body: Optional[Body] = None
) -> Product:
    """
    Add Product Images
    
    Add or replace product images to an existing product.
    透過open API對現有商品進行新增或覆蓋圖片。
    
    Path: POST /products/{id}/add_images
    """
    # 构建请求 URL
    url = f"products/{id}/add_images"

    # 构建请求头
    headers = {"Content-Type": "application/json"}

    # 构建请求体
    json_data = body.model_dump(exclude_none=True) if body else None

    # 发起 HTTP 请求
    async with session.post(
        url, json=json_data, headers=headers
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
        return Product(**response_data)