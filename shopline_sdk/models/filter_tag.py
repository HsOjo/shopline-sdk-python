"""Shopline API 数据模型 - FilterTag"""

from typing import Optional

from pydantic import BaseModel

from .translatable import Translatable


class FilterTag(BaseModel):
    id: Optional[str] = None
    """Filter Tag's ID 自訂篩選條件 ID"""
    name_translations: Optional[Translatable] = None
