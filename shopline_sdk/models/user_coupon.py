"""Shopline API 数据模型 - UserCoupon"""

from typing import Optional

from pydantic import BaseModel


class UserCoupon(BaseModel):
    id: Optional[str] = None
    """User Coupon ID"""
    user_id: Optional[str] = None
    """User ID 使用者 ID"""
