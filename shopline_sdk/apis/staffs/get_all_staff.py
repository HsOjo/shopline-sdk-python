from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.channel import Channel
from ...models.merchant import Merchant
from ...models.staff import Staff

class Request(BaseModel):
    """查询参数模型"""
    permission_scopes: Optional[List[Literal['open_api', 'admin', 'shop_crm', 'pos', 'one', 'shoplytics', 'sc', 'dash', 'ads', 'payment_center', 'mc', 'form_builder']]] = None
    """The permissions scopes
       獲取權限的範圍(可以多個)。"""

class Response(BaseModel):
    """响应体模型"""
    items: Optional[List[Dict[str, Any]]] = None

async def call(
    session: aiohttp.ClientSession, request: Optional[Request] = None
) -> Response:
    """
    Get all staff
    
    To retrieve all staff
    獲取所有管理員。
    
    Path: GET /staffs
    """
    # 构建请求 URL
    url = "staffs"

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