"""Shopline API 数据模型 - PosSetting"""

from typing import Optional

from pydantic import BaseModel


class PosSetting(BaseModel):
    mobile_logo_media_url: Optional[str] = None
    terms_and_condition: Optional[str] = None
    show_title: Optional[bool] = None
    show_original_price: Optional[bool] = None
    show_footer_image: Optional[bool] = None
    apply_platform: Optional[str] = None
    footer_image_media_url: Optional[str] = None
    enable_pos_salesperson_password_required: Optional[bool] = None
    enable_pos_transaction_password_required: Optional[bool] = None
    enable_pos_purchase_order_password_required: Optional[bool] = None
    enable_pos_inventory_count_password_required: Optional[bool] = None
    enable_pos_inventory_transfer_password_required: Optional[bool] = None
    enable_pos_settlement_password_required: Optional[bool] = None
