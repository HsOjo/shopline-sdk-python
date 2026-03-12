"""Shopline API 数据模型 - ThemeSchema"""

from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel

from .translatable import Translatable


class ItemsConfig(BaseModel):
    """Configuration model for items"""
    name: Optional[Translatable] = None
    settings: Optional[Dict[str, Any]] = None
    """Settings of the item of theme schema"""


class ThemeSchema(BaseModel):
    items: Optional[Union[ItemsConfig, List[ItemsConfig]]] = None
