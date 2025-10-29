from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.customer_group import CustomerGroup
from ...models.paginatable import Paginatable
from ...models.server_error import ServerError
from ...models.unprocessable_entity_error import UnprocessableEntityError

class Request(BaseModel):
    """查询参数模型"""
    page: Optional[int] = None
    """Page
      頁數
      (Default: 1)"""
    per_page: Optional[int] = None
    """Numbers of Customers per page
      每頁顯示 n 筆資料
      (Default: 24, Max: 999)"""
    sort_by: Optional[str] = None
    """Setting sort by created time
      設定依照建立時間排序
      (Default: desc)"""
    created_after: Optional[str] = None
    """Filter customers which is later than created_after
      篩選依據 created_after 時間之後建立的分群
      -
       Please fill in to the second level. Default value is 00:00:00 if only fill in dates.
      請輸入至秒數，若只輸入日期，則會自動帶入當天00:00:00"""
    created_before: Optional[str] = None
    """Filter customers which is earlier than created_before
      篩選依據 created_before 時間之前建立的分群
      -
       Please fill in to the second level. Default value is 00:00:00 if only fill in dates.
      請輸入至秒數，若只輸入日期，則會自動帶入當天00:00:00"""
    status: Optional[Literal['active', 'expired']] = None
    """Filter the customer group is active or expired.
       篩選已過期或未過期的顧客分群
      -
       If the value isn't given, it will return all customer groups.
      若不填寫，則會回傳所有顧客分群
       Don't use created_before or created_after if the status is given.
       若有設定 status 欄位，則不要同時設定 created_before 或 created_before 參數"""

class Response(BaseModel):
    """响应体模型"""
    items: Optional[List[CustomerGroup]] = None
    pagination: Optional[Paginatable] = None

async def call(
    session: aiohttp.ClientSession, request: Optional[Request] = None
) -> Response:
    """
    Get Customer Groups
    
    To get customer groups.
    獲取顧客分群。
    
    Path: GET /customer_groups
    """
    # 构建请求 URL
    url = "customer_groups"

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