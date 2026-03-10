"""Shopline API 数据模型 - UpdatePromotionBody"""

from typing import List, Optional

from pydantic import BaseModel

from .translatable import Translatable


class ConditionsItem(BaseModel):
    """Item model for conditions"""
    id: Optional[str] = None
    """Promotion Condition ID 優惠活動條件ID"""
    min_item_count: Optional[int] = None
    """滿件數量"""
    min_price: Optional[float] = None
    whitelisted_product_ids: Optional[List[str]] = None
    """指定商品條件id"""
    whitelisted_category_ids: Optional[List[str]] = None
    """指定分類條件id"""
    blacklisted_product_ids: Optional[List[str]] = None
    """指定排除商品條件id"""


class Benefit_TiersItem(BaseModel):
    """Item model for benefit_tiers"""
    id: Optional[str] = None
    min_item_count: Optional[int] = None
    """滿件數量"""
    min_price: Optional[float] = None
    discountable_product_ids: Optional[str] = None


class Addon_ProductsItem(BaseModel):
    """Item model for addon_products"""
    addon_product_id: Optional[str] = None
    """Add-on Product‘s ID 加購品ID"""
    discounted_price: Optional[float] = None
    discountable_quantity: Optional[float] = None


class GiftsItem(BaseModel):
    """Item model for gifts"""
    gift_id: Optional[str] = None
    """Gift ID 贈品ID"""
    discounted_point: Optional[float] = None


class UpdatePromotionBody(BaseModel):
    """Payload for updating promotion"""
    title_translations: Optional[Translatable] = None
    discountable_product_ids: Optional[List[str]] = None
    discountable_category_ids: Optional[List[str]] = None
    """Ids of Discounted category 指定商品分類ids"""
    is_accumulated: Optional[bool] = None
    requires_membership: Optional[bool] = None
    """Does it require membership? 設定目標群組 - false: 所有顧客 true: 會員"""
    whitelisted_membership_tier_ids: Optional[List[str]] = None
    """Specific Membership Tiers 適用會員等級"""
    whitelisted_tag_contents: Optional[List[str]] = None
    user_max_use_count: Optional[int] = None
    """Limit per member 每會員最多使用次數 - null = Unlimited 不限使用次數"""
    conditions: Optional[List[ConditionsItem]] = None
    benefit_tiers: Optional[List[Benefit_TiersItem]] = None
    show_coupon: Optional[bool] = None
    max_use_count: Optional[int] = None
    """How many times can this promotion be used? 活動限使用次數 - null = Unlimited 不限使用次數"""
    start_at: Optional[str] = None
    """Promotion start time 活動開始時間"""
    end_at: Optional[str] = None
    """Promotion end time 活動結束時間 - null = no end date 永不過期"""
    whitelisted_delivery_option_ids: Optional[List[str]] = None
    """Delivery options that applicable to the promotion 活動適用送貨方式"""
    whitelisted_payment_ids: Optional[List[str]] = None
    """Payment options that applicable to the promotion 活動適用付款方式"""
    banner_media_ids: Optional[List[str]] = None
    seo_enabled: Optional[bool] = None
    seo_title_translations: Optional[Translatable] = None
    seo_description_translations: Optional[Translatable] = None
    seo_keywords: Optional[str] = None
    term_translations: Optional[Translatable] = None
    addon_products: Optional[List[Addon_ProductsItem]] = None
    gifts: Optional[List[GiftsItem]] = None
