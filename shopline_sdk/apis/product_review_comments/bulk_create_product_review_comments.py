from typing import List, Optional

import aiohttp
from pydantic import BaseModel

# 导入异常类
from shopline_sdk.exceptions import ShoplineAPIError


class ItemsItemSchema(BaseModel):
    """Item model for items"""
    product_id: str
    """Product ID"""
    score: int
    comment: str
    """The content of the review comment"""
    user_id: Optional[str] = None
    """Order ID (if any)"""
    order_id: Optional[str] = None
    """Order ID (if any)"""
    status: Optional[str] = None
    user_name: Optional[str] = None
    """Name of the reviewer (only applicable on imported review)
      評論作者的名稱（只適用於導入評論）"""
    media_ids: Optional[List[str]] = None
    """Array of media ids
      媒體id陣列"""


class Body(BaseModel):
    """请求体模型"""
    items: Optional[List[ItemsItemSchema]] = None


class Response(BaseModel):
    """响应体模型"""
    result: Optional[str] = None
    count: Optional[int] = None


async def call(
        session: aiohttp.ClientSession, body: Optional[Body] = None
) -> Response:
    """
    Bulk Create Product Review Comments
    
    To bulk create product review comments.
    批量創建商品評價。
    
    Path: POST /product_review_comments/bulk
    """
    # 构建请求 URL
    url = "product_review_comments/bulk"

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
                **error_data
            )
        response_data = await response.json()

        # 验证并返回响应数据
        return Response(**response_data)
