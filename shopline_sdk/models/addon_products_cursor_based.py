"""Shopline API 数据模型 - AddonProductsCursorBased"""

from typing import List, Optional

from pydantic import BaseModel

# 导入相关模型
from .addon_product import AddonProduct


class AddonProductsCursorBased(BaseModel):
    last_id: Optional[str] = None
    """Last ID of result. 最後一筆 ID"""
    limit: Optional[int] = None
    """Numbers of result"""
    items: Optional[List[AddonProduct]] = None
