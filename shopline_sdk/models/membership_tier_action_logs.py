"""Shopline API 数据模型 - MembershipTierActionLogs"""

from typing import List, Optional

from pydantic import BaseModel

from .membership_tier_action_log import MembershipTierActionLog
from .paginatable import Paginatable


class MembershipTierActionLogs(BaseModel):
    items: Optional[List[MembershipTierActionLog]] = None
    pagination: Optional[Paginatable] = None
