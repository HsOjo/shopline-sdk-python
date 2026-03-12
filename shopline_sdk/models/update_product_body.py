"""Shopline API 数据模型 - UpdateProductBody"""

from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel
from typing_extensions import Literal

from .product_variation import ProductVariation
from .translatable import Translatable


class Variant_Custom_Type_TranslationsItem(BaseModel):
    """Item model for variant_custom_type_translations"""
    name_translations: Optional[Translatable] = None
    type: Optional[str] = None


class Variant_OptionsItem(BaseModel):
    """Item model for variant_options"""
    id: Optional[str] = None
    name_translations: Optional[Translatable] = None
    type: Optional[Union[Literal['color', 'size', 'custom_1', 'custom_2', 'custom_3'], str]] = None
    media: Optional[Dict[str, Any]] = None
    index: Optional[int] = None


class Feed_VariationsConfig(BaseModel):
    """Configuration model for feed_variations"""
    color: Optional[Union[Dict[str, Any], str]] = None
    """Color 產品資訊 - 顏色 -  有規格商品請將請求帶在 variations 欄位中  Requests for products with variants must include them in the variations field.  若為有規格商品且規格類型為顏色，則不允許調整產品資訊 - 顏色  If the type of variant_options is color, feed_variations.color is not allowed to change."""
    size: Optional[Union[Dict[str, Any], str]] = None
    """Size 產品資訊 - 尺寸 - 有規格商品請將請求帶在 variations 欄位中  Requests for products with variants must include them in the variations field.  若為有規格商品且規格類型為尺寸，則不允許調整產品資訊 - 尺寸  If the type of variant_options is size, feed_variations.size is not allowed to change."""
    material: Optional[str] = None
    """Material 產品資訊 - 材質 - 有規格商品請將請求帶在 variations 欄位中  Requests for products with variants must include them in the variations field."""


class UpdateProductBody(BaseModel):
    """Payload for updating product"""
    title_translations: Optional[Translatable] = None
    summary_translations: Optional[Translatable] = None
    description_translations: Optional[Translatable] = None
    """Product Description 商品描述"""
    show_custom_related_products: Optional[bool] = None
    """Show Custom Related products 顯示相關商品"""
    related_product_ids: Optional[List[str]] = None
    """Custom related products 自訂相關商品"""
    same_price: Optional[bool] = None
    """Main Product and Variation Product share the same price (Including original price and member price)  規格商品是否皆同主商品價格，包含原價格與會員價  1. If same price is true, main product price is required and will be apply to all variation prices  2. If same price is false, variation price is required and each variation can apply different prices."""
    location_id: Optional[str] = None
    """Stock Unit Number 儲位編號"""
    sku: Optional[str] = None
    """Stock Keeping Unit 商品貨號"""
    seo_title_translations: Optional[Translatable] = None
    """Title of SEO SEO優化標題"""
    seo_description_translations: Optional[Translatable] = None
    """Description of SEO SEO優化描述"""
    seo_keywords: Optional[str] = None
    """Keywords of SEO SEO關鍵字  *Keywords should be separated by commas (,) max length 160 characters.  關鍵字以逗號(,)分隔, 最長 160字"""
    link: Optional[str] = None
    is_reminder_active: Optional[bool] = None
    """Out-Of-Stock Reminder 商品缺貨是否提醒"""
    is_preorder: Optional[bool] = None
    """Pre-ordered or not 是否開放預購"""
    preorder_limit: Optional[int] = None
    """Pre-ordere Limit 預購上限"""
    preorder_note_translations: Optional[Translatable] = None
    """Pre-order Note Info 預購資訊"""
    max_order_quantity: Optional[int] = None
    """set maximum quantity per purchase for this product  商品單次購買上限  *-1 represents there's no quantity limit for each purchase  -1代表無商品單次購買的上限"""
    weight: Optional[float] = None
    """Product's Weight (kg) 商品重量 (公斤)"""
    tags: Optional[str] = None
    """Tags 標籤  *Tags are used to search products at the admin panel and help set up the product-related coupons.  標籤功能用作商品搜尋，並能為指定商品設置優惠券的用途。"""
    blacklisted_delivery_option_ids: Optional[List[str]] = None
    """Excluded Delivery Options 排除的送貨方式"""
    blacklisted_payment_ids: Optional[List[str]] = None
    """Excluded Payment Options 排除的付款方式"""
    available_start_time: Optional[str] = None
    available_end_time: Optional[str] = None
    schedule_publish_at: Optional[str] = None
    category_ids: Optional[List[str]] = None
    """Categories' IDs 商品所屬分類之ID"""
    tax_type: Optional[str] = None
    """Tax type 國內稅項"""
    oversea_tax_type: Optional[str] = None
    """Oversea tax type 海外稅項"""
    status: Optional[Union[Literal['active', 'draft', 'removed', 'hidden'], str]] = None
    """Product's status 商品狀態 - true: Published 上架  false: Unpublished 下架 "active": Published 上架 "draft": Unpublished 下架  "hidden": hidden 隱藏  Default: false"""
    images: Optional[List[str]] = None
    detail_images: Optional[List[str]] = None
    """Additional Product Photos 更多商品圖片"""
    gtin: Optional[str] = None
    """Barcode 商品條碼編號 - 有規格商品請將請求帶在 variations 欄位中  Requests for products with variants must include them in the variant_options field."""
    barcode_type: Optional[Union[Literal['Code 128', 'Bookland EAN', 'ISBN'], str]] = None
    """Barcode type 商品條碼編號類別"""
    variant_custom_type_translations: Optional[List[Variant_Custom_Type_TranslationsItem]] = None
    variant_options: Optional[List[Variant_OptionsItem]] = None
    """Product Variations 商品規格 -  Maximum 3 types of variant option for a product, type allow (color, size, custom_1, custom_2, custom_3)  最多支援三種不同的 type, type 支援(color, size, custom_1, custom_2, custom_3)"""
    is_replace_variations: Optional[bool] = None
    """Is replacing variations? 是否更換全部規格?"""
    variations: Optional[List[ProductVariation]] = None
    """Product Variations Data 商品規格資訊"""
    unlimited_quantity: Optional[bool] = None
    """Unlimited product quantity or not. 商品數量是否無限"""
    default_show_image_selector: Optional[bool] = None
    """Show variation photos. 展示商品規格圖像。"""
    allow_gift: Optional[bool] = None
    """Specifies whether the item can be set as a gift.  是否可以設為贈品  true: the product can be set as a gift.  false: the product cannot be set as a gift."""
    is_custom: Optional[bool] = None
    """Specifies whether the item can be set as a customized product. 是否可以設為訂制商品  true: the product can be set as a custom product.  false: the product cannot be set as a custom product."""
    brand: Optional[str] = None
    """Product brand 商品品牌 字數不可超過 100 字  Max length is 100 characters."""
    gender: Optional[Union[Literal['unisex', 'male', 'female'], str]] = None
    """Product Category: Gender 產品類別：性別 -  male 男性  female 女性  unisex 男女通用 (default)"""
    age_group: Optional[Union[Literal['all_ages', 'adult', 'teen', 'kids', 'toddler', 'infant', 'newborn'], str]] = None
    """Product Category:Age Group 產品類別：年齡層 -  all_ages 全年齡 (default)  adult 成人  teen 青少年  kids 兒童  toddler 幼兒  infant 嬰兒  newborn 新生兒"""
    adult: Optional[Union[Literal['yes', 'no'], str]] = None
    """Product Category:Adult 產品類別：成人 -  yes: the product is classified as adult content  no: the product is not classified as adult content (default)"""
    condition: Optional[Union[Literal['new', 'refurbished', 'used'], str]] = None
    """Product Category:Condition 產品類別：狀況 -  new 新品 (default)  refurbished 整新品  used 二手"""
    mpn: Optional[str] = None
    """Manufacturer Part Number 製造編號 - 有規格商品請將請求帶在 variations 欄位中  Requests for products with variants must include them in the variant_options field."""
    feed_variations: Optional[Union[Feed_VariationsConfig, List[Feed_VariationsConfig]]] = None
    """Feed Variations 產品資訊 - 顏色、尺寸、材質"""
