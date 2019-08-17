import libkloudtrader.analysis as analysis
import libkloudtrader.stocks as stocks
import libkloudtrader.processing as processing
import libkloudtrader.algorithm as algorithm
import numpy as np
import pandas as pd
import libkloudtrader.crypto as crypto



from streamz import Stream
source = Stream()
def return_orderbook(symbol):
    #data=processing.add_data_to_batch(batch_size=50,data='stocks_bid')
    #a=crypto.order_book('BTC/USD',number_of_data_points=1)['bids']
    #for i in a:
    a=processing.add_data_to_batch(batch_size=50,data='crypto_bid')
        #return 'BidPrice: {}, BidSize: {}'.format(i[0],i[1])
    df=pd.DataFrame()
    df['SMA_5']=analysis.ma(a,5)
    df['SMA_25']=analysis.ma(a,25)
    previous_5 = df['SMA_5'].shift(1)
    previous_25 = df['SMA_25'].shift(1)
    crossing = (((df['SMA_5'] <= df['SMA_25']) & (previous_5 >= previous_25))
            | ((df['SMA_5'] >= df['SMA_25']) & (previous_5 <= previous_25)))

    return crossing







algorithm.run(mode='live',strategy_name=return_orderbook,states=['premarket','open','postmarket','closed'],symbols=['AAPL'])
