"""Shopline API 数据模型 - DiscountOption"""

from typing import Optional, Union

from pydantic import BaseModel, Field
from typing_extensions import Literal

from .discount_amount import DiscountAmount
from .title_translations import TitleTranslations


class DiscountOption(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    title_translations: Optional[TitleTranslations] = None
    discount_type: Optional[Union[Literal['amount', 'percentage'], str]] = None
    discount_amount: Optional[DiscountAmount] = None
    discount_percentage: Optional[float] = None
    merchant_id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
