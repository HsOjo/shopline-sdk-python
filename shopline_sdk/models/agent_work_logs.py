"""Shopline API 数据模型 - AgentWorkLogs"""

from typing import List, Optional

from pydantic import BaseModel

from .agent_work_log import AgentWorkLog


class AgentWorkLogs(BaseModel):
    items: Optional[List[AgentWorkLog]] = None
