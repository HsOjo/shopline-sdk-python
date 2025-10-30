from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.server_error import ServerError

class Response(BaseModel):
    """响应体模型"""
    items: Optional[List[Dict[str, Any]]] = None

async def call(
    session: aiohttp.ClientSession
) -> Response:
    """
    Get all orders tags
    
    To get all of the orders tags sorted by alphabetical order
     獲取全部訂單標籤資料
    
    Path: GET /orders/tags
    """
    # 构建请求 URL
    url = "orders/tags"

    # 构建请求头
    headers = {"Content-Type": "application/json"}

    # 发起 HTTP 请求
    async with session.get(
        url, headers=headers
    ) as response:
        if response.status >= 400:
            error_data = await response.json()
            if response.status == 500:
                error_model = ServerError(**error_data)
                raise ShoplineAPIError(
                    status_code=500,
                    error=error_model
                )
            # 默认错误处理
            raise ShoplineAPIError(
                status_code=response.status,
                **error_data
            )
        response_data = await response.json()

        # 验证并返回响应数据
        return Response(**response_data)