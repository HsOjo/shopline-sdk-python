from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.metafield_value import MetafieldValue

class Body(BaseModel):
    """请求体模型"""
    items: Optional[List[Any]] = None

class Response(BaseModel):
    """响应体模型"""
    items: Optional[List[MetafieldValue]] = None

async def call(
    session: aiohttp.ClientSession, body: Optional[Body] = None
) -> Response:
    """
    Bulk create metafield
    
    To create metafield attached to current merchant
    
    Path: POST /merchants/current/metafields/bulk
    """
    # 构建请求 URL
    url = "merchants/current/metafields/bulk"

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
            raise ShoplineAPIError(
                status_code=response.status,
                **error_data
            )
        response_data = await response.json()

        # 验证并返回响应数据
        return Response(**response_data)