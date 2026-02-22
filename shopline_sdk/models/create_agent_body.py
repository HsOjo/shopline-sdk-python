"""Shopline API 数据模型 - CreateAgentBody"""

from typing import Optional

from pydantic import BaseModel


class CreateAgentBody(BaseModel):
    """Payload for creating agent"""
    name: str
    """Name of the agent 員工名稱"""
    pin_code: str
    """Pin code of the agent 員工 pin code"""
    email: Optional[str] = None
    """Email of the agent 員工電郵"""
    phone: Optional[str] = None
    """Phone of the agent 員工電話號碼"""
