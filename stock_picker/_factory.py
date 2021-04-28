from stock_picker.stock_info import QuoteGetter

GETTER_LIBRARY = {
    "quote": QuoteGetter,
}


def _getter_factory(info_type, **kwargs):
    """Instantiate requested StockInfoGetter subclass with kwargs."""
    return GETTER_LIBRARY[info_type](**kwargs)

