import os
from abc import ABC, abstractmethod
from dataclasses import dataclass

import requests


@dataclass
class StockInfo:
    symbol: str

    def __iter__(self):
        return iter(self.__dict__)

    def __getitem__(self, key):
        return self.__dict__[key]


@dataclass
class Quote(StockInfo):
    price: float


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

