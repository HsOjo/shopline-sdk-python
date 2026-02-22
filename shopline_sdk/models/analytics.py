"""Shopline API 数据模型 - Analytics"""

from typing import Optional

from pydantic import BaseModel


class Analytics(BaseModel):
    start_date: Optional[str] = None
    """Starting date of the analytics 分析的開始日期"""
    end_date: Optional[str] = None
    """Ending date of the analytics 分析的終結日期"""
