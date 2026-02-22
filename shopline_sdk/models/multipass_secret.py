"""Shopline API 数据模型 - MultipassSecret"""

from typing import Optional, Union

from pydantic import BaseModel
from typing_extensions import Literal


class MultipassSecret(BaseModel):
    merchant_id: Optional[str] = None
    """Merchant ID"""
    app_id: Optional[str] = None
    """App ID (nullable)"""
    secret: Optional[str] = None
    """Multipass Secret"""
    status: Optional[Union[Literal['active', 'draft'], str]] = None
    """Secret Status - active - draft (inactive)"""
    updated_at: Optional[str] = None
    """Secret last updated time"""
    created_at: Optional[str] = None
    """Secret created time"""
