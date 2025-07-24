from aiohttp import web
from config import configure_logging, to_currencies
from getter_currency import GetCurrency
import logging

routes = web.RouteTableDef()

log = logging.getLogger(__name__)

@routes.get("/currency/{currency}")
@routes.get("/currency/{currency}/{date}")
async def get_cur(request: web.Request):
    cur = request.match_info.get("currency")
    date = request.match_info.get("date")
    log.info(f"Start getting {cur}")
    getter_cur = GetCurrency(cur, to_currencies, date)
    result = await getter_cur.send_inf()
    log.info(f"Got {cur}")
    return web.json_response(data=result)

app = web.Application()
app.add_routes(routes)

def main():
    configure_logging()
    web.run_app(app)

if __name__ == "__main__":
    main()
