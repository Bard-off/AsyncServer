from datetime import date
import aiofiles as aof
import json
import logging
import common as cm
from file_cls import file

log = logging.getLogger(__name__)

class GetCurrency:
    def __init__(self, cur: str, currencies: list, date_cur=None):
        self.date = date_cur
        if date_cur is None:
            self.date = str(date.today())
        self.cur = cur.lower()
        self.currencies = currencies
        self.api_url = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{date}/v1/currencies/{cur}.json"

    async def send_inf(self):
        if not await file.exist_checker_cur("./data/vals.json", self.cur):
            return {"status": 404, "error": f"{self.cur} doesn't exist in currencies's data"}
        if not cm.check_date(self.date):
            return {"status": 422, "error": f"{self.date} is invalid"}

        checker = await file.checker_to_cur_exist("./data/data.json", self.date, self.cur)
        if checker != False:
            return {"data": checker, "type": "cache"}
        try:
            res = await cm.get_inform("https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{date}/v1/currencies/{cur}.json".format(date=self.date, cur=self.cur))
        except Exception as e:
            return {"status": 404, "error": e}
        new_res = {"date": self.date, f"{self.cur}": {}}
        for cur in self.currencies:
            new_res[self.cur][cur] = res[self.cur][cur]
        try:
            await file.write_to_file("./data/data.json", new_res, self.date)
        except json.decoder.JSONDecodeError:
            await self.send_inf()
        return {"data": json.dumps(new_res), "type": "API"}
