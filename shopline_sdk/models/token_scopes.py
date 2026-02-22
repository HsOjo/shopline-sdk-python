"""Shopline API 数据模型 - TokenScopes"""

from typing import Any, Dict, Optional

from pydantic import BaseModel


class TokenScopes(BaseModel):
    scopes: Optional[Dict[str, Dict[str, Any]]] = None
    """All scopes available"""
