"""Shopline API 数据模型 - CreateProductVariationBody"""

from typing import Dict, List, Optional, Union

from pydantic import BaseModel
from typing_extensions import Literal

from .translatable import Translatable


class Variant_OptionsItem(BaseModel):
    """Item model for variant_options"""
    name_translations: Translatable
    type: Union[Literal['color', 'size', 'custom_1', 'custom_2', 'custom_3'], str]
    media_id: Optional[str] = None
    """ID of the image to represent the variation 用以表達該商品規枱的圖片ID"""


class CreateProductVariationBody(BaseModel):
    """Payload for creating product variation"""
    location_id: Optional[str] = None
    """Stock Unit Number 儲位編號"""
    sku: Optional[str] = None
    """Stock Keeping Unit 商品貨號"""
    price: Optional[float] = None
    """Price (Note: Cannot be set to null. Product with a price of 0 cannot be sold.)  原價格 (備註：不能設定為null。價格為0的商品不能被售出)"""
    retail_price: Optional[float] = None
    """Retail Price 零售價"""
    product_price_tiers: Optional[Dict[str, str]] = None
    """Membership tier's ID 會員等級ID"""
    member_price: Optional[float] = None
    """Member Price 會員價"""
    quantity: Optional[int] = None
    """Product Variation Quantity 規格商品數量 -  Directly update the quantity of the variation. The quantity is between -9999999 to 9999999.  直接更新規格商品數量。商品數量要在 -9999999 - 9999999 之間。"""
    preorder_limit: Optional[int] = None
    """Pre-ordere Limit 預購上限"""
    image: Optional[str] = None
    """Link of Images 圖片連結"""
    price_sale: Optional[float] = None
    """Price on sale  (Note: Cannot be set to null.   Product with a price_sale of 0 will be sold at its original price.)  特價 (備註：不能設定為null。特價為0的商品會以原價售出)"""
    cost: Optional[float] = None
    """Cost (Note: Cannot be set to null)  成本 (備註：不能設定為null)"""
    weight: Optional[float] = None
    """Weight (kg) 重量 (公斤)"""
    gtin: Optional[str] = None
    """Barcode 商品條碼編號"""
    ignore_product_media_errors: Optional[bool] = None
    """Will ignore errors when media upload failed. 圖像上傳失敗時將忽略錯誤。"""
    default_show_image_selector: Optional[bool] = None
    """Show variation photos. 展示商品規格圖像。"""
    variant_options: Optional[List[Variant_OptionsItem]] = None
    """Product Variations 商品規格 -  *Maximum allows 3 types of variant option for a product, type allow (color, size, custom_1, custom_2, custom_3)  最多支援三種不同的規格種類，支援color, size, custom_1, custom_2, custom_3"""
