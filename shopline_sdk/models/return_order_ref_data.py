"""Shopline API 数据模型 - ReturnOrderRefData"""

from typing import Optional

from pydantic import BaseModel


class ReturnOrderRefData(BaseModel):
    return_order_revamp: Optional[str] = None
    """Return order revamp feature flag"""
