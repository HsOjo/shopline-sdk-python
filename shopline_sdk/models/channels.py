"""Shopline API 数据模型 - Channels"""

from typing import List, Optional

from pydantic import BaseModel

from .channel import Channel
from .paginatable import Paginatable


class Channels(BaseModel):
    pagination: Optional[Paginatable] = None
    items: Optional[List[Channel]] = None
