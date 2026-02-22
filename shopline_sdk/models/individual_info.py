"""Shopline API 数据模型 - IndividualInfo"""

from typing import Optional

from pydantic import BaseModel


class IndividualInfo(BaseModel):
    identity_number: Optional[str] = None
    """Identity number 身分證字號"""
    first_name: Optional[str] = None
    """First name 名字"""
    last_name: Optional[str] = None
    """Last name 姓氏"""
