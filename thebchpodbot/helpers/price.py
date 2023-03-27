from pycoingecko import CoinGeckoAPI
import json
from babel.numbers import format_currency

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


def get_fiat_value(currencies: list[str] | str | None = None) -> str:
    if not currencies:
        currencies = "usd"
    price = cg.get_price(
        "bitcoin-cash",
        currencies,
        include_market_cap=True,
        include_24hr_vol=True,
        include_24hr_change=True,
    )
    price = price["bitcoin-cash"]
    for k, v in price.items():
        currency = k.split("_")[0]
        if k.endswith("change"):
            price[k] = format_percent(v)
        if k.endswith("cap") or k.endswith("vol"):
            if currency.lower() not in unsupported_to_format:
                price[k] = format_currency(v, currency.upper(), "¤ #,##0.00")
    price = json.dumps(price, indent=1, ensure_ascii=False).replace("{\n", "").replace("}", "").replace(' "', '"')
    return price


def format_percent(value) -> str:
    value /= 100.0
    return "{:.2%}".format(value)
