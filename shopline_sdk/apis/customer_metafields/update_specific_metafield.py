from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.metafield_value import MetafieldValue
from ...models.update_metafield_body import UpdateMetafieldBody as Body

async def call(
    session: aiohttp.ClientSession, customer_id: str, metafield_id: str, body: Optional[Body] = None
) -> MetafieldValue:
    """
    Update specific metafield
    
    To update information of metafield attached to specify customer by metafield ID
    
    Path: PUT /customers/{customer_id}/metafields/{metafield_id}
    """
    # 构建请求 URL
    url = f"customers/{customer_id}/metafields/{metafield_id}"

    # 构建请求头
    headers = {"Content-Type": "application/json"}

    # 构建请求体
    json_data = body.model_dump(exclude_none=True) if body else None

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
        return MetafieldValue(**response_data)