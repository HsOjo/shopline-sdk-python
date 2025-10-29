from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.metafield_value import MetafieldValue


class ItemsItem(BaseModel):
    """Item model for items"""
    id: Optional[str] = None
    resource_id: Optional[str] = None
    key: Optional[str] = None
    field_type: Optional[Literal['single_line_text_field', 'multi_line_text_field', 'number_integer', 'number_decimal', 'json', 'boolean', 'url']] = None
    field_value: Optional[Union[str, float, bool, Dict[str, Any]]] = None

class Request(BaseModel):
    """请求体模型"""
    items: Optional[List[ItemsItem]] = None

class Response(BaseModel):
    """响应体模型"""
    result: Optional[str] = None

async def call(
    session: aiohttp.ClientSession, cart_id: str, request: Optional[Request] = None
) -> Response:
    """
    bulk delete app metafield
    
    bulk delete information of app metafield attached to cart items of specific cart
    
    Path: DELETE /carts/{cart_id}/items/app_metafields/bulk
    """
    # 构建请求 URL
    url = f"carts/{cart_id}/items/app_metafields/bulk"

    # 构建请求头
    headers = {"Content-Type": "application/json"}

    # 构建请求体
    json_data = request.model_dump(exclude_none=True) if request else None

    # 发起 HTTP 请求
    async with session.delete(
        url, json=json_data, headers=headers
    ) as response:
        if response.status >= 400:
            error_data = await response.json()
            raise ShoplineAPIError(
                status_code=response.status,
                **error_data
            )
        response_data = await response.json()

        # 验证并返回响应数据
        return Response(**response_data)