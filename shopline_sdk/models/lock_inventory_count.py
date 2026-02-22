"""Shopline API 数据模型 - LockInventoryCount"""

from typing import Any, Dict, Optional

from pydantic import BaseModel


class LockInventoryCount(BaseModel):
    product_id: Optional[str] = None
    """Product ID. 商品 ID"""
    locked_inventory_count: Optional[int] = None
    """Locked inventory count 已鎖定庫存數量"""
    variations: Optional[Dict[str, Any]] = None
    """Variations 多規格商品"""
