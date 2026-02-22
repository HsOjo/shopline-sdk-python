"""Shopline API 数据模型 - NetAmountAnalytics"""

from typing import List, Optional

from pydantic import BaseModel

# 导入相关模型
from .money import Money


class MetadataConfig(BaseModel):
    """Configuration model for metadata"""
    total: Optional[Money] = None


class RecordsItem(BaseModel):
    """Item model for records"""
    label: Optional[str] = None
    """Datetime of the data point 時間"""
    value: Optional[Money] = None


class NetAmountAnalytics(BaseModel):
    start_date: Optional[str] = None
    """Starting date of the analytics 分析的開始日期"""
    end_date: Optional[str] = None
    """Ending date of the analytics 分析的終結日期"""
    metadata: Optional[MetadataConfig] = None
    records: Optional[List[RecordsItem]] = None
