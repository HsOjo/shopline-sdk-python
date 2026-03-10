"""Shopline API 数据模型 - CreateDeliveryOptionBody"""

from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel
from typing_extensions import Literal

from .translatable import Translatable


class Config_DataConfig(BaseModel):
    """Configuration model for config_data"""
    lead_time: Optional[int] = None
    """Lead Time (no more than 30 days) 預估備貨天數（最多30天）"""
    max_lead_time: Optional[int] = None
    """Selectable day length (from lead time)  備貨期後可指定的天數長度"""
    excluded_weekdays: Optional[List[int]] = None
    """Sunday=0; Monday=1"""
    excluded_dates: Optional[List[str]] = None
    delivery_time_required: Optional[bool] = None
    """Specified Timeslot (Enabled: Customers can set up estimated delivery arrival time in case no receiver at home.)  出貨訂單需指定時段 (啟用功能：可以設定商品到貨的時間，避免無人收貨的情況。)"""
    specific_delivery_time_translations: Optional[Translatable] = None
    delivery_target_area: Optional[Union[Literal['localOnly', 'outlyingIslandOnly', 'all'], str]] = None
    """For Taiwan only. You can set whether Main area or Outlying Island delivery service  台灣地區可進階設定本島/外島的配送區域    localOnly: Main Area delivery service 提供本島配送  outlyingIslandOnly: Outlying Island delivery service 提供外島配送  all: all of the above 以上皆是"""


class CreateDeliveryOptionBody(BaseModel):
    """Payload for creating delivery option"""
    status: Optional[Union[Literal['active', 'draft'], str]] = None
    """Delivery Option Status 送貨方式狀態 - Status allows: active 啟用中 draft 隱藏"""
    name_translations: Translatable
    description_translations: Optional[Translatable] = None
    show_description_on_checkout: Optional[bool] = None
    """Display description on the checkout page 在結帳頁面上顯示送貨方式簡介"""
    delivery_time_description_translations: Optional[Translatable] = None
    config_data: Optional[Config_DataConfig] = None
    requires_customer_address: Optional[bool] = None
    """Requires Customer Address 需要顧客提供地址"""
    fee_type: Union[Literal['flat', 'flat_weight', 'subtotal', 'item_count', 'sl_logistic'], str]
    delivery_rates: List[Dict[str, Any]]
    region_type: Optional[Union[Literal['custom'], str]] = None
    """Delivery Option Code 送貨方式代碼  Only support creating "custom" region_type through open api"""
    delivery_type: Optional[Union[Literal['custom'], str]] = None
    """Only support creating "custom" delivery_type through open api"""
