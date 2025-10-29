from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.stock import Stock
from ...models.translatable import Translatable

class Request(BaseModel):
    """查询参数模型"""
    excludes: Optional[List[str]] = None
    """Could exclude certain parameters in the response
      結果要排除哪些參數"""
    fields: Optional[List[str]] = None
    """Could only show certain parameters in the response
      結果只顯示哪些參數"""

class Response(BaseModel):
    """响应体模型"""
    id: Optional[str] = None
    title_translations: Optional[Translatable] = None
    stocks: Optional[List[Stock]] = None

async def call(
    session: aiohttp.ClientSession, id: str, request: Optional[Request] = None
) -> Response:
    """
    Get Product Stocks
    
    To get stock information for a specific product with its ID
     使用商品 ID 獲取特定一個商品的庫存資料
    
    Path: GET /products/{id}/stocks
    """
    # 构建请求 URL
    url = f"products/{id}/stocks"

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