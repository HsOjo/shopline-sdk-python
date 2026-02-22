"""Shopline API 数据模型 - DiscountAmount"""

from typing import Optional

from pydantic import BaseModel


class DiscountAmount(BaseModel):
    cents: Optional[int] = None
    currency_symbol: Optional[str] = None
    currency_iso: Optional[str] = None
    label: Optional[str] = None
    dollars: Optional[float] = None
