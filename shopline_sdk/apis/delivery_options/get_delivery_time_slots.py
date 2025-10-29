from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.delivery_time_slot import DeliveryTimeSlot

class Request(BaseModel):
    """查询参数模型"""
    date: Optional[str] = None
    """Date
      指定日期"""
    ignore_availability: Optional[bool] = None
    """Ignore Availability
      是否忽略可用性"""

class Response(BaseModel):
    """响应体模型"""
    items: Optional[List[DeliveryTimeSlot]] = None

async def call(
    session: aiohttp.ClientSession, delivery_option_id: str, request: Optional[Request] = None
) -> Response:
    """
    Get Delivery Time Slots
    
    To get all delivery time slots with open API
    透過open API獲取所有的送貨時段
    
    Path: GET /delivery_options/{delivery_option_id}/delivery_time_slots
    """
    # 构建请求 URL
    url = f"delivery_options/{delivery_option_id}/delivery_time_slots"

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

        # 验证并返回响应数据
        return Response(**response_data)