"""Shopline API 数据模型 - OrderConversations"""

from typing import List, Optional

from pydantic import BaseModel

# 导入相关模型
from .order_conversation import OrderConversation
from .paginatable import Paginatable


class OrderConversations(BaseModel):
    pagination: Optional[Paginatable] = None
    items: Optional[List[OrderConversation]] = None
