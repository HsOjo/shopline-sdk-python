from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.not_found_error import NotFoundError
from ...models.order_payment import OrderPayment
from ...models.server_error import ServerError
from ...models.unprocessable_entity_error import UnprocessableEntityError

class Request(BaseModel):
    """请求体模型"""
    status: Optional[Literal['pending', 'failed', 'expired', 'completed', 'refunding', 'refunded']] = None
    mail_notify: Optional[bool] = None
    """Do you want to notify the customer via email with the change?
      此更新是否要以email通知顧客？
      (Default: false)"""

class Response(BaseModel):
    """响应体模型"""
    order_id: Optional[str] = None
    status: Optional[Literal['pending', 'failed', 'expired', 'completed', 'refunding', 'refunded']] = None
    updated_at: Optional[str] = None

async def call(
    session: aiohttp.ClientSession, id: str, request: Optional[Request] = None
) -> Response:
    """
    Update Order Payment Status
    
    To update order's payment status
    更新訂單付款狀態
    
    Path: PATCH /orders/{id}/order_payment_status
    """
    # 构建请求 URL
    url = f"orders/{id}/order_payment_status"

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
    async with session.patch(
        url, params=params, json=json_data, headers=headers
    ) as response:
        if response.status >= 400:
            error_data = await response.json()
            if response.status == 404:
                error_model = NotFoundError(**error_data)
                raise ShoplineAPIError(
                    status_code=404,
                    error=error_model,
                    **error_data
                )
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
        return Response(**response_data)