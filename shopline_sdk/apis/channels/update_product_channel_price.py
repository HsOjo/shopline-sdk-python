from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.price_set import PriceSet

async def call(
    session: aiohttp.ClientSession, channel_id: str, product_id: str, id: str, data: Optional[Dict[str, Any]] = None
) -> PriceSet:
    """
    Update Product Channel Price
    
    To update product channel price
    更新商品分店價格
    
    Path: PUT /channels/{channel_id}/products/{product_id}/prices/{id}
    """
    # 构建请求 URL
    url = f"channels/{channel_id}/products/{product_id}/prices/{id}"

    # 构建请求头
    headers = {"Content-Type": "application/json"}

    # 构建请求体
    json_data = data if data else None

    # 发起 HTTP 请求
    async with session.put(
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
        return PriceSet(**response_data)