"""Shopline API 数据模型 - StorefrontOAuthApplication"""

from typing import Optional

from pydantic import BaseModel


class StorefrontOAuthApplication(BaseModel):
    id: Optional[str] = None
    """Application ID"""
    app_id: Optional[str] = None
    """App UID (Client ID used in OAuth requests)"""
    app_secret: Optional[str] = None
    """App Secret (Client secret used in OAuth requests)"""
    name: Optional[str] = None
    """App Name"""
    redirect_uri: Optional[str] = None
    """Redirect URI"""
