"""Shopline API 数据模型 - CreateCustomerGroupActivityBody"""

from typing import Optional, Union

from pydantic import BaseModel
from typing_extensions import Literal

# 导入相关模型
from .translatable import Translatable


class Customer_Group_ActivityConfig(BaseModel):
    """Configuration model for customer_group_activity"""
    name_translations: Translatable
    """Activity Name 活動名稱"""
    ref_id: str
    """Reference ID of the activity. 關聯此活動的外部ID"""
    type: str
    """Type of the activity. 此活動的類別"""
    activity_status: Union[
        Literal['draft', 'pending', 'cancelled', 'sending', 'sent', 'failed', 'partially_sent', 'removed'], str]
    """The activity status of the customer group. 此活動目前的狀態"""
    activity_time: Optional[str] = None
    submitted_at: Optional[str] = None


class CreateCustomerGroupActivityBody(BaseModel):
    """Payload for creating customer group activity"""
    customer_group_activity: Optional[Customer_Group_ActivityConfig] = None
