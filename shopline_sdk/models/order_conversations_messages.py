"""Shopline API 数据模型 - OrderConversationsMessages"""

from typing import List, Optional

from pydantic import BaseModel

from .order_conversations_message import OrderConversationsMessage


class OrderConversationsMessages(BaseModel):
    total: Optional[int] = None
    """Total Number 總筆數"""
    limit: Optional[int] = None
    """Numbers of Order Messages 顯示筆數"""
    items: Optional[List[OrderConversationsMessage]] = None
