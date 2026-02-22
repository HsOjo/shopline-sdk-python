"""Shopline API 数据模型 - TitleTranslations"""

from typing import Optional

from pydantic import BaseModel, Field


class TitleTranslations(BaseModel):
    en: Optional[str] = None
    zh_hant: Optional[str] = Field(default=None, alias="zh-hant")
    zh_cn: Optional[str] = Field(default=None, alias="zh-cn")
    vi: Optional[str] = None
    th: Optional[str] = None
