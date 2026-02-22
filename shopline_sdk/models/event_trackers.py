"""Shopline API 数据模型 - EventTrackers"""

from typing import List, Optional

from pydantic import BaseModel

# 导入相关模型
from .event_tracker import EventTracker
from .paginatable import Paginatable


class EventTrackers(BaseModel):
    items: Optional[List[EventTracker]] = None
    pagination: Optional[Paginatable] = None
