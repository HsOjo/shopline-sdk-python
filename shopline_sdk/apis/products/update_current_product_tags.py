from typing import Any, Dict, List, Optional, Union
import aiohttp
from pydantic import BaseModel, ValidationError, Field
from typing_extensions import Literal

# 导入异常类
from ...exceptions import ShoplineAPIError

# 导入需要的模型
from ...models.server_error import ServerError
from ...models.unprocessable_entity_error import UnprocessableEntityError

class Body(BaseModel):
    """请求体模型"""
    update_mode: Union[Literal['add', 'remove'], str]
    """Update mode of this opearation, allow "add" or "remove"
       更新商品標簽的方式，可選"add"或"remove"。"""
    tags: List[str]
    """Product tags array 
       商品標簽array"""

class Response(BaseModel):
    """响应体模型"""
    tags: Optional[List[str]] = None

async def call(
    session: aiohttp.ClientSession, productId: str, body: Optional[Body] = None
) -> Response:
    """
    Update (add/remove) current product tags
    
    Add or Remove current product tags with input tags array. 
     Each tag mush have at least 3 characters and at most 40 characters.
     When update with invalid length of tags, the update will fail and the respond will be 422.
     Must pass at least one tag, otherwise the update will fail and the respond will be 422.
     在現有的商品標簽新增/移除標簽。
     每一個商品標籤必須有最少3個字完及最多40個字完。
     若需更新的商品標籤其中之一不符字完長度規範，更新不會成功及將回傳狀態碼422。
     必須最少新增/移除一個標籤，否則更新不會成功及將回傳狀態碼422。
    
    Path: PATCH /products/{productId}/tags
    """
    # 构建请求 URL
    url = f"products/{productId}/tags"

    # 构建请求头
    headers = {"Content-Type": "application/json"}

    # 构建请求体
    json_data = body.model_dump(exclude_none=True) if body else None

    # 发起 HTTP 请求
    async with session.patch(
        url, json=json_data, headers=headers
    ) as response:
        if response.status >= 400:
            error_data = await response.json()
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
        return Response(**response_data)