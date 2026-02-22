"""Shopline API 数据模型 - CustomerViewedCategories"""

from typing import List, Optional

from pydantic import BaseModel

# 导入相关模型
from .customer_viewed_category import CustomerViewedCategory
from .paginatable import Paginatable


class CustomerViewedCategories(BaseModel):
    items: Optional[List[CustomerViewedCategory]] = None
    pagination: Optional[Paginatable] = None
