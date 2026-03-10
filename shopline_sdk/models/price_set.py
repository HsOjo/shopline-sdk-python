"""Shopline API 数据模型 - PriceSet"""

from typing import List, Optional, Union

from pydantic import BaseModel
from typing_extensions import Literal

from .money import Money
from .price_detail import PriceDetail


class PriceSet(BaseModel):
    id: Optional[str] = None
    type: Optional[Union[Literal['pos', 'flash_price'], str]] = None
    """price set type"""
    price: Optional[Money] = None
    status: Optional[str] = None
    """price set status"""
    merchant_id: Optional[str] = None
    """商家 ID"""
    channel_id: Optional[str] = None
    """渠道(實體店) ID"""
    product_id: Optional[str] = None
    """商品 ID"""
    price_sale: Optional[Money] = None
    price_details: Optional[List[PriceDetail]] = None
    """product variation price set"""
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
