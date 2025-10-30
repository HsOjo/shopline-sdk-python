from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.addon_product import AddonProduct
from ...models.forbidden_error import ForbiddenError
from ...models.not_found_error import NotFoundError
from ...models.server_error import ServerError
from ...models.unprocessable_entity_error import UnprocessableEntityError

class Body(BaseModel):
    """请求体模型"""
    quantity: float
    """Quantity
      (新增/減少)加購品數量
      -
       *if replace sets as false, allows quantity to be negative number
       如果 replace 為 false，准許 quantity 為負數"""
    replace: Optional[bool] = None
    """Whether replacing the original quantity
      是否取代原本數量
       - 
       true: replace the product's quantity with the number you provided
      取代原本數量
      
       false: increase/decrease the quantity with the number you provided
      增加/減少數量"""

async def call(
    session: aiohttp.ClientSession, id: str, body: Optional[Body] = None
) -> AddonProduct:
    """
    Update Addon Product Quantity
    
    To update quantity of add-on products with open API
    透過open API 更新加購品數量
    
    Path: PUT /addon_products/{id}/update_quantity
    """
    # 构建请求 URL
    url = f"addon_products/{id}/update_quantity"

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
            if response.status == 403:
                error_model = ForbiddenError(**error_data)
                raise ShoplineAPIError(
                    status_code=403,
                    error=error_model
                )
            if response.status == 404:
                error_model = NotFoundError(**error_data)
                raise ShoplineAPIError(
                    status_code=404,
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
        return AddonProduct(**response_data)