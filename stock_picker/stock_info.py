import os
from abc import ABC, abstractmethod

import requests


class StockInfo:
    def __init__(self, symbol):
        self.symbol = symbol


class Quote(StockInfo):
    def __init__(self, price, **kwargs):
        super().__init__(**kwargs)
        self.price = price

    def __repr__(self):
        return f"{self.__class__.__name__}(symbol={self.symbol}, price={self.price})"


class StockInfoGetter(ABC):
    @abstractmethod
    def update_info(stock_infos):
        """Updates given StockInfo objects"""

    @abstractmethod
    def get_info(symbols):
        """Creates StockInfo objects from given symbols."""

    @abstractmethod
    def _process_response(response):
        """Process JSON response. Used by get_info."""


class QuoteGetter(StockInfoGetter):

    endpoint = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"
    headers = {"x-rapidapi-host": "apidojo-yahoo-finance-v1.p.rapidapi.com"}

    def __init__(self, api_key, params):
        self.headers = self.headers.copy()
        self.headers["x-rapidapi-key"] = api_key
        self.params = params

    def update_info(self, quotes):
        """Given Quote objects, update their price."""
        response = requests.get(
            url=self.endpoint, headers=self.headers, params=self.params
        )
        prices = self._process_response(response)
        for quote, price in zip(quotes, prices):
            quote.price = price

        return quotes

    def get_info(self):
        """Create Quote objects."""
        response = requests.get(
            url=self.endpoint, headers=self.headers, params=self.params
        )
        return [
            Quote(symbol=symbol, price=price)
            for symbol, price in zip(
                self.params["symbols"].split(","), self._process_response(response)
            )
        ]

    def _process_response(self, response):
        """Find prices in response dict."""
        return (elem["bid"] for elem in response.json()["quoteResponse"]["result"])

    def __repr__(self):
        return f"{self.__class__.__name__}(params={self.params})"


if __name__ == "__main__":
    params = {"region": "US", "symbols": "AMD,IBM,AAPL"}

    getter = QuoteGetter(api_key=os.environ.get("API_KEY"), params=params)
    quotes = getter.get_info()

    print(quotes)
