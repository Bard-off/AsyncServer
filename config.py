import logging

log = logging.getLogger(__name__)

my_url = "http://127.0.0.1:8080/"

to_currencies = ["rub", "eur", "usd", "ttd"]

def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)s - %(message)s"
    )
