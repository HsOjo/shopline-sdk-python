"""Shopline API 数据模型 - UpdateAddonProductBody"""

from typing import List, Optional

from pydantic import BaseModel, Field

# 导入相关模型
from .money import Money
from .translatable import Translatable


class Main_ProductsItem(BaseModel):
    """Item model for main_products"""
    id: Optional[str] = Field(default=None, alias="_id")
    addon_price: Optional[Money] = None


class UpdateAddonProductBody(BaseModel):
    """Payload for updating addon product"""
    title_translations: Optional[Translatable] = None
    media_ids: Optional[List[str]] = None
    unlimited_quantity: Optional[bool] = None
    """Unlimited quantity or not. 加購品數量是否無限  -  true: unlimited quantity  false: limited quantity"""
    start_at: Optional[str] = None
    """Addon Product start time 生效時間"""
    end_at: Optional[str] = None
    """Addon Product end time 過期時間"""
    main_products: Optional[List[Main_ProductsItem]] = None
    location_id: Optional[str] = None
    """custom location id"""
    tax_type: Optional[str] = None
    """Tax Type 國內稅項"""
    oversea_tax_type: Optional[str] = None
    """Oversea Tax Type 海外稅項"""
    sku: Optional[str] = None
    """Stock Keeping Unit 加購品貨號"""
    cost: Optional[Money] = None
    weight: Optional[float] = None
    """Addon Product's Weight (kg) 加購品重量 (公斤)"""
    quantity: Optional[float] = None
    """Current Quantity 加購品目前庫存"""
