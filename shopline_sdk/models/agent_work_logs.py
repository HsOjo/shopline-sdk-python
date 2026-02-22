"""Shopline API 数据模型 - AgentWorkLogs"""

from typing import List, Optional

from pydantic import BaseModel

# 导入相关模型
from .agent_work_log import AgentWorkLog


class AgentWorkLogs(BaseModel):
    items: Optional[List[AgentWorkLog]] = None
