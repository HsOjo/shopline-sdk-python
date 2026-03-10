"""Shopline API 数据模型 - MultipassLinkings"""

from typing import List, Optional

from pydantic import BaseModel

from .multipass_linking import MultipassLinking


class MultipassLinkings(BaseModel):
    result: Optional[str] = None
    """operation result"""
    linkings: Optional[List[MultipassLinking]] = None
    next: Optional[str] = None
    """for pagination on next call, return items since this ID"""
