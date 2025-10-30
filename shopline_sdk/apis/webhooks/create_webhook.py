from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.create_webhook_body import CreateWebhookBody as Body
from ...models.webhook import Webhook

async def call(
    session: aiohttp.ClientSession, body: Optional[Body] = None
) -> Webhook:
    """
    Create Webhook
    
    To create a webhook
    創建一個webhook
    
    Path: POST /webhooks
    """
    # 构建请求 URL
    url = "webhooks"

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
        return Webhook(**response_data)