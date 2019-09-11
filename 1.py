import libkloudtrader.analysis as analysis
import libkloudtrader.stocks as stocks

aapl_data=stocks.ohlcv('AAPL','2018-01-01','2019-01-01')
print(analysis.moving_standard_deviation(aapl_data['close'],5))