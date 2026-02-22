"""Shopline API 数据模型 - CreateProductReviewCommentBody"""

from typing import List, Optional

from pydantic import BaseModel


class CreateProductReviewCommentBody(BaseModel):
    """Payload for creating product review comment"""
    product_id: Optional[str] = None
    """Product ID"""
    score: Optional[int] = None
    comment: Optional[str] = None
    """The content of the review comment"""
    user_id: Optional[str] = None
    """Customer ID (if any)"""
    order_id: Optional[str] = None
    """Order ID (if any)"""
    status: Optional[str] = None
    user_name: Optional[str] = None
    """Name of the reviewer (only applicable on imported review) 評論作者的名稱（只適用於導入評論）"""
    media_ids: Optional[List[str]] = None
    """Array of media ids 媒體id陣列"""
