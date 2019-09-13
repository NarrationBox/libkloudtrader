import libkloudtrader.analysis as analysis
import libkloudtrader.stocks as stocks
import libkloudtrader.crypto as crypto
import pandas as pd
#load data
aapl_data=stocks.ohlcv('AAPL','2018-01-01','2019-01-01')

print(analysis.average_directional_index(aapl_data['high'],aapl_data['low'],aapl_data['close'],4))