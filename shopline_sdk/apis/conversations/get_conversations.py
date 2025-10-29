from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.order_conversations import OrderConversations
from ...models.server_error import ServerError
from ...models.shop_conversations import ShopConversations

class Request(BaseModel):
    """查询参数模型"""
    platform: Literal['shop_messages', 'order_messages', 'return_order_messages']
    """Conversation from shop or order
      網店訊息或是訂單訊息
      return_order_messages 尚未開放"""
    customer_id: Optional[str] = None
    """Customer ID
      客戶ID"""
    page: Optional[int] = None
    """Page Number
      頁數"""
    per_page: Optional[int] = None
    """Numbers of Conversation per Page
      每頁顯示 n 筆資料"""

async def call(
    session: aiohttp.ClientSession, request: Optional[Request] = None
) -> ShopConversations:
    """
    Get Conversations
    
    Get Conversations
    獲取對話列表
    
    Path: GET /conversations
    """
    # 构建请求 URL
    url = "conversations"

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
        return ShopConversations(**response_data)