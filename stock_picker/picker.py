"""StockPicker interface class module."""
from stock_picker._factory import _getter_factory
from stock_picker.table import StockTable


def start_picker(info_type="quote", time=60_000, **kwargs):
    stock_getter = _getter_factory(info_type,**kwargs)
    table = StockTable(stock_getter, refresh_time=time)
    table.display()

