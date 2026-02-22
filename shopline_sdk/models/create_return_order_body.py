"""Shopline API 数据模型 - CreateReturnOrderBody"""

from typing import Any, List, Optional

from pydantic import BaseModel


class Payment_OptionConfig(BaseModel):
    """Configuration model for payment_option"""
    id: Optional[str] = None
    """payment option id, required when return_by is not shop 支付信息ID"""
    key: Optional[str] = None
    """payment option key, required when return_by is shop 支付信息key"""


class Delivery_OptionConfig(BaseModel):
    """Configuration model for delivery_option"""
    id: Optional[str] = None
    """delivery option key 物流ID"""
    key: Optional[str] = None
    """delivery option id 物流key"""


class CreateReturnOrderBody(BaseModel):
    """Payload for creating return order"""
    order_id: str
    """Order ID"""
    recipient_name: Optional[str] = None
    """Recipient Name 收件人姓名"""
    recipient_phone: Optional[str] = None
    """Recipient Phone 收件人電話號碼"""
    recipient_phone_country_code: Optional[str] = None
    """Recipient Phone 收件人電話號碼國碼"""
    country: Optional[str] = None
    """Country Code 國家代碼"""
    postcode: Optional[str] = None
    """ZIP code 郵政編號"""
    city: Optional[str] = None
    """City 城市"""
    state: Optional[str] = None
    """Stage or Region 州/省/地區"""
    district: Optional[str] = None
    """district 區域"""
    address_1: Optional[str] = None
    """Address 1 地址 1"""
    address_2: Optional[str] = None
    """Address 1 地址 2 (這裡原則上會自動帶入地址所在行政區)"""
    logistic_codes: Optional[List[str]] = None
    payment_option: Payment_OptionConfig
    """payment option 支付信息"""
    delivery_option: Delivery_OptionConfig
    """delivery option 物流信息"""
    subtotal_items: Any
    bank_account: Optional[Any] = None
    """bank account, available when payment option type is bank_transfer_return  銀行賬號，當payment option type是bank_transfer_return時可用"""
    returned_by: Optional[Any] = None
    """returned by which channel 訂單被退途徑"""
