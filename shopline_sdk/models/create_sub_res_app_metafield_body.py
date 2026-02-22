"""Shopline API 数据模型 - CreateSubResAppMetafieldBody"""

from typing import Any, Dict, Optional, Union

from pydantic import BaseModel
from typing_extensions import Literal


class CreateSubResAppMetafieldBody(BaseModel):
    """Payload for creating app metafield"""
    key: Optional[str] = None
    """Key"""
    field_type: Optional[Union[Literal[
        'single_line_text_field', 'multi_line_text_field', 'number_integer', 'number_decimal', 'json', 'boolean', 'url'], str]] = None
    """Data type of the metafield value  Type allows:  single_line_text_field - One line of string (max 50 characters)  multi_line_text_field - Multiple line of string (max 1000 characters)  number_integer - Integer  number_decimal - Decimal  json - String of JSON object (max 4000 characters)  boolean - Boolean  url - String of URL"""
    field_value: Optional[Union[str, float, bool, Dict[str, Any]]] = None
    """Metafield value"""
    resource_id: Optional[str] = None
    """Resource ID"""
