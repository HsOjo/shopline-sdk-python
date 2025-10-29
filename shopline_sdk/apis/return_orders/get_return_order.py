from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.return_order import ReturnOrder

async def call(
    session: aiohttp.ClientSession, id: str
) -> ReturnOrder:
    """
    Get return order
    
    To retrieve a specific return order by id
    以id獲取一個退貨單
    
    Path: GET /return_orders/{id}
    """
    # 构建请求 URL
    url = f"return_orders/{id}"

    # 构建请求头
    headers = {"Content-Type": "application/json"}

    # 发起 HTTP 请求
    async with session.get(
        url, headers=headers
    ) as response:
        if response.status >= 400:
            error_data = await response.json()
            raise ShoplineAPIError(
                status_code=response.status,
                **error_data
            )
        response_data = await response.json()

        # 验证并返回响应数据
        return ReturnOrder(**response_data)