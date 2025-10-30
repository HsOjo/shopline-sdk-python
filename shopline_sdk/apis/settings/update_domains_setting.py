from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.bad_request_error import BadRequestError
from ...models.domains_setting import DomainsSetting
from ...models.server_error import ServerError
from ...models.unauthorized_error import UnauthorizedError
from ...models.unprocessable_entity_error import UnprocessableEntityError


class Webmasters(BaseModel):
    """Model for webmasters"""
    google: Optional[str] = None
    """Google Search Console verification code"""
    bing: Optional[str] = None
    """Bing Webmaster Tools verification code"""
    facebook_domain_verification: Optional[str] = None
    """Facebook domain verification code"""
    pinterest_domain_verification: Optional[str] = None
    """Pinterest domain verification code"""
    google_merchant_center: Optional[str] = None
    """Google Merchant Center verification code"""
    google_merchant_id: Optional[str] = None
    """Google Merchant Center ID"""

class Body(BaseModel):
    """请求体模型"""
    webmasters: Webmasters

async def call(
    session: aiohttp.ClientSession, body: Body
) -> DomainsSetting:
    """
    Update Domains Setting
    
    To update domain verification settings
    including Google, Bing, Facebook, Pinterest, and Google Merchant Center
    
    更新第三方網域工具設定，包括 Google、Bing、Facebook、Pinterest 和 Google Merchant Center
    
    
    Path: PUT /settings/domains
    """
    # 构建请求 URL
    url = "settings/domains"

    # 构建请求头
    headers = {"Content-Type": "application/json"}

    # 构建请求体
    json_data = body.model_dump(exclude_none=True) if body else None

    # 发起 HTTP 请求
    async with session.put(
        url, json=json_data, headers=headers
    ) as response:
        if response.status >= 400:
            error_data = await response.json()
            if response.status == 400:
                error_model = BadRequestError(**error_data)
                raise ShoplineAPIError(
                    status_code=400,
                    error=error_model
                )
            if response.status == 401:
                error_model = UnauthorizedError(**error_data)
                raise ShoplineAPIError(
                    status_code=401,
                    error=error_model
                )
            if response.status == 422:
                error_model = UnprocessableEntityError(**error_data)
                raise ShoplineAPIError(
                    status_code=422,
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
        return DomainsSetting(**response_data)