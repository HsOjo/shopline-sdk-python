"""Shopline API 数据模型 - UnprocessableEntityError"""

from typing import Any, Dict, Optional

from pydantic import BaseModel


class UnprocessableEntityError(BaseModel):
    error: Optional[str] = None
    """A detailed message of the reason of failure"""
    message: Optional[str] = None
    """A detailed message of the reason of failure"""
    code: Optional[str] = None
    """An error code"""
    extras: Optional[Dict[str, Any]] = None
    """An extra information of the reason of failure"""
