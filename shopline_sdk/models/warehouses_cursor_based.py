"""Shopline API 数据模型 - WarehousesCursorBased"""

from typing import Any, Dict, List, Optional

from pydantic import BaseModel

# 导入相关模型
from .product import Product


class WarehousesCursorBased(BaseModel):
    last_id: Optional[str] = None
    """Last ID of result. 最後一筆 ID"""
    limit: Optional[int] = None
    """Numbers of result"""
    items: Optional[List[Product]] = None
    removed_item_ids: Optional[List[Any]] = None
    price_sets: Optional[Dict[str, Any]] = None
