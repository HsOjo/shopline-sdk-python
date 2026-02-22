"""Shopline API 数据模型 - retail_status"""

from pydantic import BaseModel
from typing_extensions import Literal


class retail_status(BaseModel):
    """The status that will be applied on the products to the retail store.  更新商品狀態至實體店。"""
    value: Literal['active', 'draft']
    """Enum values: active, draft"""
