from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.not_found_error import NotFoundError
from ...models.server_error import ServerError
from ...models.theme_setting import ThemeSetting

async def call(
    session: aiohttp.ClientSession
) -> ThemeSetting:
    """
    Get Theme Setting
    
    To retrieve the setting of theme
    請求該主題有的設定
    
    Path: GET /settings/theme
    """
    # 构建请求 URL
    url = "settings/theme"

    # 构建请求头
    headers = {"Content-Type": "application/json"}

    # 发起 HTTP 请求
    async with session.get(
        url, headers=headers
    ) as response:
        if response.status >= 400:
            error_data = await response.json()
            if response.status == 404:
                error_model = NotFoundError(**error_data)
                raise ShoplineAPIError(
                    status_code=404,
                    error=error_model
                )
            if response.status == 500:
                error_model = ServerError(**error_data)
                raise ShoplineAPIError(
                    status_code=500,
                    error=error_model
                )
            # 默认错误处理
            raise ShoplineAPIError(
                status_code=response.status,
                **error_data
            )
        response_data = await response.json()

        # 验证并返回响应数据
        return ThemeSetting(**response_data)