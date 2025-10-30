from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.page_sections import PageSections
from ...models.server_error import ServerError
from ...models.unauthorized_error import UnauthorizedError

class Params(BaseModel):
    """查询参数模型"""
    types: List[Literal['announcement', 'header', 'footer']]
    """Types of layouts sections
      佈局元件的種類"""

class Response(BaseModel):
    """响应体模型"""
    items: Optional[PageSections] = None

async def call(
    session: aiohttp.ClientSession, theme_key: str, params: Optional[Params] = None
) -> Response:
    """
    Get Layouts Sections
    
    To get the layouts sections with theme key
    用theme_key請求佈局元件
    
    Path: GET /themes/{theme_key}/layouts/sections
    """
    # 构建请求 URL
    url = f"themes/{theme_key}/layouts/sections"

    # 构建查询参数
    query_params = {}
    if params:
        params_dict = params.model_dump(exclude_none=True)
        for key, value in params_dict.items():
            if value is not None:
                query_params[key] = value

    # 构建请求头
    headers = {"Content-Type": "application/json"}

    # 发起 HTTP 请求
    async with session.get(
        url, params=query_params, headers=headers
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