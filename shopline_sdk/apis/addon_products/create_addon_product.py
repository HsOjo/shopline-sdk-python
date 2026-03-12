from typing import List, Optional

import aiohttp
from pydantic import BaseModel, Field

# 导入异常类
from shopline_sdk.exceptions import ShoplineAPIError
# 导入需要的模型
from shopline_sdk.models.addon_product import AddonProduct
from shopline_sdk.models.money import Money
from shopline_sdk.models.translatable import Translatable


class MainProductsItemSchema(BaseModel):
    """Item model for main_products"""
    id: Optional[str] = Field(default=None, alias="_id")
    addon_price: Optional[Money] = None


class Body(BaseModel):
    """请求体模型"""
    title_translations: Optional[Translatable] = None
    unlimited_quantity: Optional[bool] = None
    """Unlimited quantity or not.
      加購品數量是否無限
       -
       true: unlimited quantity
       false: limited quantity"""
    sku: Optional[str] = None
    """Stock Keeping Unit
      加購品貨號"""
    weight: Optional[float] = None
    """Addon Product's Weight (kg)
      加購品重量 (公斤)"""
    media_ids: Optional[List[str]] = None
    start_at: Optional[str] = None
    end_at: Optional[str] = None
    location_id: Optional[str] = None
    tax_type: Optional[str] = None
    """Tax Type
      國內稅項"""
    oversea_tax_type: Optional[str] = None
    """Oversea Tax Type
      海外稅項"""
    product_id: Optional[str] = None
    cost: Optional[Money] = None
    main_products: Optional[List[MainProductsItemSchema]] = None


async def call(
        session: aiohttp.ClientSession, body: Optional[Body] = None
) -> AddonProduct:
    """
    Create Addon Product
    
    To create addon product
    建立加購品
    
    Path: POST /addon_products
    """
    # 构建请求 URL
    url = "addon_products"

    # 构建请求头
    headers = {"Content-Type": "application/json"}

    # 构建请求体
    json_data = body.model_dump(exclude_none=True) if body else None

    # 发起 HTTP 请求
    async with session.post(
            url, json=json_data, headers=headers
    ) as response:
        if response.status >= 400:
            error_data = await response.json()
            raise ShoplineAPIError(
                status_code=response.status,
                error=error_data
            )
        response_data = await response.json()

        # 验证并返回响应数据
        return AddonProduct(**response_data)
