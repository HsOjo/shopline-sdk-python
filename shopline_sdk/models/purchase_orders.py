"""Shopline API 数据模型 - PurchaseOrders"""

from typing import List, Optional

from pydantic import BaseModel

from .paginatable import Paginatable
from .purchase_order import PurchaseOrder


class PurchaseOrders(BaseModel):
    pagination: Optional[Paginatable] = None
    items: Optional[List[PurchaseOrder]] = None
