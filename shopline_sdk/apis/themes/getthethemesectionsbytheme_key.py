from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.server_error import ServerError
from ...models.theme_schema import ThemeSchema
from ...models.unauthorized_error import UnauthorizedError

class Request(BaseModel):
    """查询参数模型"""
    template_key: Optional[str] = None
    """Template Key"""

class Response(BaseModel):
    """响应体模型"""
    items: Optional[ThemeSchema] = None

async def call(
    session: aiohttp.ClientSession, theme_key: str, request: Optional[Request] = None
) -> Response:
    """
    Get the theme sections by theme_key
    
    To get the page sections of the theme with the theme_key
    用theme_key請求該主題有的頁面sections
    
    Path: GET /themes/{theme_key}/sections
    """
    # 构建请求 URL
    url = f"themes/{theme_key}/sections"

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
            if response.status == 401:
                error_model = UnauthorizedError(**error_data)
                raise ShoplineAPIError(
                    status_code=401,
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