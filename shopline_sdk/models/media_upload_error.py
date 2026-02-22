"""Shopline API 数据模型 - MediaUploadError"""

from typing import List, Optional

from pydantic import BaseModel


class MediaUploadError(BaseModel):
    error: Optional[List[str]] = None
    """A detailed array of messages of the reason of failure"""
