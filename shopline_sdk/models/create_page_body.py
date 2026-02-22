"""Shopline API 数据模型 - CreatePageBody"""

from typing import Dict, List, Optional

from pydantic import BaseModel

# 导入相关模型
from .link import Link
from .page_section_settings import PageSectionSettings
from .translatable import Translatable


class CreatePageBody(BaseModel):
    """Payload for creating page"""
    type: Optional[str] = None
    """Type of the Page 頁面類別"""
    title_translations: Optional[Translatable] = None
    content_translations: Optional[Translatable] = None
    seo_title_translations: Optional[Translatable] = None
    seo_description_translations: Optional[Translatable] = None
    seo_keywords: Optional[str] = None
    """Key of the page"""
    link: Optional[Link] = None
    use_noindex_meta_tag: Optional[bool] = None
    """Whether the page is searchable on search engines 頁面會否被搜尋引擎搜尋到"""
    sections: Optional[Dict[str, PageSectionSettings]] = None
    sections_order: Optional[List[str]] = None
