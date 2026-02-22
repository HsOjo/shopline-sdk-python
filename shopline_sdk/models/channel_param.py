"""Shopline API 数据模型 - channelParam"""

from pydantic import BaseModel
from typing_extensions import Literal


class channelParam(BaseModel):
    """Channel 銷售渠道"""
    value: Literal['all', 'online', 'offline']
    """Enum values: all, online, offline"""
