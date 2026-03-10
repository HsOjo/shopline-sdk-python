"""Shopline API 数据模型 - ReturnOrderPromotionItem"""

from typing import Optional

from pydantic import BaseModel

from .money import Money


class ReturnOrderPromotionItem(BaseModel):
    id: Optional[str] = None
    """Return Order Promotion Item ID"""
    order_promotion_item_id: Optional[str] = None
    """Order Promotion Item ID"""
    return_order_id: Optional[str] = None
    """Return Order ID"""
    discounted_amount: Optional[Money] = None
    updated_at: Optional[str] = None
    """Updated Time 更新時間"""
    created_at: Optional[str] = None
    """Created Time 創造時間"""
