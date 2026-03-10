"""Shopline API 数据模型 - CustomField"""

from typing import Optional

from pydantic import BaseModel

from .translatable import Translatable


class CustomField(BaseModel):
    type: Optional[str] = None
    """Column Type for the Custom Field 欄位類別"""
    name_translations: Optional[Translatable] = None
    field_id: Optional[str] = None
    """Field ID 欄位ID"""
    value: Optional[str] = None
    """Field Value 欄位值"""
