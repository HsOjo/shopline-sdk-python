from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.update_webhook_body import UpdateWebhookBody as Body
from ...models.webhook import Webhook

async def call(
    session: aiohttp.ClientSession, id: str, body: Optional[Body] = None
) -> Webhook:
    """
    Update Webhook
    
    To update a specific subscribed webhook by id
    以id更新一個已訂閱的webhook
    
    Path: PUT /webhooks/{id}
    """
    # 构建请求 URL
    url = f"webhooks/{id}"

    # 构建请求头
    headers = {"Content-Type": "application/json"}

    # 构建请求体
    json_data = body.model_dump(exclude_none=True) if body else None

    # 发起 HTTP 请求
    async with session.put(
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