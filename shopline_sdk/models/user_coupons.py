"""Shopline API 数据模型 - UserCoupons"""

from typing import List, Optional

from pydantic import BaseModel

from .paginatable import Paginatable
from .user_coupon import UserCoupon


class UserCoupons(BaseModel):
    pagination: Optional[Paginatable] = None
    items: Optional[List[UserCoupon]] = None
