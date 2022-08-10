import requests
import json
import math

import config
from currencies import Currencies
from utils import round_up


class PriceConverter:
    def __init__(self) -> None:
        self.currencies = [currency for currency in Currencies]
        self._url = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from=USD&amount={amount}"
        self._headers= {
            "apikey": config.api_key
        }

    def convert_USD(self, usd_amt: str, currency: Currencies) -> str:
        converted_amount = 0
        if currency in self.currencies:
            converted_amount = self._convert(usd_amt, currency)
        else:
            converted_amount = usd_amt
        round_amt = self._roundUp(converted_amount)
        return currency.value.format(amount=round_amt)

    def _convert(self, usd_amt: str, currency: Currencies) -> str:
        url = self._url.format(to=currency.name, amount=usd_amt)
        response = requests.request("GET", url, headers=self._headers, verify=False)
        status_code = response.status_code
        amt = usd_amt
        if status_code == 200:
            result = json.loads(response.text)
            amt = result["result"]
        return amt

    def _roundUp(self, amt: str) -> str:
        round_amt = amt
        if amt < 1000:
            round_amt = math.ceil(amt)
            round_amt -= 0.01
        elif amt < 10000:
            round_amt = round_up(amt, -1)
        else:
            round_amt = round_up(amt, -2)
        return round_amt

