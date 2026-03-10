"""Shopline API 数据模型 - CustomerViewedProducts"""

from typing import List, Optional

from pydantic import BaseModel

from .customer_viewed_product import CustomerViewedProduct
from .paginatable import Paginatable


class CustomerViewedProducts(BaseModel):
    items: Optional[List[CustomerViewedProduct]] = None
    pagination: Optional[Paginatable] = None
