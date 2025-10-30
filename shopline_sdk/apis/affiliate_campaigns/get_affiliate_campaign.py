from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.affiliate_campaign import AffiliateCampaign
from ...models.server_error import ServerError
from ...models.unprocessable_entity_error import UnprocessableEntityError

async def call(
    session: aiohttp.ClientSession, id: str
) -> AffiliateCampaign:
    """
    Get Affiliate Campaign
    
    To get affiliate campaign.
    獲取推薦活動。
    
    Path: GET /affiliate_campaigns/{id}
    """
    # 构建请求 URL
    url = f"affiliate_campaigns/{id}"

    # 构建请求头
    headers = {"Content-Type": "application/json"}

    # 发起 HTTP 请求
    async with session.get(
        url, headers=headers
    ) as response:
        if response.status >= 400:
            error_data = await response.json()
            if response.status == 422:
                error_model = UnprocessableEntityError(**error_data)
                raise ShoplineAPIError(
                    status_code=422,
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
        return AffiliateCampaign(**response_data)