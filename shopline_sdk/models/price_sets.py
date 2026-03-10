"""Shopline API 数据模型 - PriceSets"""

from typing import List, Optional

from pydantic import BaseModel

from .price_set import PriceSet


class PriceSets(BaseModel):
    items: Optional[List[PriceSet]] = None
