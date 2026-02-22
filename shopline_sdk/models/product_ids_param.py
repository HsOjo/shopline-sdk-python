"""Shopline API 数据模型 - productIdsParam"""

from pydantic import BaseModel


class productIdsParam(BaseModel):
    """Comma-separated product IDs for the query 用於查詢的逗號分隔產品 ID"""
    pass
