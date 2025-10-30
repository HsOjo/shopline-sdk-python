from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.order_conversations_messages import OrderConversationsMessages
from ...models.server_error import ServerError
from ...models.shop_conversations_messages import ShopConversationsMessages

class Params(BaseModel):
    """查询参数模型"""
    platform: Union[Literal['shop_messages', 'order_messages', 'return_order_messages'], str]
    """Conversation from shop or order
      網店訊息或是訂單訊息
      return_order_messages 尚未開放"""
    limit: Optional[int] = None
    """Numbers of Messages of Conversations
      顯示 n 筆資料"""
    start: Optional[str] = None
    """Messages Start From
      訊息開始時間"""
    end: Optional[str] = None
    """Messages End Before
      訊息結束時間"""

async def call(
    session: aiohttp.ClientSession, conversationId: str, params: Optional[Params] = None
) -> ShopConversationsMessages:
    """
    Get Messages
    
    Get Conversations
    獲取對話訊息列表
    
    Path: GET /conversations/{conversationId}/messages
    """
    # 构建请求 URL
    url = f"conversations/{conversationId}/messages"

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
        return ShopConversationsMessages(**response_data)