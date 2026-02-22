"""Shopline API 数据模型 - CursorBasedPaginatable"""

from typing import Optional

from pydantic import BaseModel


class CursorBasedPaginatable(BaseModel):
    last_id: Optional[str] = None
    """Last ID of result. 最後一筆 ID"""
    limit: Optional[int] = None
    """Numbers of result"""
