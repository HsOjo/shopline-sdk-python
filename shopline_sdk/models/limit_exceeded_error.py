"""Shopline API 数据模型 - LimitExceededError"""

from typing import Any, Dict, Optional

from pydantic import BaseModel


class LimitExceededError(BaseModel):
    message: Optional[str] = None
    """A detailed message of the reason of failure"""
    code: Optional[str] = None
    """An error code"""
    extras: Optional[Dict[str, Any]] = None
    """Optional, Extra information about the error"""
