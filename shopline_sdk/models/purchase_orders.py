"""Shopline API 数据模型 - PurchaseOrders"""

from typing import List, Optional

from pydantic import BaseModel

# 导入相关模型
from .paginatable import Paginatable
from .purchase_order import PurchaseOrder


class PurchaseOrders(BaseModel):
    pagination: Optional[Paginatable] = None
    items: Optional[List[PurchaseOrder]] = None
