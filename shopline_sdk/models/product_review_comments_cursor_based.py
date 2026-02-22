"""Shopline API 数据模型 - ProductReviewCommentsCursorBased"""

from typing import List, Optional

from pydantic import BaseModel

# 导入相关模型
from .product_review_comment import ProductReviewComment


class ProductReviewCommentsCursorBased(BaseModel):
    last_id: Optional[str] = None
    """Last ID of result. 最後一筆 ID"""
    limit: Optional[int] = None
    """Numbers of result"""
    items: Optional[List[ProductReviewComment]] = None
