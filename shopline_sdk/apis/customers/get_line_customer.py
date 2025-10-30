from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.customer import Customer
from ...models.not_found_error import NotFoundError
from ...models.server_error import ServerError
from ...models.unauthorized_error import UnauthorizedError

async def call(
    session: aiohttp.ClientSession, lineId: str
) -> Customer:
    """
    Get Line Customer
    
    To get detailed information for a specific customer with its Line ID
    使用顧客用來註冊的Line ID獲取特定一個顧客的詳細資料
    
    Path: GET /customers/line/{lineId}
    """
    # 构建请求 URL
    url = f"customers/line/{lineId}"

    # 构建请求头
    headers = {"Content-Type": "application/json"}

    # 发起 HTTP 请求
    async with session.get(
        url, headers=headers
    ) as response:
        if response.status >= 400:
            error_data = await response.json()
            if response.status == 401:
                error_model = UnauthorizedError(**error_data)
                raise ShoplineAPIError(
                    status_code=401,
                    error=error_model
                )
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
        return Customer(**response_data)