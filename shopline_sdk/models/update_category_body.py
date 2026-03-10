"""Shopline API 数据模型 - UpdateCategoryBody"""

from typing import Optional

from pydantic import BaseModel

from .translatable import Translatable


class CategoryConfig(BaseModel):
    """Configuration model for category"""
    name_translations: Optional[Translatable] = None
    seo_title_translations: Optional[Translatable] = None
    seo_description_translations: Optional[Translatable] = None
    seo_keywords: Optional[str] = None
    """SEO Keyword SEO 關鍵字"""
    seo_link: Optional[str] = None
    """SEO url 自訂SEO url"""
    parent_id: Optional[str] = None
    """Parent Category ID 母分類ID"""
    banner_url: Optional[str] = None
    """Category Banner Picture 分類横幅圖片"""
    priority: Optional[float] = None
    """Weight to control sorting 分類權重"""


class UpdateCategoryBody(BaseModel):
    """Payload for updating category"""
    category: Optional[CategoryConfig] = None
