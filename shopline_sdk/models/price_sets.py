"""Shopline API 数据模型 - PriceSets"""

from typing import List, Optional

from pydantic import BaseModel

# 导入相关模型
from .price_set import PriceSet


class PriceSets(BaseModel):
    items: Optional[List[PriceSet]] = None
