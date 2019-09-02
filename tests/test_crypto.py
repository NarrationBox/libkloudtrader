import libkloudtrader.crypto as crypto
import pandas

CRYPTO_EXCHANGE=crypto.CRYPTO_EXCHANGE

class Test_list_of_exchanges:
    def test_return_type(self):
        '''test return type'''
        data=crypto.list_of_exchanges()
        data2=crypto.list_of_exchanges(test_mode=True)
        assert isinstance(data,list) and isinstance(data2,list) and not 'message' in data

class Test_exchange_strucutre:
    def test_return_type(self):
        '''test return type'''
        data=crypto.exchange_structure()
        assert isinstance(data,str)

class Test_exchange_attribute:
    def test_return_type(self):
        '''test return type'''
        data=crypto.exchange_attribute(attribute="id")
        assert isinstance(data,str) and not 'message' in data
    
    def test_returned_data(self):
        '''test returned data'''
        data=crypto.exchange_attribute(attribute="id")
        assert data==crypto.CRYPTO_EXCHANGE

class Test_markets:
    def test_return_type(self):
        '''test return type'''
        data=crypto.markets()
        assert isinstance(data,dict) and not 'message' in data

class Test_market_structure:
    def test_return_type(self):
        '''test return type'''
        data=crypto.market_structure('BTC/USD')
        assert isinstance(data,dict) and not 'message' in data

    def test_retured_data(self):
        '''test returned data'''
        data=crypto.market_structure('BTC/USD')
        assert 'precision','percentage' in data

class Test_quotes:
    def test_return_type(self):
        '''test return type'''
        data=crypto.quotes('BTC/USD')
        assert isinstance(data,dict) and not 'message' in data

    def test_retured_data(self):
        '''test returned data'''
        data=crypto.quotes('BTC/USD')
        assert 'high','low' in data


class Test_quotes_for_all_symbols:
    def test_return_type(self):
        '''test return type'''
        data=crypto.quotes_for_all_symbols(exchange="binance")
        assert isinstance(data,dict) and not 'message' in data

class Test_ohlcv:
    def test_return_type(self):
        '''test return type'''
        data=crypto.ohlcv(symbol='BTC/USD',start="2018-01-01",end="2018-04-01",dataframe=False)
        data2=crypto.ohlcv(symbol='BTC/USD',start="2019-01-01 17:30:00",end="2019-01-01 17:35:00",interval='1m',dataframe=False)
        assert isinstance(data,list) and isinstance(data2,list)

    def test_return_pandas_type(self):
        '''test pandas return type'''
        data=crypto.ohlcv(symbol='BTC/USD',start="2018-01-01",end="2018-04-01")
        data2=crypto.ohlcv(symbol='BTC/USD',start="2019-01-01 17:30:00",end="2019-01-01 17:35:00",interval='1m')
        assert isinstance(data,pandas.DataFrame) and isinstance(data2,pandas.DataFrame)

    def test_invalid_interval(self):
        '''test invalid interval'''
        data=crypto.ohlcv(symbol='BTC/USD',start="2019-01-01 15:30:00",end="2019-01-01 17:35:00",interval='134m')
        assert data=="Invalid Time Interval"
    
    def test_invalid_date(self):
        pass
    
    def test_invalid_date_format(self):
        pass

class Test_trades:
    def test_return_type(self):
        '''test return type'''
        data=crypto.trades('ETH/BTC',exchange="binance",number_of_data_points=5)
        assert isinstance(data,list) and not 'message' in data

    def test_number_data_points(self):
        '''test number of data points'''
        data=crypto.trades('ETH/BTC',exchange="binance",number_of_data_points=5)
        assert len(data)==5

class Test_order_book:
    def test_return_type(self):
        '''test return type'''
        data=crypto.order_book('BTC/USD',number_of_data_points=5)
        assert isinstance(data,dict) and not 'message' in data

    def test_returned_data(self):
        '''test returned data'''
        data=crypto.order_book('BTC/USD',number_of_data_points=5)
        assert 'bids','asks' in data


class Test_L2_order_book:
    def test_return_type(self):
        '''test return type'''
        data=crypto.L2_order_book('BTC/USD',number_of_data_points=5)
        assert isinstance(data,dict) and not 'message' in data

    def test_returned_data(self):
        '''test returned data'''
        data=crypto.L2_order_book('BTC/USD',number_of_data_points=5)
        assert 'bids','asks' in data


class Test_currencies:
    def test_return_type(self):
        '''test return type'''
        data=crypto.currencies(exchange="kraken")
        assert isinstance(data,dict) and not 'message' in data
        

class Test_user_balance:
    def test_return_type(self):
        '''test return type'''
        data=crypto.user_balance(test_mode=True)
        assert isinstance(data,dict) and not 'message' in data
    
    def test_returned_data(self):
        '''test returned data'''
        data=crypto.user_balance(test_mode=True)
        assert 'info' in data

class Test_user_trades:
    def test_return_type(self):
        '''test return type'''
        data=crypto.user_trades('BTC/USD',test_mode=True)
        assert isinstance(data,list) and not 'message' in data
    
    def test_returned_data(self):
        '''test returned data'''
        data=crypto.user_trades('BTC/USD',test_mode=True)
        assert 'id','info' in data[0]

class Test_user_closed_orders:
    def test_return_type(self):
        '''test return type'''
        data=crypto.user_closed_orders('BTC/USD',test_mode=True)
        assert isinstance(data,list) and not 'message' in data
    
    def test_returned_data(self):
        '''test returned data'''
        data=crypto.user_closed_orders('BTC/USD',test_mode=True)
        assert 'id','info' in data[0]
"""
class Test_get_order:
    def test_return_type(self):
        '''test return type'''
        data=crypto.get_order(order_id="55d7e42e-3a6c-41f7-a692-9bdcd23dce70",symbol='BTC/USD',test_mode=True)
        assert isinstance(data,dict) and not 'message' in data
    
    def test_returned_data(self):
        '''test returned data'''
        data=crypto.get_order(order_id="55d7e42e-3a6c-41f7-a692-9bdcd23dce70",symbol='BTC/USD',test_mode=True)
        assert 'id','info' in data
"""
class Test_user_orders:
    def test_return_type(self):
        '''test return type'''
        data=crypto.user_orders('BTC/USD',test_mode=True)
        assert isinstance(data,list) and not 'message' in data
    
    def test_returned_data(self):
        '''test returned data'''
        data=crypto.user_orders('BTC/USD',test_mode=True)
        assert 'id','info' in data[0]

class Test_create_deposit_address:
    pass

class Test_user_deposits:
    pass

class Test_user_deposit_address:
    pass

class Test_user_withdrawls:
    pass

class Test_user_transactions:
    def test_return_type(self):
        '''test return type'''
        data=crypto.user_transactions('USD',test_mode=True)
        assert isinstance(data,list) and not 'message' in data
