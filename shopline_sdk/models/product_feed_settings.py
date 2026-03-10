"""Shopline API 数据模型 - ProductFeedSettings"""

from typing import List, Optional

from pydantic import BaseModel

from .paginatable import Paginatable
from .product_feed_setting import ProductFeedSetting


class ProductFeedSettings(BaseModel):
    items: Optional[List[ProductFeedSetting]] = None
    pagination: Optional[Paginatable] = None
