"""Shopline API 数据模型 - CreateMetafieldDefinitionBody"""

from typing import Optional, Union

from pydantic import BaseModel
from typing_extensions import Literal


class CreateMetafieldDefinitionBody(BaseModel):
    """Payload for creating metafield definition"""
    namespace: Optional[str] = None
    """Namespace"""
    key: Optional[str] = None
    """Key"""
    name: Optional[str] = None
    """Name"""
    description: Optional[str] = None
    """description"""
    field_type: Optional[Union[Literal[
        'single_line_text_field', 'multi_line_text_field', 'number_integer', 'number_decimal', 'json', 'boolean', 'url'], str]] = None
    """Data type of the metafield value  Type allows:  single_line_text_field - One line of string (max 50 characters)  multi_line_text_field - Multiple line of string (max 1000 characters)  number_integer - Integer  number_decimal - Decimal  json - String of JSON object (max 4000 characters)  boolean - Boolean  url - String of URL"""
