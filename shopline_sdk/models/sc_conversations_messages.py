"""Shopline API 数据模型 - SCConversationsMessages"""

from typing import List, Optional

from pydantic import BaseModel

from .sc_conversations_message import SCConversationsMessage


class SCConversationsMessages(BaseModel):
    total: Optional[int] = None
    """Total Number 總筆數"""
    limit: Optional[int] = None
    """Numbers of Shop Messages 顯示筆數"""
    items: Optional[List[SCConversationsMessage]] = None
