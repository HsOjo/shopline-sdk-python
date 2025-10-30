from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.not_found_error import NotFoundError
from ...models.order_delivery import OrderDelivery
from ...models.server_error import ServerError
from ...models.unprocessable_entity_error import UnprocessableEntityError

class Params(BaseModel):
    """查询参数模型"""
    include_fields: Optional[List[Union[Literal['affiliate_campaign'], str]]] = None
    """Provide additional attributes in the response
      結果添加哪些參數"""
    fields: Optional[List[str]] = None
    """Only return the provided fields in the responses
      結果只包含輸入的參數
       This parameter will override include_fields[]
      此參數會覆蓋include_fields[]。"""

class Body(BaseModel):
    """请求体模型"""
    status: Optional[Union[Literal['pending', 'shipping', 'shipped', 'arrived', 'collected', 'returned', 'returning'], str]] = None
    mail_notify: Optional[bool] = None
    """Do you want to notify the customer via email with the change?
      此更新是否要以email通知顧客？
      (Default: false)"""
    force_update: Optional[Union[Literal['status'], str]] = None
    """To force update delivery status for third party delivery providers
       強制更新第三方物流服務供應商訂單運送狀態"""

class Response(BaseModel):
    """响应体模型"""
    order_id: Optional[str] = None
    status: Optional[Union[Literal['pending', 'shipping', 'shipped', 'arrived', 'collected', 'returned', 'returning'], str]] = None
    updated_at: Optional[str] = None

async def call(
    session: aiohttp.ClientSession, id: str, params: Optional[Params] = None, body: Optional[Body] = None
) -> Response:
    """
    Update Order Delivery Status
    
    To update order's delivery status
    更新訂單運送狀態
    
    Path: PATCH /orders/{id}/order_delivery_status
    """
    # 构建请求 URL
    url = f"orders/{id}/order_delivery_status"

    # 构建查询参数
    query_params = {}
    if params:
        params_dict = params.model_dump(exclude_none=True)
        for key, value in params_dict.items():
            if value is not None:
                query_params[key] = value

    # 构建请求头
    headers = {"Content-Type": "application/json"}

    # 构建请求体
    json_data = body.model_dump(exclude_none=True) if body else None

    # 发起 HTTP 请求
    async with session.patch(
        url, params=query_params, json=json_data, headers=headers
    ) as response:
        if response.status >= 400:
            error_data = await response.json()
            if response.status == 404:
                error_model = NotFoundError(**error_data)
                raise ShoplineAPIError(
                    status_code=404,
                    error=error_model
                )
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