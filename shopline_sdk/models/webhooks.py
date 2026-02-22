"""Shopline API 数据模型 - Webhooks"""

from typing import List, Optional

from pydantic import BaseModel

# 导入相关模型
from .paginatable import Paginatable
from .webhook import Webhook


class Webhooks(BaseModel):
    items: Optional[List[Webhook]] = None
    pagination: Optional[Paginatable] = None
