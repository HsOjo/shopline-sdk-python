from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.order import Order
from ...models.order_delivery_address import OrderDeliveryAddress
from ...models.server_error import ServerError
from ...models.unprocessable_entity_error import UnprocessableEntityError

class Request(BaseModel):
    """请求体模型"""
    order: Optional[Dict[str, Any]] = None
    is_registering_as_member: Optional[bool] = None
    """Do you want to set the customer as a member?
      是否要將此筆訂單顧客設為會員？
      -
      *Default: false"""
    is_inventory_fulfillment: Optional[bool] = None
    """Do you want to deduct the inventory numbers after the order is created?
      此筆訂單是否要扣掉庫存？
      -
      *Default:false"""
    mail_notify: Optional[bool] = None
    """Do you want to notify the customer of the order creation by email ?
      此筆訂單成立之後是否要通知顧客？
      -
      *Default:false"""

async def call(
    session: aiohttp.ClientSession, request: Optional[Request] = None
) -> Order:
    """
    Create Order
    
    To create an order with open API
    透過open API創建一筆新訂單
    
    Path: POST /orders
    """
    # 构建请求 URL
    url = "orders"

    # 构建查询参数
    params = {}
    if request:
        request_dict = request.model_dump(exclude_none=True)
        for key, value in request_dict.items():
            if value is not None:
                params[key] = value

    # 构建请求头
    headers = {"Content-Type": "application/json"}

    # 构建请求体
    json_data = request.model_dump(exclude_none=True) if request else None

    # 发起 HTTP 请求
    async with session.post(
        url, params=params, json=json_data, headers=headers
    ) as response:
        if response.status >= 400:
            error_data = await response.json()
            if response.status == 422:
                error_model = UnprocessableEntityError(**error_data)
                raise ShoplineAPIError(
                    status_code=422,
                    error=error_model,
                    **error_data
                )
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
        return Order(**response_data)