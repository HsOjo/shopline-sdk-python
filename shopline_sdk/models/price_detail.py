"""Shopline API 数据模型 - PriceDetail"""

from typing import Optional

from pydantic import BaseModel

from .money import Money


class PriceDetail(BaseModel):
    variation_key: Optional[str] = None
    """ProductVariation's ID 商品規格ID"""
    price: Optional[Money] = None
    price_sale: Optional[Money] = None
