from libkloudtrader.algorithm import *
import libkloudtrader.analysis as analysis
import pandas as pd
import numpy as np



def ba(backtest,data):

    data['high']=data.close.shift(1).rolling(window=5).max()
    data['low']=data.close.shift(1).rolling(window=5).min()
    data['avg']=analysis.ma(data.close,5)
    buy=(data.close>data.high)
    sell=(data.close<data.avg)
    #short=(data.close<data.low)
    #cover=(data.close>data.avg)
    if buy.tail(1).bool():
        backtest.buy(5)
    elif sell.tail(1).bool():
        backtest.sell(5)


    #rets=analysis.daily_returns(data.close)
    #data['volatility']=analysis.moving_volatility(rets,1)
    #data['slip']=data.high-data.close
   


    

run_backtest(ba,['AAPL'],data="US_STOCKS_times_and_sale",start='2019-09-24 09:30:00',end='2019-09-24 15:30:00',data_interval='15m')