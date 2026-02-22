"""Shopline API 数据模型 - ShopConversations"""

from typing import List, Optional

from pydantic import BaseModel

# 导入相关模型
from .paginatable import Paginatable
from .shop_conversation import ShopConversation


class ShopConversations(BaseModel):
    pagination: Optional[Paginatable] = None
    items: Optional[List[ShopConversation]] = None
