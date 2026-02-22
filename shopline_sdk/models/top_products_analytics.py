"""Shopline API 数据模型 - TopProductsAnalytics"""

from typing import List, Optional

from pydantic import BaseModel

# 导入相关模型
from .paginatable import Paginatable
from .top_products_analytics_record import TopProductsAnalyticsRecord


class TopProductsAnalytics(BaseModel):
    start_date: Optional[str] = None
    """Starting date of the analytics 分析的開始日期"""
    end_date: Optional[str] = None
    """Ending date of the analytics 分析的終結日期"""
    timezone: Optional[int] = None
    """Timezone offset 時區時差"""
    pagination: Optional[Paginatable] = None
    records: Optional[List[TopProductsAnalyticsRecord]] = None
