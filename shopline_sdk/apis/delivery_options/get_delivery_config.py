from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

class Request(BaseModel):
    """查询参数模型"""
    type: str
    """Region Type
      自訂物流種類"""

async def call(
    session: aiohttp.ClientSession, request: Optional[Request] = None
) -> Dict[str, Any]:
    """
    Get Delivery Config
    
    To get delivery config for pickup
    透過open API獲取自訂物流的設定
    
    Path: GET /delivery_options/delivery_config
    """
    # 构建请求 URL
    url = "delivery_options/delivery_config"

    # 构建查询参数
    params = {}
    if request:
        request_dict = request.model_dump(exclude_none=True)
        for key, value in request_dict.items():
            if value is not None:
                params[key] = value

    # 构建请求头
    headers = {"Content-Type": "application/json"}

    # 发起 HTTP 请求
    async with session.get(
        url, params=params, headers=headers
    ) as response:
        if response.status >= 400:
            error_data = await response.json()
            # 默认错误处理
            raise ShoplineAPIError(
                status_code=response.status,
                **error_data
            )
        response_data = await response.json()
        return response_data