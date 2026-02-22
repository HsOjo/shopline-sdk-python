"""Shopline API 数据模型 - OrderTag"""

from typing import Optional

from pydantic import BaseModel


class OrderTag(BaseModel):
    content: Optional[str] = None
    """Text content of the tag 標籤內容"""
