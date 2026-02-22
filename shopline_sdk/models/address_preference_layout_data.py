"""Shopline API 数据模型 - AddressPreferenceLayoutData"""

from typing import Optional

from pydantic import BaseModel


class AddressPreferenceLayoutData(BaseModel):
    """Display location of the single address data value 單一地址資料的顯示位置"""
    row: Optional[int] = None
    """The number of row 列"""
    column: Optional[int] = None
    """The number of column 欄"""
    width: Optional[int] = None
    """Width of display 寬度"""
