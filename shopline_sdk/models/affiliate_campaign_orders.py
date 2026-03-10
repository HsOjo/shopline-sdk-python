"""Shopline API 数据模型 - AffiliateCampaignOrders"""

from typing import List, Optional

from pydantic import BaseModel

from .affiliate_campaign_order import AffiliateCampaignOrder


class AffiliateCampaignOrders(BaseModel):
    items: Optional[List[AffiliateCampaignOrder]] = None
    limit: Optional[int] = None
    """Numbers of Orders"""
    last_id: Optional[str] = None
    """The last ID of the orders"""
