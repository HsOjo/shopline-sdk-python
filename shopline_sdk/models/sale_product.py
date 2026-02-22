"""Shopline API 数据模型 - SaleProduct"""

from typing import List, Optional

from pydantic import BaseModel


class VariationsItem(BaseModel):
    """Item model for variations"""
    variation_id: Optional[str] = None
    custom_keys: Optional[List[str]] = None


class SaleProduct(BaseModel):
    product_id: Optional[str] = None
    custom_numbers: Optional[List[str]] = None
    custom_keys: Optional[List[str]] = None
    effective_key: Optional[bool] = None
    create_time: Optional[str] = None
    update_time: Optional[str] = None
    variations: Optional[List[VariationsItem]] = None
