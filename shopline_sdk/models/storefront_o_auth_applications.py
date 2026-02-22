"""Shopline API 数据模型 - StorefrontOAuthApplications"""

from typing import List, Optional

from pydantic import BaseModel

# 导入相关模型
from .storefront_o_auth_application import StorefrontOAuthApplication


class StorefrontOAuthApplications(BaseModel):
    items: Optional[List[StorefrontOAuthApplication]] = None
