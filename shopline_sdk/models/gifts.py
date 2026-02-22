"""Shopline API 数据模型 - Gifts"""

from typing import List, Optional

from pydantic import BaseModel

# 导入相关模型
from .gift import Gift
from .paginatable import Paginatable


class Gifts(BaseModel):
    pagination: Optional[Paginatable] = None
    items: Optional[List[Gift]] = None
