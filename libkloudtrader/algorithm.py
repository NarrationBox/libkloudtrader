from typing import Any
import random
import time
import logging
import numpy as np
import libkloudtrader.stocks as stocks
from .exceptions import InvalidAlgorithmMode, EmptySymbolBucket
import pandas as pd
from libkloudtrader.enumerables import Data_Types
import libkloudtrader.processing as processing

def backtest(symbol: str,
             strategy: str,
             data: str,
             start_date: Any = None,
             end_date: Any = None,
             data_interval: str = '1d',
             initial_capital: float = None,
             comission: float = 0):

    data_to_backtest = Data_Types[data].value
    print(
        data_to_backtest(symbol, start_date, end_date, interval=data_interval))
    #print(return_data_from_enum(a,symbol,start_date, end_date))
    #print(locals()[a](symbol, start_date, end_date))
    '''
    initial_capital=float(initial_capital)
    positions=pd.DataFrame(index=signals_dataframe.index).fillna(0.0)
    positions['Positions in TSLA']=1000*signals_dataframe['signal']
    portfolio=positions.multiply(data['close'],axis=0)
    pos_diff=positions.diff()
    portfolio['holdings']=(positions.multiply(data['close'],axis=0).sum(axis=1))
    portfolio['cash']=initial_capital-(pos_diff.multiply(data['close'],axis=0)).sum(axis=1).cumsum()
    portfolio['total']=portfolio['cash']+portfolio['holdings']
    portfolio['returns']=portfolio['total'].pct_change()
    print(portfolio.tail(10))'''
    return strategy.__name__


def live_trade(strategy_name: str,
               symbol_bucket: list,
               states: list = ['open'],
               data: str = None,
               batch_size=500):
    try:
        logging.info("{} is now entering the live markets. All the Best 👍🏼".format(
            strategy_name.__name__))
        if isinstance(symbol_bucket, list):
            symbol_bucket = np.array(symbol_bucket)
        elif type(symbol_bucket) not in (numpy.ndarray, list):
            raise TypeError('Symbol bucket must be a list or numpy array')
        while stocks.intraday_status()['state'] in states:
            batch = processing.Buffer(batch_size, dtype=object)
            while len(batch) < batch_size:
                for symbol in symbol_bucket:
                    batch.append(stocks.incoming_tick_data_handler(symbol,fake_feed=True))
                    data_batch = pd.DataFrame(batch)
                    locals()['strategy_name'](
                        data_batch) 
                    if len(batch)==batch_size:
                        batch.popleft()
                    time.sleep(1)
    except Exception as exception:
        logging.exception(exception)
        break
