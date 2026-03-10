"""Shopline API 数据模型 - Categories"""

from typing import List, Optional

from pydantic import BaseModel

from .category import Category
from .paginatable import Paginatable


class Categories(BaseModel):
    pagination: Optional[Paginatable] = None
    items: Optional[List[Category]] = None
