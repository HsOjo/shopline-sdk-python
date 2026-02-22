"""Shopline API 数据模型 - CustomerGroups"""

from typing import List, Optional

from pydantic import BaseModel

# 导入相关模型
from .customer_group import CustomerGroup
from .paginatable import Paginatable


class CustomerGroups(BaseModel):
    pagination: Optional[Paginatable] = None
    items: Optional[List[CustomerGroup]] = None
