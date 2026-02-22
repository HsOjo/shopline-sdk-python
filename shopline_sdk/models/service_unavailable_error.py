"""Shopline API 数据模型 - ServiceUnavailableError"""

from typing import Any, Dict, Optional

from pydantic import BaseModel


class ServiceUnavailableError(BaseModel):
    message: Optional[str] = None
    code: Optional[str] = None
    extras: Optional[Dict[str, Any]] = None
    """Optional, Extra information about the error"""
