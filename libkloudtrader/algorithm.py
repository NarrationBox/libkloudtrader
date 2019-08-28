from typing import Any
import random
import time
import numpy as np
import pandas as pd
import libkloudtrader.stocks as stocks
from libkloudtrader.exceptions import InvalidAlgorithmMode, EmptySymbolBucket, InvalidDataFeedType
from libkloudtrader.enumerables import Data_Types
import libkloudtrader.processing as processing
from libkloudtrader.logs import start_logger

logger = start_logger(__name__)
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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
               data_feed_type: str,
               states: list = ['open'],
               batch_size: int = 1000,
               feed_delay: float = 0.0,
               fake_feed: bool = False):
    try:
        logger.info("{} is now entering the live markets. 📈\n".format(
            strategy_name.__name__))
        if isinstance(symbol_bucket, list):
            symbol_bucket = np.array(symbol_bucket)
        elif type(symbol_bucket) not in (numpy.ndarray, list):
            raise TypeError('Symbol bucket must be a list or numpy array')
        if data_feed_type not in ('CRYPTO_live_feed', 'US_STOCKS_live_feed',
                                  'CRYPTO_live_feed_level2'):
            raise InvalidDataFeedType(
                'This Data Feed is not available for live trading. Please use libkloudtrader.algorithm.backtest() for backtesting or using hisotrical data.'
            )
        if data_feed_type in ("CRYPTO_live_feed", 'CRYPTO_live_feed_level2'):
            feed_delay = 2
        data_feed = Data_Types[data_feed_type].value
        while stocks.intraday_status()['state'] in states:
            batch = processing.Buffer(batch_size, dtype=object)
            while len(batch) < batch_size:
                for symbol in symbol_bucket:
                    batch.append(data_feed(symbol, fake_feed=fake_feed))
                    data_batch = pd.DataFrame(batch)
                    locals()['strategy_name'](data_batch)
                    if len(batch) == batch_size:
                        batch.popleft()
                    time.sleep(feed_delay)
    except (KeyboardInterrupt, SystemExit):
        print('\n')
        logger.critical('User stopped the algorithm')
    except Exception as exception:
        logger.critical('Exiting {}...'.format(strategy_name.__name__))
        logger.warning(
            'Oops! Something went wrong while your algorithm was being deployed to live markets. ⚠️'
        )
        logger.error(exception)
        exit()
