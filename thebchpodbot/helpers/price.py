from pycoingecko import CoinGeckoAPI
import json
from babel.numbers import format_currency
import time

cg = CoinGeckoAPI()
supported_currencies = cg.get_supported_vs_currencies()
unsupported_to_format = [
    "btc",
    "eth",
    "ltc",
    "bch",
    "bnb",
    "eos",
    "xrp",
    "xlm",
    "link",
    "dot",
    "yfi",
    "bits",
    "sats",
    "xau",
    "xdr",
    "xag",
]

price_cache = {}


def refresh_price_cache():
    price = cg.get_price(
        "bitcoin-cash",
        supported_currencies,
        include_market_cap=True,
        include_24hr_vol=True,
        include_24hr_change=True,
    )["bitcoin-cash"]
    for k, v in price.items():
        currency = k.split("_")[0]
        if currency not in price_cache:
            price_cache[currency] = {"price": {}, "timestamp": time.time()}
        if k.endswith("change"):
            price_cache[currency]["price"][k] = format_percent(v)
        elif k.endswith(("cap", "vol")) and currency.lower() not in unsupported_to_format:
            price_cache[currency]["price"][k] = format_currency(v, currency.upper(), "¤ #,##0.00")
        else:
            price_cache[currency]["price"][k] = v


def get_fiat_value(currencies: list[str] = supported_currencies) -> str:
    if "usd" not in price_cache or time.time() - price_cache["usd"]["timestamp"] <= 240:
        refresh_price_cache()
    to_ret = ""
    for currency in currencies:
        to_ret += json.dumps(price_cache[currency]["price"], indent=1, ensure_ascii=False).replace("{\n", "").replace("}", "").replace(' "', '"')
    return to_ret


def format_percent(value) -> str:
    value /= 100.0
    return "{:.2%}".format(value)
