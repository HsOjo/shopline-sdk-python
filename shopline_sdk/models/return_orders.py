"""Shopline API 数据模型 - ReturnOrders"""

from typing import List, Optional

from pydantic import BaseModel

from .paginatable import Paginatable
from .return_order import ReturnOrder


class ReturnOrders(BaseModel):
    items: Optional[List[ReturnOrder]] = None
    pagination: Optional[Paginatable] = None
