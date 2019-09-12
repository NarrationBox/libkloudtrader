import libkloudtrader.analysis as analysis
import libkloudtrader.stocks as stocks
import libkloudtrader.crypto as crypto

#load data
aapl_data=stocks.ohlcv('AAPL','2018-01-01','2019-01-01')

print(analysis.rate_of_change(aapl_data['close'],7))