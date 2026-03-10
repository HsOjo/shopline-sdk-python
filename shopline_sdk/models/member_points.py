"""Shopline API 数据模型 - MemberPoints"""

from typing import List, Optional

from pydantic import BaseModel

from .member_point import MemberPoint
from .paginatable import Paginatable


class MemberPoints(BaseModel):
    items: Optional[List[MemberPoint]] = None
    pagination: Optional[Paginatable] = None
