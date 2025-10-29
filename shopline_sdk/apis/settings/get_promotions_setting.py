from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.promotions_setting import PromotionsSetting
from ...models.server_error import ServerError

async def call(
    session: aiohttp.ClientSession
) -> PromotionsSetting:
    """
    Get Promotions Setting
    
    To retrieve the setting of Promotions
    獲取優惠相關設定
    
    Path: GET /settings/promotions
    """
    # 构建请求 URL
    url = "settings/promotions"

    # 构建请求头
    headers = {"Content-Type": "application/json"}

    # 发起 HTTP 请求
    async with session.get(
        url, headers=headers
    ) as response:
        if response.status >= 400:
            error_data = await response.json()
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
        return PromotionsSetting(**response_data)