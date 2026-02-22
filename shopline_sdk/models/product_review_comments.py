"""Shopline API 数据模型 - ProductReviewComments"""

from typing import List, Optional

from pydantic import BaseModel

# 导入相关模型
from .paginatable import Paginatable
from .product_review_comment import ProductReviewComment


class ProductReviewComments(BaseModel):
    items: Optional[List[ProductReviewComment]] = None
    pagination: Optional[Paginatable] = None
