"""Shopline API 数据模型 - UpdateAgentBody"""

from typing import Optional

from pydantic import BaseModel


class UpdateAgentBody(BaseModel):
    """Payload for updating agent"""
    name: Optional[str] = None
    """Name of the agent 員工名稱"""
    email: Optional[str] = None
    """Email of the agent 員工電郵"""
    phone: Optional[str] = None
    """Phone of the agent 員工電話號碼"""
