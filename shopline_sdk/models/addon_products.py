"""Shopline API 数据模型 - AddonProducts"""

from typing import List, Optional

from pydantic import BaseModel

from .addon_product import AddonProduct
from .paginatable import Paginatable


class AddonProducts(BaseModel):
    pagination: Optional[Paginatable] = None
    items: Optional[List[AddonProduct]] = None
