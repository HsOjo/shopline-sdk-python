import asyncio
import os

from shopline_sdk.apis.customers import get_customers
from shopline_sdk.client import ShoplineAPIClient


async def test_get_customers():
    client = ShoplineAPIClient(os.getenv('SHOPLINE_ACCESS_TOKEN'))
    async with client.new_session() as session:
        resp = await get_customers.call(session, get_customers.Request())
    print(resp.items)


asyncio.run(test_get_customers())
