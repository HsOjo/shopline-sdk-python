"""Shopline API 数据模型 - CampaignProduct"""

from typing import Optional

from pydantic import BaseModel

from .money import Money


class CampaignProduct(BaseModel):
    id: Optional[str] = None
    """Affiliate Campaign Unique ID 推薦活動ID"""
    product_id: Optional[str] = None
    """Product ID 商品ID"""
    affiliate_percentage: Optional[float] = None
    """Affiliate percentage 分潤百分比"""
    affiliate_amount: Optional[Money] = None
