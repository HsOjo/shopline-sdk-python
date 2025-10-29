from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.customer import Customer
from ...models.paginatable import Paginatable
from ...models.server_error import ServerError
from ...models.unauthorized_error import UnauthorizedError
from ...models.unprocessable_entity_error import UnprocessableEntityError

class Request(BaseModel):
    """查询参数模型"""
    updated_after: Optional[str] = None
    """Filter data by those updated after specific time.
      取得 updated_at 大於指定時間的顧客(包含指定時間)
       *Should use UTC time"""
    updated_before: Optional[str] = None
    """Filter data by those updated before specific time.
      取得 updated_at 小於指定時間的顧客(包含指定時間)
       *Should use UTC time"""
    created_after: Optional[str] = None
    """Filter data by those created after specific time.
      取得 created_at 大於指定時間的顧客(包含指定時間)
       *Should use UTC time"""
    created_before: Optional[str] = None
    """Filter data by those created before specific time.
      取得 created_at 小於指定時間的顧客(包含指定時間)
       *Should use UTC time"""
    page: Optional[int] = None
    """Page Number
      頁數"""
    per_page: Optional[int] = None
    """Numbers of records per Page
      每頁顯示 n 筆資料"""
    sort_by: Optional[Literal['asc', 'desc']] = None
    """Setting sort by created time
      設定創建時間排序"""
    previous_id: Optional[str] = None
    """Customer id before the first record of the target records as pagination cursor
       目標資料的第一個顧客的前一個顧客ID，同作分頁標記。
       * If "previous_id" is provided, this operation will ignore "page" param. 
       * 如果使用param "previous_id"，這次操作會忽略param "page" """
    include_fields: Optional[List[Literal['metafields']]] = None
    """Provide additional attributes in the response
      結果添加哪些參數"""
    fields: Optional[List[str]] = None
    """Only show certain parameters in the response
       This field will have conflicts to the include_fields[]
       To avoid the conflicts
       please also input all the items included in the include_fields[] to this field
       otherwise those fields will not be shown
       結果只顯示哪些參數
       這個欄位會跟include_fields[]的欄位有衝突
       要避免衝突的話，請輸入所有也包括在include_fields[]內的項目
       否則那些項目將不能被顯示"""

class Response(BaseModel):
    """响应体模型"""
    items: Optional[List[Customer]] = None
    pagination: Optional[Paginatable] = None

async def call(
    session: aiohttp.ClientSession, request: Optional[Request] = None
) -> Response:
    """
    Get Customers
    
    To get detailed information of couple customers sorted by time
    利用時間範圍選取與排序獲取數筆顧客資料
    
    Path: GET /customers
    """
    # 构建请求 URL
    url = "customers"

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
        return Response(**response_data)