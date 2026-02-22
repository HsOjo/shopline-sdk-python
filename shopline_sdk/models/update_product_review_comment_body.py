"""Shopline API 数据模型 - UpdateProductReviewCommentBody"""

from typing import List, Optional

from pydantic import BaseModel


class UpdateProductReviewCommentBody(BaseModel):
    """Payload for updating product review comment"""
    user_name: Optional[str] = None
    """Name of the reviewer (only applicable on imported review) 評論作者的名稱（只適用於導入評論）"""
    status: Optional[str] = None
    score: Optional[int] = None
    comment: Optional[str] = None
    """The content of the review comment"""
    media_ids: Optional[List[str]] = None
    """Array of media ids 媒體id陣列"""
