"""Shopline API 数据模型 - DiscountOptions"""

from typing import List, Optional

from pydantic import BaseModel

from .discount_option import DiscountOption


class DataConfig(BaseModel):
    """Configuration model for data"""
    offset: Optional[int] = None
    limit: Optional[int] = None
    total: Optional[int] = None
    items: Optional[List[List[DiscountOption]]] = None


class DiscountOptions(BaseModel):
    data: Optional[DataConfig] = None
