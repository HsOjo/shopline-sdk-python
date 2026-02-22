"""Shopline API 数据模型 - ShopSetting"""

from typing import Any, List, Optional

from pydantic import BaseModel


class ShopSetting(BaseModel):
    home_page: Optional[str] = None
    page_schedules: Optional[List[Any]] = None
