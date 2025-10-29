from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.event_trackers import EventTrackers
from ...models.server_error import ServerError
from ...models.unauthorized_error import UnauthorizedError
from ...models.unprocessable_entity_error import UnprocessableEntityError

class Request(BaseModel):
    """查询参数模型"""
    event_type: Optional[Literal['loaded_home_page', 'added_product_to_cart', 'loaded_checkout_page', 'placed_an_order', 'loaded_any_page', 'all']] = None
    """Filter event trackers by their event_type.
       Default: all
       按 event_type 過濾事件追踪資料
       預設: all"""
    tracker_types: Optional[List[Literal['tiktok', 'facebook_standard_pixel']]] = None
    """Filter event trackers by their event_keys.
       Default: []
       按 event_key 過濾事件追踪資料
       預設: []"""
    page: Optional[int] = None
    """Page Number
      頁數"""
    per_page: Optional[int] = None
    """Numbers of Orders per Page
      每頁顯示 n 筆資料"""
    version: Optional[str] = None
    """控制 api version"""

async def call(
    session: aiohttp.ClientSession, request: Optional[Request] = None
) -> EventTrackers:
    """
    Get Event Trackers
    
    To get detailed information of event trackers sorted by
     event_type or event_keys
     利用 event_type 或 event_keys 獲取第三方事件追蹤資料
    
    Path: GET /event_trackers
    """
    # 构建请求 URL
    url = "event_trackers"

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
            if response.status == 401:
                error_model = UnauthorizedError(**error_data)
                raise ShoplineAPIError(
                    status_code=401,
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
        return EventTrackers(**response_data)