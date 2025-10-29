"""Shopline API 数据模型 - CreateCustomerGroupActivityBody"""

from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from typing_extensions import Literal

# 导入相关模型
from .customer_group_activity import CustomerGroupActivity
from .translatable import Translatable



class Customer_Group_ActivityConfig(BaseModel):
    """Configuration model for customer_group_activity"""
    name_translations: Translatable
    ref_id: str
    type: str
    activity_status: Literal['draft', 'pending', 'cancelled', 'sending', 'sent', 'failed', 'partially_sent', 'removed']
    activity_time: Optional[str] = None
    submitted_at: Optional[str] = None

class CreateCustomerGroupActivityBody(BaseModel):
    """Payload for creating customer group activity"""
    customer_group_activity: Optional[Customer_Group_ActivityConfig] = None