from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.addon_product import AddonProduct
from ...models.server_error import ServerError

async def call(
    session: aiohttp.ClientSession, id: str, data: Optional[Dict[str, Any]] = None
) -> AddonProduct:
    """
    Update Addon Product
    
    To update information about existing addon product with open API.
    透過open API 更新加購品
    
    Path: PUT /addon_products/{id}
    """
    # 构建请求 URL
    url = f"addon_products/{id}"

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
            if response.status == 500:
                error_model = ServerError(**error_data)
                raise ShoplineAPIError(
                    status_code=500,
                    error=error_model,
                    **error_data
                )
            # 默认错误处理
            raise ShoplineAPIError(
                status_code=response.status,
                **error_data
            )
        response_data = await response.json()

        # 验证并返回响应数据
        return AddonProduct(**response_data)