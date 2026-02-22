"""Shopline API 数据模型 - AppSetting"""

from typing import Any, Dict, Optional

from pydantic import BaseModel


class AppSetting(BaseModel):
    appName: Optional[Dict[str, Any]] = None
