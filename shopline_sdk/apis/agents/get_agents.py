from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.agent import Agent
from ...models.paginatable import Paginatable

class Params(BaseModel):
    """查询参数模型"""
    page: Optional[int] = None
    """Page Number
      頁數"""
    per_page: Optional[int] = None
    """Numbers of Orders per Page
      每頁顯示 n 筆資料"""
    sort_by: Optional[Literal['asc', 'desc']] = None
    """Setting sorting direction
      設定時間排序"""
    excludes: Optional[List[str]] = None
    """Could exclude certain parameters in the response
      結果要排除哪些參數"""
    fields: Optional[List[str]] = None
    """Could only show certain parameters in the response
      結果只顯示哪些參數"""
    channel_ids: Optional[List[str]] = None
    """Show agents include one of channel_ids, length limit is 10
      結果只顯示哪些員工，長度限制10個"""

class Response(BaseModel):
    """响应体模型"""
    items: Optional[List[Agent]] = None
    pagination: Optional[Paginatable] = None

async def call(
    session: aiohttp.ClientSession, params: Optional[Params] = None
) -> Response:
    """
    Get Agents
    
    To get all agents with open API
    透過open API獲取 Agents
    
    Path: GET /agents
    """
    # 构建请求 URL
    url = "agents"

    # 构建查询参数
    query_params = {}
    if params:
        params_dict = params.model_dump(exclude_none=True)
        for key, value in params_dict.items():
            if value is not None:
                query_params[key] = value

    # 构建请求头
    headers = {"Content-Type": "application/json"}

    # 发起 HTTP 请求
    async with session.get(
        url, params=query_params, headers=headers
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