"""Shopline API 数据模型 - ProductSubscription"""

from typing import Optional, Union

from pydantic import BaseModel
from typing_extensions import Literal

from .translatable import Translatable


class ProductSubscription(BaseModel):
    id: Optional[str] = None
    """Order item's ID (ID of an order item's collection, including item_type, item_id..and so on)  系統自行創建訂單品項ID"""
    recurring_count: Optional[int] = None
    """Subscription Term 定期購訂單期數"""
    duration: Optional[int] = None
    """Number of subscription cycle intervals 定期購週期長度"""
    duration_type: Optional[Union[Literal['year', 'month', 'day'], str]] = None
    """Unit of subscription cycle interval 定期購週期單位"""
    next_billing_at: Optional[str] = None
    """Next billing date 下次產單日期"""
    status: Optional[Union[Literal['active', 'inactive'], str]] = None
    """Status 狀態"""
    customer_name: Optional[str] = None
    """Customer's Name 顧客姓名"""
    customer_email: Optional[str] = None
    """Customer's Email 顧客Email"""
    product_name: Optional[Translatable] = None
    initial_billing_at: Optional[str] = None
    """Initial billing date 最初產單日期 possibly null 可能為null"""
    created_at: Optional[str] = None
    """Created date 創建時間"""
    updated_at: Optional[str] = None
    """Updated date 更新時間"""
    enable_apply_user_credits: Optional[bool] = None
    """Enable apply user credits 是否開啟子單自動折抵購物金"""
