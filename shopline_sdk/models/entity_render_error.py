"""Shopline API 数据模型 - EntityRenderError"""

from typing import Optional

from pydantic import BaseModel


class EntityRenderError(BaseModel):
    """Unprocessable entity"""
    message: Optional[str] = None
    code: Optional[str] = None
