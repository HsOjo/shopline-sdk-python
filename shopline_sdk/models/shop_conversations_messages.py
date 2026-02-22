"""Shopline API 数据模型 - ShopConversationsMessages"""

from typing import List, Optional

from pydantic import BaseModel

# 导入相关模型
from .shop_conversations_message import ShopConversationsMessage


class ShopConversationsMessages(BaseModel):
    total: Optional[int] = None
    """Total Number 總筆數"""
    limit: Optional[int] = None
    """Numbers of Shop Messages 顯示筆數"""
    items: Optional[List[ShopConversationsMessage]] = None
