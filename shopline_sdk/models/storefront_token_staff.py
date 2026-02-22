"""Shopline API 数据模型 - StorefrontTokenStaff"""

from typing import Optional

from pydantic import BaseModel


class StorefrontTokenStaff(BaseModel):
    """The staff that created this storefront token 創建這令牌的商户"""
    id: Optional[str] = None
    """Staff ID 員工ID"""
    name: Optional[str] = None
    """Staff name 員工名稱"""
    email: Optional[str] = None
    """Staff email 員工電郵"""
