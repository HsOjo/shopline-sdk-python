"""Shopline API 数据模型 - Agents"""

from typing import List, Optional

from pydantic import BaseModel

from .agent import Agent
from .paginatable import Paginatable


class Agents(BaseModel):
    items: Optional[List[Agent]] = None
    pagination: Optional[Paginatable] = None
