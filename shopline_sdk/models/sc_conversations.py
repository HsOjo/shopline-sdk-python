"""Shopline API 数据模型 - SCConversations"""

from typing import List, Optional

from pydantic import BaseModel

# 导入相关模型
from .paginatable import Paginatable
from .sc_conversation import SCConversation


class SCConversations(BaseModel):
    pagination: Optional[Paginatable] = None
    items: Optional[List[SCConversation]] = None
