"""Shopline API 数据模型 - BulkDeleteMetafieldBody"""

from typing import Optional

from pydantic import BaseModel


class BulkDeleteMetafieldBody(BaseModel):
    """Payload for updating metafield"""
    id: Optional[str] = None
    """Metafield Value ID"""
    namespace: Optional[str] = None
    """Namespace"""
    key: Optional[str] = None
    """Key"""
