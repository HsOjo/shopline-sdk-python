from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

async def call(
    session: aiohttp.ClientSession, id: str
) -> str:
    """
    Delete Webhook
    
    To delete a specific subscribed webhook by id
    以id刪除一個已訂閱的webhook
    
    Path: DELETE /webhooks/{id}
    """
    # 构建请求 URL
    url = f"webhooks/{id}"

    # 构建请求头
    headers = {"Content-Type": "application/json"}

    # 发起 HTTP 请求
    async with session.delete(
        url, headers=headers
    ) as response:
        if response.status >= 400:
            error_data = await response.json()
            raise ShoplineAPIError(
                status_code=response.status,
                **error_data
            )
        # 返回文本响应
        return await response.text()