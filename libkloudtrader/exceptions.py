class InvalidBrokerage(Exception):
    '''Exception for invalid brokerage'''
    pass


class InvalidStockExchange(Exception):
    '''Exception for invalid stock exchange'''
    pass


class InvalidCryptoExchange(Exception):
    '''Exception for invalid crypto exchange'''
    pass


class BadRequest(Exception):
    '''Exception for Bad Request/bad parameters'''
    pass


class InvalidCredentials(Exception):
    '''Exception for 401, Wrong Credentials'''
    pass


class OverwriteError(Exception):
    '''Exception raised when trying to add elements to DoubleEndedBuffer that has allow_overwrite=False and size==maxlen'''
    pass


class InvalidAlgorithmMode(Exception):
    '''Exception raised if mode for libkloudtrader.algorithm.run() is invalid'''
    pass


class EmptySymbolBucket(Exception):
    '''Excption raised if symbol bucket is empty'''
    pass


class InvalidDataFeedType(Exception):
    '''Exception raised if user asks for invalid data feed'''
    pass


class AnalysisException(Exception):
    """Exception raised if something goes wrong in libkloudtrader.analysis"""
    pass


class InvlaidTimeInterval(Exception):
    """Exception raised if input interval for historical data apis is invalid"""
    pass


class InvalidPricePoint(Exception):
    """Exception raised if price point is invalid for backtesting"""
    pass


class OrderError(Exception):
    '''Exception raised if any error with order arises'''
    pass


class AccountError(Exception):
    '''Exception raised if any error with user's account arises'''
    pass


class AuthError(Exception):
    '''Exception raised if any error with Auth'''
    pass


class ResponseError(Exception):
    '''Exception raised if any error with response from the exchange'''
    pass


class ExchangeError(Exception):
    '''Exception raised if a crypto exchange cannot process user request'''
    pass


class NetworkError(Exception):
    '''Exception raised due to network issues on either client or exchange side'''
    pass


class FunctionalityNotSupported(Exception):
    '''Exception raised if functionality is not supported by the crypto exchange'''
    pass
