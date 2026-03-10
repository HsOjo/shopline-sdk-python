"""Shopline API 数据模型 - DomainsSetting"""

from typing import Optional

from pydantic import BaseModel

from .domains_setting_webmaster import DomainsSettingWebmaster


class DomainsSetting(BaseModel):
    webmasters: Optional[DomainsSettingWebmaster] = None
    """Third Party Domain Tools   第三方網域工具"""
