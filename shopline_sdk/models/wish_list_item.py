"""Shopline API 数据模型 - WishListItem"""

from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel
from typing_extensions import Literal

from .money import Money
from .product_variation import ProductVariation
from .translatable import Translatable


class ProductConfig(BaseModel):
    """Configuration model for product"""
    id: Optional[str] = None
    """Product's ID 商品ID"""
    title_translations: Optional[Translatable] = None
    field_titles: Optional[List[Dict[str, Any]]] = None
    """Field Title Data 規格名稱"""
    price: Optional[Union[Money, float]] = None
    price_sale: Optional[Union[Money, float]] = None
    hide_price: Optional[bool] = None
    """Hide Price to customers 隱藏價格 - *Default: false"""
    same_price: Optional[bool] = None
    """Main Product and Variation Product share the same price (Including original price and member price)  規格商品是否皆同主商品價格，包含原價格與會員價  1. If same price is true, main product price is required and will be apply to all variation prices  2. If same price is false, variation price is required and each variation can apply different prices."""
    lowest_price: Optional[Money] = None
    max_order_quantity: Optional[int] = None
    """set maximum quantity per purchase for this product  商品單次購買上限  *-1 represents there's no quantity limit for each purchase  -1代表無商品單次購買的上限"""
    status: Optional[Union[Literal['active', 'draft', 'removed', 'hidden'], str]] = None
    """Product's status 商品狀態 - true: Published 上架  false: Unpublished 下架 "active": Published 上架 "draft": Unpublished 下架  "hidden": hidden 隱藏  Default: false"""
    sku: Optional[str] = None
    """Stock Keeping Unit 商品貨號"""
    flash_price_sets: Optional[List[Dict[str, Any]]] = None
    """price for flash campaign 限時促銷價"""
    member_price: Optional[Union[Money, float]] = None
    unlimited_quantity: Optional[bool] = None
    """Unlimited product quantity or not. 商品數量是否無限"""
    quantity: Optional[float] = None
    """Product's Current quantity 商品目前數量 -  *If unlimited_quantity is true, the product has unlimited quantity  regardless of the quantity showing here"""
    available_start_time: Optional[str] = None
    available_end_time: Optional[str] = None
    variation: Optional[ProductVariation] = None


class WishListItem(BaseModel):
    id: Optional[str] = None
    """Wish list item ID."""
    product: Optional[ProductConfig] = None
    variation_key: Optional[str] = None
    """Variation key. Variation 的 key   If this wish list item is not a variation, the variation_key will be an empty string.  如果此 item 是一般商品不是規格，則 variation_key 會是空字串"""
