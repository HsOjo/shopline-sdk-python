"""Shopline API 数据模型 - Jobs"""

from typing import List, Optional

from pydantic import BaseModel

# 导入相关模型
from .job import Job
from .paginatable import Paginatable


class Jobs(BaseModel):
    items: Optional[List[Job]] = None
    pagination: Optional[Paginatable] = None
