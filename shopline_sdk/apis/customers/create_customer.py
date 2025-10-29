from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.customer import Customer
from ...models.server_error import ServerError
from ...models.unauthorized_error import UnauthorizedError
from ...models.unprocessable_entity_error import UnprocessableEntityError

class Request(BaseModel):
    """查询参数模型"""
    excludes: Optional[List[str]] = None
    """Exclude certain parameters in the response
      結果要排除哪些參數"""
    fields: Optional[List[str]] = None
    """Only show certain parameters in the response
       結果只顯示哪些參數"""

async def call(
    session: aiohttp.ClientSession, request: Optional[Request] = None
) -> Customer:
    """
    Create Customer
    
    To create a customer with open API
    透過open API創建一筆新的顧客資料
    
    Path: POST /customers
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

    # 构建请求体
    json_data = request.model_dump(exclude_none=True) if request else None

    # 发起 HTTP 请求
    async with session.post(
        url, params=params, json=json_data, headers=headers
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
        return Customer(**response_data)