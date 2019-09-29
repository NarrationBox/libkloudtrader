from enum import Enum
from functools import partial
import libkloudtrader.stocks as stocks
import libkloudtrader.crypto as crypto
import libkloudtrader.options as options


class Data_Types(Enum):
    '''Data Types of backtesting and live trading'''
    US_STOCKS_ohlcv = partial(stocks.ohlcv)
    US_STOCKS_live_feed = partial(stocks.incoming_tick_data_handler)
    CRYPTO_live_feed = partial(crypto.incoming_tick_data_handler)
    CRYPTO_live_feed_level2 = partial(crypto.incoming_tick_data_handler_level2)

