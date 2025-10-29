from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError


class ProductsItem(BaseModel):
    """Item model for products"""
    id: Optional[str] = None
    """Product Id
      商品 ID"""
    variation_id: Optional[str] = None
    """Variation Id
      款式 ID"""

class Request(BaseModel):
    """请求体模型"""
    affiliate_campaign_id: Optional[str] = None
    """Campaign Id
      推薦活動 ID"""
    products: Optional[List[ProductsItem]] = None
    """Products
      商品資料"""

class Response(BaseModel):
    """响应体模型"""
    link: Optional[str] = None

async def call(
    session: aiohttp.ClientSession, request: Optional[Request] = None
) -> Response:
    """
    Generate Merchant's express cart link
    
    To get merchant's express cart link
    產生快速結帳網址
    
    Path: POST /merchants/generate_express_link
    """
    # 构建请求 URL
    url = "merchants/generate_express_link"

    # 构建请求头
    headers = {"Content-Type": "application/json"}

    # 构建请求体
    json_data = request.model_dump(exclude_none=True) if request else None

    # 发起 HTTP 请求
    async with session.post(
        url, json=json_data, headers=headers
    ) as response:
        if response.status >= 400:
            error_data = await response.json()
            # 默认错误处理
            raise ShoplineAPIError(
                status_code=response.status,
                **error_data
            )
        response_data = await response.json()

        # 验证并返回响应数据
        return Response(**response_data)