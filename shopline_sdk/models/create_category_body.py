"""Shopline API 数据模型 - CreateCategoryBody"""

from typing import Optional

from pydantic import BaseModel

# 导入相关模型
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


class CreateCategoryBody(BaseModel):
    """Payload for creating category"""
    category: Optional[CategoryConfig] = None
