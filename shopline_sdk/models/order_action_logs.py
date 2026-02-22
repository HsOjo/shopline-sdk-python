"""Shopline API 数据模型 - OrderActionLogs"""

from typing import List, Optional

from pydantic import BaseModel

# 导入相关模型
from .order_action_log import OrderActionLog


class OrderActionLogs(BaseModel):
    items: Optional[List[OrderActionLog]] = None
