"""Shopline API 数据模型 - LayoutsSetting"""

from typing import Optional

from pydantic import BaseModel

# 导入相关模型
from .global_section_settings import GlobalSectionSettings


class LayoutsSetting(BaseModel):
    announcement: Optional[GlobalSectionSettings] = None
    header: Optional[GlobalSectionSettings] = None
    footer: Optional[GlobalSectionSettings] = None
