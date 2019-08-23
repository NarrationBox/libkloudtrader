from typing import Any
from streamz import Stream
import numpy as np
import libkloudtrader.stocks as stocks
from .exceptions import InvalidAlgorithmMode, EmptySymbolBucket
import pandas as pd
from libkloudtrader.enumerables import Data_Types
import libkloudtrader.processing as processing
import random

source = Stream()


def backtest(symbol: str,
             strategy: str,
             data:str,
             start_date: Any = None,
             end_date: Any = None,
             data_interval:str='1d',
             initial_capital: float = None,
             comission:float=0):

    data_to_backtest=Data_Types[data].value
    print(data_to_backtest(symbol,start_date, end_date,interval=data_interval))
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


def live_trade(
        strategy_name: str,
        symbol_bucket: list,
        states: list = ['open'],data:str=None,size=0):
    try:
        if not symbol_bucket:
            raise EmptySymbolBucket(
                'Symbol Bucket is empty. It must containe at least one equity or crypto symbol to trade.'
            )
        symbol_bucket = np.array(symbol_bucket)
        print("{} is now entering the live markets. All the Best!".format(
                strategy_name.__name__))
        while stocks.intraday_status()['state'] in states:
            for symbol in symbol_bucket:
                if size==1:
                    print('Latest ASK Price for {}'.format(symbol))
                    locals()['strategy_name'](float(stocks.latest_quote(symbol)['ask'])+random.uniform(-2, 2))
                else:
                    batch=processing.Buffer(size)
                    while len(batch)<size:
                        data=float(stocks.latest_quote(symbol)['ask']+random.uniform(-2, 2))
                        batch.append(data)
                        #if len(batch)==size:
                        data_batch=pd.Series()
                        data_batch.name=symbol+"ask_prices"
                        df=pd.Series(np.array(batch))
                        #print(data_batch.append(df))
                        locals()['strategy_name'](data_batch.append(df))
                        #    batch.popleft()
                    

    except Exception as exception:
        raise exception
