"""Shopline API 数据模型 - EventTrackers"""

from typing import List, Optional

from pydantic import BaseModel

from .event_tracker import EventTracker
from .paginatable import Paginatable


class EventTrackers(BaseModel):
    items: Optional[List[EventTracker]] = None
    pagination: Optional[Paginatable] = None
