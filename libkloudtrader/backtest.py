'''
import pandas as pd
from libkloudtrader.exceptions import InvalidPricePoint


class Backtest():
    def __init__(self, locals, preferred_price_point):
        self.buy_signal = locals['buy']
        self.sell_signal = locals['sell']
        self.cover_signal = locals['cover']
        self.short_signal = locals['short']
        self.data_to_bakctest_on = locals['data']
        self.default_price = preferred_price_point
        if self.default_price.lower() not in ('open', 'high', 'low', 'close'):
            raise InvalidPricePoint(
                "Invalid price point. Please select a price point from 'open','high','low','close'"
            )

    @property
    def signals(self):
        df = pd.DataFrame()
        df['buy'] = self.buy_signal
        df['sell'] = self.sell_signal
        df['cover'] = self.cover_signal
        df['short'] = self.short_signal
        return df

    @property
    def data(self):
        return self.data_to_bakctest_on

    @property
    def preferred_price_point(self):
        return self.default_price
'''
import numpy as np
import pandas as pd

class Backtest():
    def __init__(self,capital:float,commission:float,enable_slippage:bool):
        """Init backtest"""
        self.capital=capital
        self.bar=0
        self.position=0
        self.commission=commission
        self.enable_slippage=enable_slippage
        self.slippage=0
        self.trades_log=pd.DataFrame(columns=['datetime','trade_type','price','fill_price','order_cost','capital','position'])

    
    def buy(self,quantity):
        '''emulates a buy order'''
        self.capital-=self.order_cost
        self.update_positions(quantity)
        self.update_trade_logs(datetime=self.bar.datetime,trade_type='Buy',price=self.bar.close,fill_price=self.fill_price,order_cost=self.order_cost,capital=self.capital,position=self.position)
        #print('Bought {} of stocks @ {} but price is {}'.format(quantity,self.order_cost,self.bar.close))

    
    def sell(self,quantity):
        '''emulates a sell order'''
        #if self.position!=0:
        self.capital+=self.order_cost
        self.update_positions(-1*quantity)
        self.update_trade_logs(datetime=self.bar.datetime,trade_type='Sell',price=self.bar.close,fill_price=self.fill_price,order_cost=self.order_cost,capital=self.capital,position=self.position)
        #print('Sold {} of stocks @ {} but price is {}'.format(quantity,self.order_cost,self.bar.close))
        #else:
            #pass#print('No position to close')

    def update_trade_logs(self,datetime,trade_type,price,fill_price,order_cost,capital,position):
        df=pd.DataFrame([{'datetime':datetime,'trade_type':trade_type,'price':price,'fill_price':fill_price,'order_cost':order_cost,'capital':capital,'position':position}])
        self.trades_log=self.trades_log.append(df)


    @property
    def get_trade_log(self):
        self.trades_log.set_index('datetime',inplace=True)
        return self.trades_log

    def update_bar(self,index,bar):
        self.bar=bar
        self.bar.datetime=index

    def update_positions(self,quantity):
        self.position+=quantity

    @property
    def calculate_commission(self):
        commiss=(self.commission/100)*self.bar.close
        return commiss

    @property
    def calculate_slippage(self):
        '''how is slippage calculated?'''
        '''slippage should not be more than 2% in most of the trades. so we generate a random percentage b/w 0-2.use that number as %age'''
        if self.enable_slippage:
            slippage_percent= np.random.uniform(low=0, high=0.02)
            slippage=slippage_percent*self.bar.close
            return slippage
        return 0.0
    
    @property   
    def fill_price(self):
        return self.bar.close+self.calculate_slippage
        

    @property   
    def order_cost(self):
        return self.fill_price+self.calculate_commission
         
    
    @property
    def getcapital(self):
        return self.capital

    @property
    def getbar(self):
        return self.bar

    @property
    def getposition(self):
        return self.position

    @property
    def get_portfolio(self):
        trade_log=self.get_trade_log
        portfolio=pd.DataFrame(index=trade_log.index)
        portfolio['holdings']=trade_log.position.multiply(trade_log.price)
        portfolio['cash']=trade_log.capital
        portfolio['total']=portfolio.cash+portfolio.holdings
        return portfolio