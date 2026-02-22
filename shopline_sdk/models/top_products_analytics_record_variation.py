"""Shopline API 数据模型 - TopProductsAnalyticsRecordVariation"""

from typing import Optional

from pydantic import BaseModel

# 导入相关模型
from .money import Money
from .translatable import Translatable


class TopProductsAnalyticsRecordVariation(BaseModel):
    id: Optional[str] = None
    """Product Variation's ID 規格 ID"""
    amount_sold: Optional[Money] = None
    cost: Optional[Money] = None
    discount: Optional[Money] = None
    gross_profit: Optional[Money] = None
    gross_profit_margin: Optional[float] = None
    """Gross profit margin 毛利率"""
    gtin: Optional[str] = None
    """Barcode 商品條碼編號"""
    net_sold: Optional[float] = None
    """Net amount sold 折後售出金額"""
    offline_quantity: Optional[int] = None
    """Quantity sold on offline channel 於線下銷售渠道售出的數量"""
    online_quantity: Optional[int] = None
    """Quantity sold on online channel 於線上銷售渠道售出的數量"""
    price: Optional[Money] = None
    quantity_sold: Optional[int] = None
    """Quantity sold 售出數量"""
    sku: Optional[str] = None
    """Stock Keeping Unit 貨號"""
    title_translations: Optional[Translatable] = None
    product_id: Optional[str] = None
    """Product's ID 商品ID"""
