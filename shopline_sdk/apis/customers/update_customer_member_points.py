from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.member_point import MemberPoint
from ...models.not_found_error import NotFoundError
from ...models.server_error import ServerError
from ...models.unauthorized_error import UnauthorizedError
from ...models.unprocessable_entity_error import UnprocessableEntityError

class Request(BaseModel):
    """请求体模型"""
    value: int
    """Points to be added or deducted
      增加或減除點數
      -
      *Number can be -999999~999999"""
    remarks: str
    """Reason for adding or deducting member points
      增加或減除點數原因
      -
      *Limit to max 50 characters"""
    email_target: Optional[int] = None
    """Notification with Email
      是否發送email通知
      Only applicable for addition
      僅適用於增加
      -
       1=NOT_SEND全部不送
       3=SEND_TO_ALL全部都送"""
    sms_notification_target: Optional[int] = None
    """Notification with SMS
      是否發送簡訊通知
      Only applicable for addition
      僅適用於增加
      -
       1=NOT_SEND全部不送
       2=SEND_VERIFIED只送手機驗證過的
       3=SEND_TO_ALL全部都送"""
    performer_id: Optional[str] = None
    """Performer ID
      操作者ID"""
    performer_type: Optional[Literal['User', 'Agent']] = None
    """Performer Type
      操作者類型"""

async def call(
    session: aiohttp.ClientSession, id: str, request: Optional[Request] = None
) -> MemberPoint:
    """
    Update Customer Member Points
    
    Using open API to update customer member points
    
    Path: POST /customers/{id}/member_points
    """
    # 构建请求 URL
    url = f"customers/{id}/member_points"

    # 构建请求头
    headers = {"Content-Type": "application/json"}

    # 构建请求体
    json_data = request.model_dump(exclude_none=True) if request else None

    # 发起 HTTP 请求
    async with session.post(
        url, json=json_data, headers=headers
    ) as response:
        if response.status >= 400:
            error_data = await response.json()
            if response.status == 401:
                error_model = UnauthorizedError(**error_data)
                raise ShoplineAPIError(
                    status_code=401,
                    error=error_model,
                    **error_data
                )
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
        return MemberPoint(**response_data)