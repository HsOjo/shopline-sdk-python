from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.channels import Channels
from ...models.server_error import ServerError

class Request(BaseModel):
    """查询参数模型"""
    belongs_to: Optional[Literal['staff', 'merchant']] = None
    """Channels belongs to staff or merchant. Default is staff
      網店通路或是 Staff 的通路，預設為 staff"""
    platform: Optional[Literal['Shopee', 'shop_crm', 'online', 'pos', 'sc']] = None
    """Filter channels by platform. It can only filter channel by sc or shop_crm if belogs_to is staff.
       過濾通路屬於哪個平台，如果 belongs_to 為 staff 則只能過濾 sc 或是 shop_crm 通路。"""
    platforms: Optional[List[Literal['Shopee', 'shop_crm', 'online', 'pos', 'sc']]] = None
    """Filter multiple channels by platforms. It can only filter channel by sc or shop_crm if belogs_to is staff.
       過濾通路屬於哪些平台，如果 belongs_to 為 staff 則只能過濾 sc 或是 shop_crm 通路。"""
    include_fields: Optional[List[Literal['e_invoice_setting', 'pin_codes']]] = None
    """Some fields need to be specified in this parameter. Otherwise, it will not be returned.
       有些欄位需要定義在此參數內，否則將不會返回這些欄位的值。"""
    fields: Optional[List[Literal['items.mobile_logo_media_url']]] = None
    """For mobile logo media, need to add items.mobile_logo_media_url to this field.
       mobile logo media 必須加入 items.mobile_logo_media_url 到此欄位。"""
    page: Optional[int] = None
    """Page number
      頁數"""
    per_page: Optional[int] = None
    """Numbers of channels per page
      每頁顯示資料筆數"""

async def call(
    session: aiohttp.ClientSession, request: Optional[Request] = None
) -> Channels:
    """
    Get Channels
    
    Get Channels
    獲取 Channel 列表
    
    Path: GET /channels
    """
    # 构建请求 URL
    url = "channels"

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
        return Channels(**response_data)