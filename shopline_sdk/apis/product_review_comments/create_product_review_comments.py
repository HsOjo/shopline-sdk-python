from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.product_review_comment import ProductReviewComment

async def call(
    session: aiohttp.ClientSession, data: Optional[Dict[str, Any]] = None
) -> ProductReviewComment:
    """
    Create Product Review Comments
    
    To create a product review comment.
    創建一個商品評價。
    
    Path: POST /product_review_comments
    """
    # 构建请求 URL
    url = "product_review_comments"

    # 构建请求头
    headers = {"Content-Type": "application/json"}

    # 构建请求体
    json_data = data if data else None

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
        return ProductReviewComment(**response_data)