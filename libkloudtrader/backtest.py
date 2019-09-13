import pandas as pd
from libkloudtrader.exceptions import InvalidPricePoint


class Backtest():
    def __init__(self,locals, preferred_price_point):
        self.buy_signal=locals['buy']
        self.sell_signal=locals['sell']
        self.cover_signal=locals['cover']
        self.short_signal=locals['short']
        self.data_to_bakctest_on=locals['data']
        self.default_price=preferred_price_point
        if self.default_price.lower() not in ('open','high','low','close'):
            raise InvalidPricePoint("Invalid price point. Please select a price point from 'open','high','low','close'")


    @property
    def signals(self):
        df= pd.DataFrame()
        df['buy']=self.buy_signal
        df['sell']=self.sell_signal
        df['cover']=self.cover_signal
        df['short']=self.short_signal
        return df

    @property
    def data(self):
        return self.data_to_bakctest_on

    @property
    def preferred_price_point(self):
        return self.default_price