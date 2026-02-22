"""Shopline API 数据模型 - TaxSetting"""

from typing import Optional

from pydantic import BaseModel


class TaxSetting(BaseModel):
    products_taxable: Optional[bool] = None
    """All Shops need Tax Collection 全店皆需收稅"""
