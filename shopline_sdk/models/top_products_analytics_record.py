"""Shopline API 数据模型 - TopProductsAnalyticsRecord"""

from typing import Optional

from pydantic import BaseModel

# 导入相关模型
from .money import Money
from .top_products_analytics_record_variation import TopProductsAnalyticsRecordVariation
from .translatable import Translatable


class TopProductsAnalyticsRecord(BaseModel):
    """Product performance 商品表現"""
    id: Optional[str] = None
    """Product's ID 商品ID"""
    image_url: Optional[str] = None
    """URL to the product's image 商品圖片的URL"""
    quantity_sold: Optional[float] = None
    """Quantity sold 出售數量"""
    amount_sold: Optional[Money] = None
    cost: Optional[Money] = None
    gtin: Optional[str] = None
    """Barcode 商品條碼編號"""
    price: Optional[Money] = None
    sku: Optional[str] = None
    """Stock Keeping Unit 商品貨號"""
    title_translations: Optional[Translatable] = None
    supplier_translations: Optional[Translatable] = None
    total_views: Optional[float] = None
    """Total views 總瀏覽量"""
    variations: Optional[TopProductsAnalyticsRecordVariation] = None
