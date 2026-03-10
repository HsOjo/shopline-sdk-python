"""Shopline API 数据模型 - UpdateCustomerGroupActivityBody"""

from typing import Optional, Union

from pydantic import BaseModel
from typing_extensions import Literal

from .translatable import Translatable


class Customer_Group_ActivityConfig(BaseModel):
    """Configuration model for customer_group_activity"""
    activity_time: Optional[str] = None
    submitted_at: Optional[str] = None
    activity_status: Optional[Union[
        Literal['draft', 'pending', 'cancelled', 'sending', 'sent', 'failed', 'partially_sent', 'removed'], str]] = None
    """The activity status of the customer group. 此活動目前的狀態"""
    name_translations: Optional[Translatable] = None
    """Activity Name 活動名稱"""


class UpdateCustomerGroupActivityBody(BaseModel):
    """Payload for updating customer group activity"""
    customer_group_activity: Optional[Customer_Group_ActivityConfig] = None
