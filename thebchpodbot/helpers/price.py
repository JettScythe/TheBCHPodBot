from pycoingecko import CoinGeckoAPI
from typing import List, Optional, Union, Dict
import json

cg = CoinGeckoAPI()
supported_currencies = cg.get_supported_vs_currencies()

def get_fiat_value(currencies: Optional[Union[List[str], str]] = None) -> Dict:
    if not currencies:
        currencies = 'usd'
    price = cg.get_price('bitcoin-cash', currencies, include_market_cap=True, include_24hr_vol=True, include_24hr_change=True)
    price = price["bitcoin-cash"]
    """
    # This works for most fiat, but not crypto pairs
    for k, v in price.items():
        currency = k.split("_")[0]
        if k.endswith("vol") or k.endswith("cap"):
            price[k] = format_currency(v, currency.upper()) """
    price = json.dumps(price, indent=2)
    return price
