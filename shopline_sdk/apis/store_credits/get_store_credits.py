from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.paginatable import Paginatable
from ...models.store_credit import StoreCredit

class Request(BaseModel):
    """查询参数模型"""
    created_at_after: Optional[str] = None
    """Filter store credits by those created after specific time.
       取得 created_at 大於指定時間的購物金(包含指定時間)
       *Should use UTC time'"""
    created_at_before: Optional[str] = None
    """Filter store credits by those create before specific time.
       取得 created_at 小於指定時間的購物金(包含指定時間)
       *Should use UTC time'"""
    end_at_after: Optional[str] = None
    """Filter store credits by those end after specific time.
       取得 end_at 大於指定時間的購物金(包含指定時間)
       *Should use UTC time'"""
    end_at_before: Optional[str] = None
    """Filter store credits by those end before specific time.
       取得 end_at 小於指定時間的購物金(包含指定時間)
       *Should use UTC time'"""
    page: Optional[int] = None
    """Page Number
      頁數"""
    per_page: Optional[int] = None
    """Numbers of Orders per Page
      每頁顯示 n 筆資料"""
    excludes: Optional[List[str]] = None
    """Could exclude certain parameters in the response
      結果要排除哪些參數"""
    fields: Optional[List[str]] = None
    """Could only show certain parameters in the response
      結果只顯示哪些參數"""

class Response(BaseModel):
    """响应体模型"""
    items: Optional[List[StoreCredit]] = None
    pagination: Optional[Paginatable] = None

async def call(
    session: aiohttp.ClientSession, request: Optional[Request] = None
) -> Response:
    """
    Get Store Credits
    
    To get customers store credits
    獲取商店購物金紀錄
    
    Path: GET /user_credits
    """
    # 构建请求 URL
    url = "user_credits"

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
            raise ShoplineAPIError(
                status_code=response.status,
                **error_data
            )
        response_data = await response.json()

        # 验证并返回响应数据
        return Response(**response_data)