import asyncio as aso
import logging

import common as cm
from config import configure_logging, my_url

log = logging.getLogger(__name__)

async def getting_infor():
    log.info("Start getting information")
    async with aso.TaskGroup() as tg:
        res = tg.create_task(cm.get_inform(cm.make_url(my_url, "/currency/ttd")))
        res1 = tg.create_task(cm.get_inform(cm.make_url(my_url, "/currency/rub/2025-06-25")))
        res2 = tg.create_task(cm.get_inform(cm.make_url(my_url, "/currency/eur/2025-06-25")))
        res3 = tg.create_task(cm.get_inform(cm.make_url(my_url, "/currency/rub/2025-25-23")))

        res4 = tg.create_task(cm.get_inform(cm.make_url(my_url, "/currency/usd/2025-06-25")))
        res5 = tg.create_task(cm.get_inform(cm.make_url(my_url, "/currency/gbp/2025-06-25")))
        res6 = tg.create_task(cm.get_inform(cm.make_url(my_url, "/currency/cad/2025-06-25")))
        res7 = tg.create_task(cm.get_inform(cm.make_url(my_url, "/currency/aud/2025-06-25")))
        res8 = tg.create_task(cm.get_inform(cm.make_url(my_url, "/currency/jpy/2025-06-25")))
        res9 = tg.create_task(cm.get_inform(cm.make_url(my_url, "/currency/chf/2025-06-25")))
        res10 = tg.create_task(cm.get_inform(cm.make_url(my_url, "/currency/cnh/2025-06-25")))
        res11 = tg.create_task(cm.get_inform(cm.make_url(my_url, "/currency/inr/2025-06-25")))
        res12 = tg.create_task(cm.get_inform(cm.make_url(my_url, "/currency/mxn/2025-06-25")))
        res13 = tg.create_task(cm.get_inform(cm.make_url(my_url, "/currency/sek/2025-06-25")))
        res14 = tg.create_task(cm.get_inform(cm.make_url(my_url, "/currency/nzd/2025-06-25")))
        res15 = tg.create_task(cm.get_inform(cm.make_url(my_url, "/currency/zar/2025-06-25")))
        res16 = tg.create_task(cm.get_inform(cm.make_url(my_url, "/currency/try/2025-06-25")))
        res17 = tg.create_task(cm.get_inform(cm.make_url(my_url, "/currency/krw/2025-06-25")))
        res18 = tg.create_task(cm.get_inform(cm.make_url(my_url, "/currency/brl/2025-06-25")))

    log.info("Got information")
    log.info(res.result())
    log.info(res1.result())
    log.info(res2.result())
    log.info(res3.result())
    log.info(res4.result())
    log.info(res5.result())
    log.info(res6.result())
    log.info(res7.result())
    log.info(res8.result())
    log.info(res9.result())
    log.info(res10.result())
    log.info(res11.result())
    log.info(res12.result())
    log.info(res13.result())
    log.info(res14.result())
    log.info(res15.result())
    log.info(res16.result())
    log.info(res17.result())
    log.info(res18.result())


async def main():
    configure_logging()
    await getting_infor()

if __name__ == "__main__":
    aso.run(main())

