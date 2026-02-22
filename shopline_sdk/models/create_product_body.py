"""Shopline API 数据模型 - CreateProductBody"""

from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel
from typing_extensions import Literal

# 导入相关模型
from .product_variation import ProductVariation
from .translatable import Translatable


class ProductConfig(BaseModel):
    """Configuration model for product"""
    price: Optional[float] = None
    """Product Price 原價格"""
    price_sale: Optional[float] = None
    """Product Sale Price 特價"""
    retail_price: Optional[float] = None
    """Retail Price 零售價"""
    member_price: Optional[float] = None
    """Member Price 會員價"""
    cost: Optional[float] = None
    """Product Cost 成本價"""
    product_price_tiers: Optional[Dict[str, str]] = None
    """Membership tier's ID 會員等級ID"""
    hide_price: Optional[bool] = None
    """Hide Price to customers 隱藏價格 - *Default: false"""
    same_price: Optional[bool] = None
    """Main Product and Variation Product share the same price (Including original price and member price)  規格商品是否皆同主商品價格，包含原價格與會員價  1. If same price is true, main product price is required and will be apply to all variation prices  2. If same price is false, variation price is required and each variation can apply different prices."""
    quantity: Optional[float] = None
    """Quantity 商品數量 -  If the product contains variations with quantity, this field will be the sum of quantities of all variations.  Otherwise, the product quantity is between 0 to 9999999.  如果商品有不同規格及數量，商品數量將會是所有規格商品數量的總和。  否則，商品數量要在 0 - 9999999 之間。"""
    unlimited_quantity: Optional[bool] = None
    """Unlimited product quantity or not. 商品數量是否無限"""
    location_id: Optional[str] = None
    """Stock Unit Number 儲位編號"""
    sku: Optional[str] = None
    """Stock Keeping Unit 商品貨號"""
    category_ids: Optional[List[str]] = None
    """Categories' IDs 商品所屬分類之ID"""
    title_translations: Optional[Translatable] = None
    summary_translations: Optional[Translatable] = None
    description_translations: Optional[Translatable] = None
    """Product Description 商品描述"""
    seo_title_translations: Optional[Translatable] = None
    """Title of SEO SEO優化標題"""
    seo_description_translations: Optional[Translatable] = None
    """Description of SEO SEO優化描述"""
    seo_keywords: Optional[str] = None
    """Keywords of SEO SEO關鍵字  *Keywords should be separated by commas (,) max length 160 characters.  關鍵字以逗號(,)分隔, 最長 160字"""
    link: Optional[str] = None
    is_preorder: Optional[bool] = None
    """Pre-ordered or not 是否開放預購"""
    preorder_limit: Optional[int] = None
    """Pre-ordere Limit 預購上限"""
    preorder_note_translations: Optional[Translatable] = None
    """Pre-order Note Info 預購資訊"""
    is_reminder_active: Optional[bool] = None
    """Out-Of-Stock Reminder 商品缺貨是否提醒"""
    show_custom_related_products: Optional[bool] = None
    """Show Custom Related products 顯示相關商品"""
    related_product_ids: Optional[List[str]] = None
    """Custom related products 自訂相關商品"""
    weight: Optional[float] = None
    """Product's Weight (kg) 商品重量 (公斤)"""
    tags: Optional[str] = None
    """Tags 標籤  *Tags are used to search products at the admin panel and help set up the product-related coupons.  標籤功能用作商品搜尋，並能為指定商品設置優惠券的用途。"""
    blacklisted_delivery_option_ids: Optional[List[str]] = None
    """Excluded Delivery Options 排除的送貨方式"""
    blacklisted_payment_ids: Optional[List[str]] = None
    """Excluded Payment Options 排除的付款方式"""
    max_order_quantity: Optional[int] = None
    """set maximum quantity per purchase for this product  商品單次購買上限  *-1 represents there's no quantity limit for each purchase  -1代表無商品單次購買的上限"""
    created_by: Optional[Union[Literal['catcher', 'pos', 'sc'], str]] = None
    supplier_id: Optional[str] = None
    available_start_time: Optional[str] = None
    available_end_time: Optional[str] = None
    schedule_publish_at: Optional[str] = None
    tax_type: Optional[str] = None
    """Tax type 國內稅項"""
    oversea_tax_type: Optional[str] = None
    """Oversea tax type 海外稅項"""
    status: Optional[Union[Literal['active', 'draft', 'removed', 'hidden'], str]] = None
    """Product's status 商品狀態 - true: Published 上架  false: Unpublished 下架 "active": Published 上架 "draft": Unpublished 下架  "hidden": hidden 隱藏  Default: false"""
    images: Optional[List[str]] = None
    """Product Main Photos. If the images field is null, the system will upload a default image.  商品主圖片，如images為空，將會帶入系統預設圖片"""
    detail_images: Optional[List[str]] = None
    """Additional Product Photos 更多商品圖片"""
    variant_options: Optional[List[Dict[str, Any]]] = None
    """Product Variations 商品規格 -  Maximum 3 types of variant option for a product, type allow (color, size, custom_1, custom_2, custom_3)  最多支援三種不同的 type, type 支援(color, size, custom_1, custom_2, custom_3)"""
    variant_custom_type_translations: Optional[List[Dict[str, Any]]] = None
    variations: Optional[List[ProductVariation]] = None
    """Product Variations Data 商品規格資訊"""
    all_variations: Optional[bool] = None
    """Set if all combinations of variation options should be used or not.  設定是否需要使用所有商品規格選項的組合。  when "same_price" is set as "false", "all_variations" is not applicable.  當"same_price"被設定為false，"all_variations"不適用。"""
    channel_id: Optional[str] = None
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
    gtin: Optional[str] = None
    """Barcode 商品條碼編號 - 有規格商品請將請求帶在 variations 欄位中  Requests for products with variants must include them in the variant_options field."""
    feed_variations: Optional[Dict[str, Any]] = None
    """Feed Variations 產品資訊 - 顏色、尺寸、材質"""


class CreateProductBody(BaseModel):
    """Payload for creating product"""
    ignore_product_media_errors: Optional[bool] = None
    """Do not raise error when failed to upload media 上傳圖像失敗時不報錯"""
    default_show_image_selector: Optional[bool] = None
    """Show product variations image on product page 在產品頁面上顯示產品規格圖像"""
    product: Optional[ProductConfig] = None
