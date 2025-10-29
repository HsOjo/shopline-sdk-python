from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.jobs import Jobs

class Request(BaseModel):
    """查询参数模型"""
    status: Optional[Literal['all', 'pending', 'in_progress', 'done', 'failed', 'timeout']] = None
    """Specify the status for bulk operations
       指定批量操作狀態的過濾"""

async def call(
    session: aiohttp.ClientSession, request: Optional[Request] = None
) -> Jobs:
    """
    Get Bulk Operations
    
    To retrieve bulk operation list
    獲取批量操作
    
    Path: GET /bulk_operations
    """
    # 构建请求 URL
    url = "bulk_operations"

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
            # 默认错误处理
            raise ShoplineAPIError(
                status_code=response.status,
                **error_data
            )
        response_data = await response.json()

        # 验证并返回响应数据
        return Jobs(**response_data)