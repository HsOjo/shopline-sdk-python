"""Shopline API 数据模型 - CartPromotion"""

from typing import Optional

from pydantic import BaseModel

# 导入相关模型
from .translatable import Translatable


class CartPromotion(BaseModel):
    id: Optional[str] = None
    """優惠 ID"""
    title_translations: Optional[Translatable] = None
    """Title Translations 優惠標題"""
    discount_type: Optional[str] = None
    """Discount Type 優惠類型"""
    is_extended_promotion: Optional[bool] = None
    """Is Extend Promotion 是否是多階層優惠"""
