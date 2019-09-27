from libkloudtrader.algorithm import *
import pandas as pd
import libkloudtrader.analysis as analysis

def crypto_turtle(data):
    data['high']=data.price.shift(1).rolling(window=5).max()
    data['low']=data.price.shift(1).rolling(window=5).min()
    data['avg']=analysis.ma(data.price,5)
    buy=data.price>data.high
    sell=data.price<data.avg
    short=data.price<data.low
    cover=data.price>data.avg
    if buy.tail(1).bool():
        logger.info('Buy signal')
    if sell.tail(1).bool():
        logger.info('Sell signal')
    if short.tail(1).bool():
        logger.info('Short signal')
    if cover.tail(1).bool():
        logger.info('Cover signal')


live_trade(crypto_turtle,symbol_bucket=['BTC/USD'],data_feed_type="CRYPTO_live_feed")