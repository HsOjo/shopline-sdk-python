from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.metafield_value import MetafieldValue

class Request(BaseModel):
    """查询参数模型"""
    filters: Optional[List[str]] = None
    """Search criteria
       In format of {namespace}.{key}:{value}
       {namespace} - required
       {key} - required
       {value} - optional"""

class Response(BaseModel):
    """响应体模型"""
    items: Optional[List[MetafieldValue]] = None

async def call(
    session: aiohttp.ClientSession, customer_id: str, request: Optional[Request] = None
) -> Response:
    """
    Get metafields attached to specific customer
    
    To get information of metafield attached to specific customer
    
    Path: GET /customers/{customer_id}/metafields
    """
    # 构建请求 URL
    url = f"customers/{customer_id}/metafields"

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
            raise ShoplineAPIError(
                status_code=response.status,
                **error_data
            )
        response_data = await response.json()

        # 验证并返回响应数据
        return Response(**response_data)