"""Shopline API 数据模型 - UpdateGiftBody"""

from typing import List, Optional

from pydantic import BaseModel

# 导入相关模型
from .translatable import Translatable


class UpdateGiftBody(BaseModel):
    """Payload for updating gift"""
    title_translations: Optional[Translatable] = None
    unlimited_quantity: Optional[bool] = None
    """Unlimited gift quantity or not. 贈品數量是否無限"""
    sku: Optional[str] = None
    """Stock Keeping Unit 贈品貨號"""
    cost: Optional[Translatable] = None
    weight: Optional[float] = None
    """Weight of Gift (kg) 贈品重量 (公斤重)"""
    quantity: Optional[float] = None
    """Current Quantity 贈品目前庫存"""
    media_ids: Optional[List[str]] = None
