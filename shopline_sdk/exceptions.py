"""
Shopline SDK 异常类
"""

from typing import Any, Optional
from pydantic import BaseModel


class ShoplineAPIError(Exception):
    """Shopline API 错误异常"""
    
    def __init__(
        self, 
        code: str = "UNKNOWN", 
        message: str = "Unknown error", 
        status_code: int = 500,
        error: Optional[BaseModel] = None,
        **kwargs
    ):
        """
        初始化 Shopline API 错误
        
        Args:
            code: 错误代码
            message: 错误消息
            status_code: HTTP 状态码
            error: 错误响应模型实例
            **kwargs: 其他错误数据
        """
        self.code = code
        self.message = message
        self.status_code = status_code
        self.error = error
        
        # 存储额外的错误数据
        for key, value in kwargs.items():
            setattr(self, key, value)
        
        super().__init__(f"[{code}] {message}")
    
    def __str__(self) -> str:
        return f"ShoplineAPIError({self.status_code}): [{self.code}] {self.message}"
    
    def __repr__(self) -> str:
        return (
            f"ShoplineAPIError(code='{self.code}', message='{self.message}', "
            f"status_code={self.status_code}, error={self.error})"
        )
