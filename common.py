import urllib
import urllib.parse
import aiohttp as ao
import datetime

def make_url(base, router):
    return urllib.parse.urljoin(base, router)

async def get_inform(url: str):
    async with ao.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

def check_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False