"""StockPicker interface class module."""
import os

from ._factory import _getter_factory
from .table import StockTable

class StockPicker:

    def __init__(self, info_type='quote', **kwargs):
        self.info_type = info_type

        self._info_getter = _getter_factory(info_type, **kwargs)
        self._request_info()

    def _request_info(self):
        if not hasattr(self, 'info'):
            self.info = self._info_getter.get_info()
        else:
            self.info = self._info_getter.update_info(self.info)

    def __repr__(self):
        return f"{self.__class__.__name__}(info_type='{self.info_type}')"

if __name__ == '__main__':
    params = {"region":"US", "symbols":"AMD,IBM,AAPL"}

    picker = StockPicker(api_key=os.environ.get('API_KEY'), params=params)

    print(picker)
