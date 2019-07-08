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
