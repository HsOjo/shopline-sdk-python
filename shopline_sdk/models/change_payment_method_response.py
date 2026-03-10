"""Shopline API 数据模型 - ChangePaymentMethodResponse"""

from typing import List, Optional

from pydantic import BaseModel

from .order import Order
from .transaction import Transaction


class ChangePaymentMethodResponse(BaseModel):
    order: Optional[Order] = None
    transactions: Optional[List[Transaction]] = None
