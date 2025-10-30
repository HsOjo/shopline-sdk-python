from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.payment import Payment

class Params(BaseModel):
    """查询参数模型"""
    excludes: Optional[List[str]] = None
    """Could exclude certain parameters in the response
      結果要排除哪些參數"""
    fields: Optional[List[str]] = None
    """Could only show certain parameters in the response
      結果只顯示哪些參數"""

async def call(
    session: aiohttp.ClientSession, id: str, params: Optional[Params] = None
) -> Payment:
    """
    Get Payment
    
    To get payment method information by inputing payment method ID
    輸入付款方式ID取得該付款方式資訊
    
    Path: GET /payments/{id}
    """
    # 构建请求 URL
    url = f"payments/{id}"

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
        return Payment(**response_data)