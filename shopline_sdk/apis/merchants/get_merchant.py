from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.merchant import Merchant

class Request(BaseModel):
    """查询参数模型"""
    include_fields: Optional[List[Literal['current_theme_key', 'instagram_username', 'admin_status']]] = None
    """Provide additional attributes in the response
      結果添加哪些參數"""

async def call(
    session: aiohttp.ClientSession, merchant_id: str, request: Optional[Request] = None
) -> Merchant:
    """
    Get Merchant
    
    To get information of merchant by merchant id
    以商户id獲取商户資料
    
    Path: GET /merchants/{merchant_id}
    """
    # 构建请求 URL
    url = f"merchants/{merchant_id}"

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
        return Merchant(**response_data)