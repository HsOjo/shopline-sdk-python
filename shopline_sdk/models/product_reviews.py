"""Shopline API 数据模型 - ProductReviews"""

from typing import List, Optional

from pydantic import BaseModel

from .paginatable import Paginatable
from .product_review import ProductReview


class ProductReviews(BaseModel):
    items: Optional[List[ProductReview]] = None
    pagination: Optional[Paginatable] = None
