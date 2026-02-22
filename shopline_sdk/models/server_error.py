"""Shopline API 数据模型 - ServerError"""

from typing import Optional

from pydantic import BaseModel


class ServerError(BaseModel):
    message: Optional[str] = None
    """A detailed message of the reason of failure"""
    code: Optional[str] = None
    """An error code"""
