"""Shopline API 数据模型 - LockInventory"""

from typing import List, Optional

from pydantic import BaseModel


class LockInventory(BaseModel):
    items: Optional[List['LockInventory']] = None
