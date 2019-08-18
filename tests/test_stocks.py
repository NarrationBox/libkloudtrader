'''This module contains tests for stocks module'''

import sys
import datetime
sys.path.append('./libkloudtrader')
import pandas
import libkloudtrader.stocks as stocks

class TestLatestPriceInfo:
    def test_type(self):
        """Test return type"""
        data = stocks.latest_price_info('AAPl')
        assert isinstance(data, dict)

    def test_pandas_type(self):
        """Test return type"""
        data = stocks.latest_price_info('AAPl', dataframe=True)
        assert isinstance(data, pandas.DataFrame)

    def test_data(self):
        """Test if data is correct"""
        data = stocks.latest_price_info('AAPl')
        assert 'last','change' in data

    def test_multiple_symbols(self):
        """Test multiple symbols as input"""
        data=stocks.latest_price_info('AAPL,SPY,GOOG,GE')
        for i in data:
            assert 'last','change' in data

class TestCreateSession:
    def test_return_type(self):
        """Test return type and data"""
        data=stocks.create_session()
        assert isinstance(data,str) 

class TestLatestQuote:
    def test_return_type_and_data(self):
        """Test return type and data"""
        data=stocks.latest_quote('aapl')
        assert isinstance(data,dict) and 'bidsz','ask' in data
    
    def test_wrong_symbol_input(self):
        """Test non existing symbol as input"""
        pass

class TestLatestTrade:
    def test_return_type_and_data(self):
        """Test return type and data"""
        data=stocks.latest_trade('aapl')
        assert isinstance(data,dict) and 'last','type' in data
    
    def test_wrong_symbol_input(self):
        """Test non existing symbol as input"""
        pass

class TestIntradaySummary:
    def test_return_type_and_data(self):
        """Test return type and data"""
        data=stocks.intraday_summary('aapl')
        assert isinstance(data,dict) and 'open','low' in data
    
    def test_wrong_symbol_input(self):
        """Test non existing symbol as input"""
        pass

class TestOHLCV:
    def test_type(self):
        """Test return type"""
        data = stocks.ohlcv('AAPl',start="2018-01-01",end="2019-01-01",dataframe=False)
        assert isinstance(data, dict)
    
    def test_pandas_type(self):
        """Test return Type"""
        data=stocks.ohlcv('AAPl',start="2018-01-01",end="2019-01-01")
        assert isinstance(data, pandas.DataFrame)

    def test_data(self):
        """Test data returned"""
        data=stocks.ohlcv('AAPl',start="2018-01-01",end="2019-01-01",dataframe=False)
        assert 'day' in data['history']

    def test_wrong_date(self):
        """Exception for wrong date"""
        pass
    
    def test_multiple_symbols(self):
        """No data retured with multiple symbols"""
        pass

    def test_number_returned_data_points(self):
        """Test number of data of points returned based on start and end"""
        pass

    def test_fake_symbol(self):
        """Test when a symbol is given that does not exists"""
        pass
'''
class TesthistoricalTickData:
    def setup(self):
        self.start=datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        d = datetime.datetime.today() - datetime.timedelta(days=3)
        self.end=d.strftime("%Y-%m-%d %H:%M:%S")
    def test_type(self):
        """Test return type"""
        data = stocks.tick_data('AAPL',start=self.start,end=self.end)
        assert isinstance(data, dict)
    
    def test_pandas_type(self):
        """Test return Type"""
        data=stocks.tick_data('AAPL',start=self.start,end=self.end,dataframe=True)
        assert isinstance(data, pandas.DataFrame)

    def test_data(self):
        """Test data returned"""
        data=stocks.tick_data('AAPL',start=self.start,end=self.end)
        assert 'data' in data['series']
    
    def test_date_older_than_allowed(self):
        """Test for date input older than 5 days."""
    pass

    def test_multiple_symbols(self):
        """No data retured with multiple symbols"""
        pass

    def test_number_returned_data_points(self):
        """Test number of data of points returned based on start and end"""
        pass

    def test_fake_symbol(self):
        """Test when a symbol is given that does not exists"""
        pass

class Test1minBarData:
    def setup(self):
        self.start=datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        d = datetime.datetime.today() - datetime.timedelta(days=3)
        self.end=d.strftime("%Y-%m-%d %H:%M:%S")
        print(self.start)
    def test_type(self):
        """Test return type"""
        data = stocks.min1_bar_data('AAPL',start=self.start,end=self.end)
        assert isinstance(data, dict)

    def test_pandas_type(self):
        """Test return Type"""
        data=stocks.min1_bar_data('AAPL',start=self.start,end=self.end,dataframe=True)
        assert isinstance(data, pandas.DataFrame)

    def test_data(self):
        """Test data returned"""
        data=stocks.min1_bar_data('AAPL',start=self.start,end=self.end)
        assert 'data' in data['series']
    
    def test_date_older_than_allowed(self):
        """Test for date input older than 20 days with open filter and 10 days with all filter"""
        pass

    def test_multiple_symbols(self):
        """No data retured with multiple symbols"""
        pass

    def test_number_returned_data_points(self):
        """Test number of data of points returned based on start and end"""
        pass

    def test_fake_symbol(self):
        """Test when a symbol is given that does not exists"""
        pass

class Test5minBarData:
    def setup(self):
        self.start=datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        d = datetime.datetime.today() - datetime.timedelta(days=8)
        self.end=d.strftime("%Y-%m-%d %H:%M:%S")
    def test_type(self):
        """Test return type"""
        data = stocks.min5_bar_data('AAPL',start=self.start,end=self.end)
        assert isinstance(data, dict)

    def test_pandas_type(self):
        """Test return Type"""
        data=stocks.min5_bar_data('AAPL',start=self.start,end=self.end,dataframe=True)
        assert isinstance(data, pandas.DataFrame)

    def test_data(self):
        """Test data returned"""
        data=stocks.min5_bar_data('AAPL',start=self.start,end=self.end)
        assert 'data' in data['series']
    
    def test_date_older_than_allowed(self):
        """Test for date input older than 40 days with open filter and 18 days with all filter"""
        pass

    def test_multiple_symbols(self):
        """No data retured with multiple symbols"""
        pass

    def test_number_returned_data_points(self):
        """Test number of data of points returned based on start and end"""
        pass

    def test_fake_symbol(self):
        """Test when a symbol is given that does not exists"""
        pass

class Test15minBarData:
    def setup(self):
        self.start=datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        d = datetime.datetime.today() - datetime.timedelta(days=10)
        self.end=d.strftime("%Y-%m-%d %H:%M:%S")
    def test_type(self):
        """Test return type"""
        data = stocks.min15_bar_data('AAPL',start=self.start,end=self.end)
        assert isinstance(data, dict)

    def test_pandas_type(self):
        """Test return Type"""
        data=stocks.min15_bar_data('AAPL',start=self.start,end=self.end,dataframe=True)
        assert isinstance(data, pandas.DataFrame)

    def test_data(self):
        """Test data returned"""
        data=stocks.min15_bar_data('AAPL',start=self.start,end=self.end)
        assert 'data' in data['series']
    
    def test_date_older_than_allowed(self):
        """Test for date input older than 40 days with open filter and 18 days with all filter"""
        pass

    def test_multiple_symbols(self):
        """No data retured with multiple symbols"""
        pass

    def test_number_returned_data_points(self):
        """Test number of data of points returned based on start and end"""
        pass

    def test_fake_symbol(self):
        """Test when a symbol is given that does not exists"""
        pass
'''
class TestStreamLiveQuotes:
    def test_return_type_and_data(self):
        """Test return type and data"""
        for data in stocks.stream_live_quotes('aapl'):
            assert isinstance(data,dict) and 'bidsz','ask' in data
            break
            
    def test_wrong_symbol_input(self):
        """Test non existing symbol as input"""
        pass

class TestStreamLiveTrades:
    def test_return_type_and_data(self):
        """Test return type and data"""
        for data in stocks.stream_live_trades('aapl'):
            assert isinstance(data,dict) and 'last','type' in data
            break
    
    def test_wrong_symbol_input(self):
        """Test non existing symbol as input"""
        pass

class TestStreamLiveSummary:
    def test_return_type_and_data(self):
        """Test return type and data"""
        for data in stocks.stream_live_summary('aapl'):
            assert isinstance(data,dict) and 'open','low' in data
            break
    
    def test_wrong_symbol_input(self):
        """Test non existing symbol as input"""
        pass


class TestListOfCompanies:
    def test_return_type(self):
        """Test return Type"""
        list_of_exchanges=['all','nyse','nasdaq','amex']
        for x in list_of_exchanges:
            data=stocks.list_of_companies(x)
            assert isinstance(data,pandas.DataFrame)
        
    def test_data(self):
        """Test columns in the returned dataframe"""
        pass
        
class TestIntradayStatus:
    def test_return_type(self):
        """Test return type"""
        data=stocks.intraday_status()
        assert isinstance(data,dict)
    
    def test_data(self):
        """Test return data"""
        data=stocks.intraday_status()
        assert 'date' and 'next_state' in data

class TestMarketCalendar:
    def test_return_type(self):
        """Test return type"""
        data=stocks.market_calendar(7,2019)
        assert isinstance(data,dict)
    
    def test_wrong_inputs(self):
        """Test wrong inputs"""
        pass

class TestSymbolSearch:
    def test_return_type(self):
        """Test return type"""
        data=stocks.symbol_search('apple')
        assert isinstance(data,dict)
    
    def test_wrong_input(self):
        """Test wrong input"""
        pass

class TestSymbolLookup:
    def test_return_type(self):
        """Test return type"""
        data=stocks.symbol_lookup('aap')
        assert isinstance(data,dict)
    
    def test_wrong_input(self):
        """Test wrong input"""
        pass

class TestShortableSecurities:
    def test_return_type(self):
        """Test return type"""
        data=stocks.shortable_securities(dataframe=False)
        assert isinstance(data,dict)
    
    def test_pandas_return_type(self):
        """Test datframe = True return type"""
        data=stocks.shortable_securities()
        assert isinstance(data,pandas.DataFrame)

    def test_data(self):
        """Test returned data"""
        data=stocks.shortable_securities(dataframe=False)
        assert 'security' in data['securities']

class TestCheckIfShortable:
    def test_return_type_and_return_data_for_right_symbol(self):
        """Test return type and data"""
        data=stocks.check_if_shortable('GOOG')
        assert isinstance(data,bool) and data==True

    def test_return_type_and_return_data_for_wrong_symbol(self):
        """Test return type and data"""
        data=stocks.check_if_shortable('RTADSS45')
        assert isinstance(data,bool) and data==False


class TestCompanyFundamentals:
    def test_return_type(self):
        """Test return type and data"""
        data=stocks.company_fundamentals('AAPL')
        assert isinstance(data,list) 

    def test_wrong_symbol(self):
        """Test wrong symbol"""
        pass

class TestCorporateCalendar:
    def test_return_type(self):
        """Test return type and data"""
        data=stocks.corporate_calendar('AAPL')
        assert isinstance(data,list) 

    def test_wrong_symbol(self):
        """Test wrong symbol"""
        pass

class TestCorporateActions:
    def test_return_type(self):
        """Test return type and data"""
        data=stocks.dividend_information('AAPL')
        assert isinstance(data,list) 

    def test_wrong_symbol(self):
        """Test wrong symbol"""
        pass

class TestDividendInformation:
    def test_return_type(self):
        """Test return type and data"""
        data=stocks.dividend_information('AAPL')
        assert isinstance(data,list) 

    def test_wrong_symbol(self):
        """Test wrong symbol"""
        pass

class TestCorporateActions:
    def test_return_type(self):
        """Test return type and data"""
        data=stocks.corporate_actions('AAPL')
        assert isinstance(data,list) 

    def test_wrong_symbol(self):
        """Test wrong symbol"""
        pass

class TestOperationRatio:
    def test_return_type(self):
        """Test return type and data"""
        data=stocks.operation_ratio('AAPL')
        assert isinstance(data,list) 

    def test_wrong_symbol(self):
        """Test wrong symbol"""
        pass

class TestCorporateFiancials:
    def test_return_type(self):
        """Test return type and data"""
        data=stocks.corporate_financials('AAPL')
        assert isinstance(data,list) 

    def test_wrong_symbol(self):
        """Test wrong symbol"""
        pass

class TestPriceStatistics:
    def test_return_type(self):
        """Test return type and data"""
        data=stocks.price_statistics('AAPL')
        assert isinstance(data,list) 

    def test_wrong_symbol(self):
        """Test wrong symbol"""
        pass


class TestBuyPreview:
    pass

class TestBuyToCoverPreview:
    pass

class TestSellPreview:
    pass

class TestSellShortPreview:
    pass

class TestBuy:
    pass

class TestBuyToCover:
    pass

class TestSell:
    pass

class TestShortSell:
    pass

class TestChangeOrder:
    pass

class TestCancelOrder:
    pass

class TestUserProfile:
    def test_return_type(self):
        '''test return type'''
        data=stocks.user_profile()
        assert isinstance(data,dict)

    def test_returned_data(self):
        '''test returned data'''
        data=stocks.user_profile()
        assert 'account'in data['profile']

class TestAccountBalance:
    def test_return_type(self):
        '''test return type'''
        data=stocks.account_balance()
        assert isinstance(data,dict)

    def test_returned_data(self):
        '''test returned data'''
        data=stocks.account_balance()
        assert 'option_short_value','equity' in data['balances']

class TestAccountHistory:
    def test_return_type(self):
        '''test return type'''
        data=stocks.account_history()
        assert isinstance(data,dict)

    def test_returned_data(self):
        '''test returned data'''
        data=stocks.account_history()
        assert 'event' in data['history']

class TestAccountPositions:
    def test_return_type(self):
        '''test return type'''
        data=stocks.account_positions()
        assert isinstance(data,dict)

class TestAccountClosedPositions:
    def test_return_type(self):
        '''test return type'''
        data=stocks.account_closed_positions()
        assert isinstance(data,dict)

class TestAccountOrders:
    def test_return_type(self):
        '''test return type'''
        data=stocks.account_orders()
        assert isinstance(data,dict)
