import libkloudtrader.options as options
import pandas

class TestChains:
    def test_return_type(seld):
        '''test return type'''
        data=options.chains(underlying_symbol="AAPL",expiration="2019-08-16")
        assert isinstance(data,list)
    
    def test_dataframe_return_type(seld):
        '''test dataframe return type'''
        data=options.chains(underlying_symbol="AAPL",expiration="2019-08-16",dataframe=True)
        assert isinstance(data,pandas.DataFrame)

    def test_data(self):
        '''test returned data'''
        data=options.chains(underlying_symbol="AAPL",expiration="2019-08-16")
        assert 'description','high'in data[0]

    def test_wrong_symbl(self):
        pass

    def test_Wrong_date(self):
        pass


class TestExpirations:
    def test_return_type(seld):
        '''test return type'''
        data=options.expirations(underlying_symbol="AAPL")
        assert isinstance(data,list)

    def test_data(self):
        '''test returned data'''
        data=options.expirations(underlying_symbol="AAPL")
        assert 'data','strikes' in data[0]

    def test_wrong_symbol(self):
        '''test wrong underlying symbol'''
        data=options.expirations(underlying_symbol="AAPL##RRWSSDJKF")
        assert data['expirations']==None

class TestStrikes:
    def test_return_type(seld):
        '''test return type'''
        data=options.strikes(underlying_symbol="AAPL",expiration="2019-07-19")
        assert isinstance(data,dict)
    
    def test_data(self):
        '''test returned data'''
        data=options.strikes(underlying_symbol="AAPL",expiration="2019-07-19")
        assert 'strike' in data['strikes']

class TestBuyToOpen:
    pass

class TestBuyToClose:
    pass

class TestSellToOpen:
    pass

class TestSellToClose:
    pass