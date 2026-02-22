"""Shopline API 数据模型 - StorefrontTokens"""

from typing import List, Optional

from pydantic import BaseModel

# 导入相关模型
from .storefront_token import StorefrontToken


class StorefrontTokens(BaseModel):
    items: Optional[List[StorefrontToken]] = None
