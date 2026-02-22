"""Shopline API 数据模型 - UpdateLockInventoryBody"""

from typing import Optional

from pydantic import BaseModel


class Meta_DataConfig(BaseModel):
    """Configuration model for meta_data"""
    start_time: Optional[str] = None


class UpdateLockInventoryBody(BaseModel):
    """Payload for updating product lock inventory"""
    virtual_cart_id: str
    variation_key: Optional[str] = None
    original_quantity: float
    changed_quantity: float
    expired_time: str
    meta_data: Optional[Meta_DataConfig] = None
    lock_inventory_id: Optional[str] = None
