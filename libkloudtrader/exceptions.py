class InvalidBrokerage(Exception):
    '''Exception for invalid brokerage'''
    pass


class InvalidStockExchange(Exception):
    '''Exception for invalid stock exchange'''
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
