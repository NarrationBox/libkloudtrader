from enum import Enum
import libkloudtrader.stocks as stocks
from functools import partial


class Data_Types(Enum):
    US_stocks_daily = partial(stocks.ohlcv)
    
