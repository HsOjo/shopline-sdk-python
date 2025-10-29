from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.metafield_definition import MetafieldDefinition

class Response(BaseModel):
    """响应体模型"""
    items: Optional[List[MetafieldDefinition]] = None

async def call(
    session: aiohttp.ClientSession
) -> Response:
    """
    Get an array of metafield definitions
    
    To get information fo metafield definition attached to cart items
    
    Path: GET /metafield_definitions/cart_items
    """
    # 构建请求 URL
    url = "metafield_definitions/cart_items"

    # 构建请求头
    headers = {"Content-Type": "application/json"}

    # 发起 HTTP 请求
    async with session.get(
        url, headers=headers
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