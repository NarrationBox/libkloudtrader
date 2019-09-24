from typing import Any
import datetime
import ccxt.async_support as ccxt
import ccxt as non_async_ccxt
from libkloudtrader.exceptions import InvlaidTimeInterval, FunctionalityNotSupported, BadRequest, OrderError, AccountError, AuthError, ResponseError, ExchangeError, NetworkError, InvalidCryptoExchange


def check_exchange_existence(exchange: str) -> bool:
    try:
        if exchange in non_async_ccxt.exchanges:
            return True
        raise InvalidCryptoExchange('Exchange not supported as of now.')
    except Exception as exception:
        raise exception


def ListOfExchanges(test_mode: bool) -> list:
    try:
        if test_mode:
            list_of_exchanges = non_async_ccxt.exchanges
            list_of_exchanges_with_test_mode = []
            for exchange in list_of_exchanges:
                initiate_exchange = getattr(non_async_ccxt, exchange)
                exchange_class = initiate_exchange({
                    'id': exchange,
                    'enableRateLimit': True
                })
                if 'test' in exchange_class.urls:
                    list_of_exchanges_with_test_mode.append(exchange)
            return list_of_exchanges_with_test_mode
        return non_async_ccxt.exchanges
    except (ccxt.ArgumentsRequired, ccxt.BadRequest) as exception:
        raise BadRequest(exception)
    except (ccxt.InvalidOrder, ccxt.OrderNotFound, ccxt.OrderNotCached,
            ccxt.CancelPending, ccxt.OrderImmediatelyFillable,
            ccxt.OrderNotFillable, ccxt.DuplicateOrderId) as exception:
        raise OrderError(exception)
    except (ccxt.InsufficientFunds, ccxt.InvalidAddress, ccxt.AddressPending,
            ccxt.AccountSuspended) as exception:
        raise AccountError(exception)
    except (ccxt.AuthenticationError, ccxt.PermissionDenied) as exception:
        raise AuthtError(exception)
    except (ccxt.BadResponse, ccxt.NullResponse) as exception:
        raise ResponseError(exception)
    except ccxt.NetworkError as exception:
        raise NetworkError(exception)
    except ccxt.ExchangeError as exception:
        raise ExchangeError(exception)
    except Exception as exception:
        raise exception


def ExchangeStructure(exchange: str) -> dict:
    """Get the structure of an exchange"""
    try:
        initiate_exchange = getattr(non_async_ccxt, exchange)
        exchange_class = initiate_exchange({
            'id': exchange,
            'enableRateLimit': True
        })
        return str(exchange_class.__dict__)
    except (ccxt.ArgumentsRequired, ccxt.BadRequest) as exception:
        raise BadRequest(exception)
    except (ccxt.InvalidOrder, ccxt.OrderNotFound, ccxt.OrderNotCached,
            ccxt.CancelPending, ccxt.OrderImmediatelyFillable,
            ccxt.OrderNotFillable, ccxt.DuplicateOrderId) as exception:
        raise OrderError(exception)
    except (ccxt.InsufficientFunds, ccxt.InvalidAddress, ccxt.AddressPending,
            ccxt.AccountSuspended) as exception:
        raise AccountError(exception)
    except (ccxt.AuthenticationError, ccxt.PermissionDenied) as exception:
        raise AuthtError(exception)
    except (ccxt.BadResponse, ccxt.NullResponse) as exception:
        raise ResponseError(exception)
    except ccxt.NetworkError as exception:
        raise NetworkError(exception)
    except ccxt.ExchangeError as exception:
        raise ExchangeError(exception)
    except Exception as exception:
        raise exception


def ExchangeAttribute(exchange: str, attribute: str) -> dict:
    """Get an attribute of the given exchange"""
    try:
        initiate_exchange = getattr(non_async_ccxt, exchange)
        exchange_class = initiate_exchange({
            'id': exchange,
            'enableRateLimit': True
        })
        exchange_attr = getattr(exchange_class, attribute)
        return exchange_attr
    except (ccxt.ArgumentsRequired, ccxt.BadRequest) as exception:
        raise BadRequest(exception)
    except (ccxt.InvalidOrder, ccxt.OrderNotFound, ccxt.OrderNotCached,
            ccxt.CancelPending, ccxt.OrderImmediatelyFillable,
            ccxt.OrderNotFillable, ccxt.DuplicateOrderId) as exception:
        raise OrderError(exception)
    except (ccxt.InsufficientFunds, ccxt.InvalidAddress, ccxt.AddressPending,
            ccxt.AccountSuspended) as exception:
        raise AccountError(exception)
    except (ccxt.AuthenticationError, ccxt.PermissionDenied) as exception:
        raise AuthtError(exception)
    except (ccxt.BadResponse, ccxt.NullResponse) as exception:
        raise ResponseError(exception)
    except ccxt.NetworkError as exception:
        raise NetworkError(exception)
    except ccxt.ExchangeError as exception:
        raise ExchangeError(exception)
    except Exception as exception:
        raise exception


async def ExchangeMarkets(exchange: str, rate_limit: str) -> dict:
    """Get all the markets on the given exchange"""
    try:
        init_exchange = getattr(ccxt, exchange)
        exchange_class = init_exchange({
            'id': exchange,
            'enableRateLimit': rate_limit
        })
        data = await exchange_class.loadMarkets(True)
        await exchange_class.close()
        return data
    except (ccxt.ArgumentsRequired, ccxt.BadRequest) as exception:
        exchange_class.close()
        raise BadRequest(exception)
    except (ccxt.InvalidOrder, ccxt.OrderNotFound, ccxt.OrderNotCached,
            ccxt.CancelPending, ccxt.OrderImmediatelyFillable,
            ccxt.OrderNotFillable, ccxt.DuplicateOrderId) as exception:
        exchange_class.close()
        raise OrderError(exception)
    except (ccxt.InsufficientFunds, ccxt.InvalidAddress, ccxt.AddressPending,
            ccxt.AccountSuspended) as exception:
        exchange_class.close()
        raise AccountError(exception)
    except (ccxt.AuthenticationError, ccxt.PermissionDenied) as exception:
        exchange_class.close()
        raise AuthtError(exception)
    except (ccxt.BadResponse, ccxt.NullResponse) as exception:
        exchange_class.close()
        raise ResponseError(exception)
    except ccxt.NetworkError as exception:
        exchange_class.close()
        raise NetworkError(exception)
    except ccxt.ExchangeError as exception:
        exchange_class.close()
        raise ExchangeError(exception)
    except Exception as exception:
        exchange_class.close()
        raise exception


async def MarketStructure(symbol: str, exchange: str, rate_limit: str) -> dict:
    """Get market structure of a symbol"""
    try:
        init_exchange = getattr(ccxt, exchange)
        exchange_class = init_exchange({
            'id': exchange,
            'enableRateLimit': rate_limit
        })
        data = await exchange_class.loadMarkets(True)
        await exchange_class.close()
        return data[symbol]
    except (ccxt.ArgumentsRequired, ccxt.BadRequest) as exception:
        exchange_class.close()
        raise BadRequest(exception)
    except (ccxt.InvalidOrder, ccxt.OrderNotFound, ccxt.OrderNotCached,
            ccxt.CancelPending, ccxt.OrderImmediatelyFillable,
            ccxt.OrderNotFillable, ccxt.DuplicateOrderId) as exception:
        exchange_class.close()
        raise OrderError(exception)
    except (ccxt.InsufficientFunds, ccxt.InvalidAddress, ccxt.AddressPending,
            ccxt.AccountSuspended) as exception:
        exchange_class.close()
        raise AccountError(exception)
    except (ccxt.AuthenticationError, ccxt.PermissionDenied) as exception:
        exchange_class.close()
        raise AuthtError(exception)
    except (ccxt.BadResponse, ccxt.NullResponse) as exception:
        exchange_class.close()
        raise ResponseError(exception)
    except ccxt.NetworkError as exception:
        exchange_class.close()
        raise NetworkError(exception)
    except ccxt.ExchangeError as exception:
        exchange_class.close()
        raise ExchangeError(exception)
    except Exception as exception:
        exchange_class.close()
        raise exception


async def getCurrencies(exchange: str, rate_limit: str) -> dict:
    """Get currencies on an exchange"""
    try:
        init_exchange = getattr(ccxt, exchange)
        exchange_class = init_exchange({
            'id': exchange,
            'enableRateLimit': rate_limit
        })
        if exchange_class.has['fetchCurrencies']:
            data = await exchange_class.fetchCurrencies()
            await exchange_class.close()
            return data
        await exchange_class.close()
        raise FunctionalityNotSupported(
            "Functionality not available for this exchange.")
    except (ccxt.ArgumentsRequired, ccxt.BadRequest) as exception:
        exchange_class.close()
        raise BadRequest(exception)
    except (ccxt.InvalidOrder, ccxt.OrderNotFound, ccxt.OrderNotCached,
            ccxt.CancelPending, ccxt.OrderImmediatelyFillable,
            ccxt.OrderNotFillable, ccxt.DuplicateOrderId) as exception:
        exchange_class.close()
        raise OrderError(exception)
    except (ccxt.InsufficientFunds, ccxt.InvalidAddress, ccxt.AddressPending,
            ccxt.AccountSuspended) as exception:
        exchange_class.close()
        raise AccountError(exception)
    except (ccxt.AuthenticationError, ccxt.PermissionDenied) as exception:
        exchange_class.close()
        raise AuthtError(exception)
    except (ccxt.BadResponse, ccxt.NullResponse) as exception:
        exchange_class.close()
        raise ResponseError(exception)
    except ccxt.NetworkError as exception:
        exchange_class.close()
        raise NetworkError(exception)
    except ccxt.ExchangeError as exception:
        exchange_class.close()
        raise ExchangeError(exception)
    except Exception as exception:
        exchange_class.close()
        raise exception


async def latestPriceInfo(symbol: str, exchange: str, rate_limit: str) -> dict:
    """Get latest price info of a symbol"""
    try:
        init_exchange = getattr(ccxt, exchange)
        exchange_class = init_exchange({
            'id': exchange,
            'enableRateLimit': rate_limit
        })
        if exchange_class.has['fetchTicker']:
            data = await exchange_class.fetchTicker(symbol)
            await exchange_class.close()
            return data
        await exchange_class.close()
        raise FunctionalityNotSupported(
            "Functionality not available for this exchange.")
    except (ccxt.ArgumentsRequired, ccxt.BadRequest) as exception:
        exchange_class.close()
        raise BadRequest(exception)
    except (ccxt.InvalidOrder, ccxt.OrderNotFound, ccxt.OrderNotCached,
            ccxt.CancelPending, ccxt.OrderImmediatelyFillable,
            ccxt.OrderNotFillable, ccxt.DuplicateOrderId) as exception:
        exchange_class.close()
        raise OrderError(exception)
    except (ccxt.InsufficientFunds, ccxt.InvalidAddress, ccxt.AddressPending,
            ccxt.AccountSuspended) as exception:
        exchange_class.close()
        raise AccountError(exception)
    except (ccxt.AuthenticationError, ccxt.PermissionDenied) as exception:
        exchange_class.close()
        raise AuthtError(exception)
    except (ccxt.BadResponse, ccxt.NullResponse) as exception:
        exchange_class.close()
        raise ResponseError(exception)
    except ccxt.NetworkError as exception:
        exchange_class.close()
        raise NetworkError(exception)
    except ccxt.ExchangeError as exception:
        exchange_class.close()
        raise ExchangeError(exception)
    except Exception as exception:
        exchange_class.close()
        raise exception


async def latestPriceInfoForAllSymbols(exchange: str, rate_limit: str) -> dict:
    """Get latest price info for all symbols on an exchange"""
    try:
        init_exchange = getattr(ccxt, exchange)
        exchange_class = init_exchange({
            'id': exchange,
            'enableRateLimit': rate_limit
        })
        if exchange_class.has['fetchTickers']:
            data = await exchange_class.fetchTickers()
            await exchange_class.close()
            return data
        await exchange_class.close()
        raise FunctionalityNotSupported(
            "Functionality not available for this exchange.")
    except (ccxt.ArgumentsRequired, ccxt.BadRequest) as exception:
        exchange_class.close()
        raise BadRequest(exception)
    except (ccxt.InvalidOrder, ccxt.OrderNotFound, ccxt.OrderNotCached,
            ccxt.CancelPending, ccxt.OrderImmediatelyFillable,
            ccxt.OrderNotFillable, ccxt.DuplicateOrderId) as exception:
        exchange_class.close()
        raise OrderError(exception)
    except (ccxt.InsufficientFunds, ccxt.InvalidAddress, ccxt.AddressPending,
            ccxt.AccountSuspended) as exception:
        exchange_class.close()
        raise AccountError(exception)
    except (ccxt.AuthenticationError, ccxt.PermissionDenied) as exception:
        exchange_class.close()
        raise AuthtError(exception)
    except (ccxt.BadResponse, ccxt.NullResponse) as exception:
        exchange_class.close()
        raise ResponseError(exception)
    except ccxt.NetworkError as exception:
        exchange_class.close()
        raise NetworkError(exception)
    except ccxt.ExchangeError as exception:
        exchange_class.close()
        raise ExchangeError(exception)
    except Exception as exception:
        exchange_class.close()
        raise exception


async def latestTrades(symbol: str, number_of_data_points: int, exchange: str,
                       rate_limit: str) -> dict:
    """Get latest trades"""
    try:
        init_exchange = getattr(ccxt, exchange)
        exchange_class = init_exchange({
            'id': exchange,
            'enableRateLimit': rate_limit
        })
        if exchange_class.has['fetchTrades']:
            data = await exchange_class.fetchTrades(
                symbol, limit=number_of_data_points)
            await exchange_class.close()
            return data
        await exchange_class.close()
        raise FunctionalityNotSupported(
            "Functionality not available for this exchange.")
    except (ccxt.ArgumentsRequired, ccxt.BadRequest) as exception:
        exchange_class.close()
        raise BadRequest(exception)
    except (ccxt.InvalidOrder, ccxt.OrderNotFound, ccxt.OrderNotCached,
            ccxt.CancelPending, ccxt.OrderImmediatelyFillable,
            ccxt.OrderNotFillable, ccxt.DuplicateOrderId) as exception:
        exchange_class.close()
        raise OrderError(exception)
    except (ccxt.InsufficientFunds, ccxt.InvalidAddress, ccxt.AddressPending,
            ccxt.AccountSuspended) as exception:
        exchange_class.close()
        raise AccountError(exception)
    except (ccxt.AuthenticationError, ccxt.PermissionDenied) as exception:
        exchange_class.close()
        raise AuthtError(exception)
    except (ccxt.BadResponse, ccxt.NullResponse) as exception:
        exchange_class.close()
        raise ResponseError(exception)
    except ccxt.NetworkError as exception:
        exchange_class.close()
        raise NetworkError(exception)
    except ccxt.ExchangeError as exception:
        exchange_class.close()
        raise ExchangeError(exception)
    except Exception as exception:
        exchange_class.close()
        raise exception


async def getOHLCV(symbol: str, start: str, end: str, interval: str,
                   exchange: str, dataframe: bool, rate_limit: str) -> list:
    """Get latest trades"""
    try:
        init_exchange = getattr(ccxt, exchange)
        exchange_class = init_exchange({
            'id': exchange,
            'enableRateLimit': rate_limit,
            'options': {
                'fetchOHLCVWarning': False
            }
        })
        if interval not in exchange_class.timeframes:
            raise InvlaidTimeInterval(
                "Time interval not supported by this exchange")
        if exchange_class.has['fetchOHLCV']:
            if interval in ["1d", "1w", "1M"]:
                converted_start = datetime.datetime.strptime(start, '%Y-%m-%d')
                converted_end = datetime.datetime.strptime(end, '%Y-%m-%d')
                date_time_diff = converted_end - converted_start
                interval_value = {'1d': 1, "1w": 7, "1M": 30}
                limit = int(date_time_diff.days) / int(
                    interval_value[interval]) + 1
                since = int(converted_start.timestamp() * 1000)
            elif interval in ["1m", "5m", "15m", "30m", "1h"]:
                converted_start = datetime.datetime.strptime(
                    start, '%Y-%m-%d %H:%M:%S')
                converted_end = datetime.datetime.strptime(
                    end, '%Y-%m-%d %H:%M:%S')
                date_time_diff = converted_end - converted_start
                interval_value = {
                    '1m': 1,
                    "5m": 5,
                    "15m": 15,
                    "30m": 30,
                    "1h": 60
                }
                limit = int(date_time_diff // datetime.timedelta(
                    minutes=1)) / int(interval_value[interval]) + 1
                since = int(converted_start.timestamp() * 1000)
            else:
                InvalidTimeInterval("Invalid Time Interval")
        data = await exchange_class.fetchOHLCV(symbol, interval, since,
                                               int(limit))
        final_list = []
        for values in range(len(data)):
            converted_date = float(data[values][0]) / 1000.0
            new_date = datetime.datetime.fromtimestamp(
                converted_date).strftime("%Y-%m-%d %H:%M:%S")
            new_list = {
                'time': new_date,
                'open': data[values][1],
                'high': data[values][2],
                'low': data[values][3],
                'close': data[values][4],
                'volume': data[values][5]
            }
            final_list.append(new_list)
        await exchange_class.close()
        if dataframe:
            import pandas
            columns = ['time', 'open', 'high', 'low', 'close', 'volume']
            df = pandas.DataFrame(final_list, columns=columns)
            df['datetime'] = pandas.to_datetime(df['time'])
            df.set_index(['datetime'], inplace=True)
            del df['time']
            return df
        return final_list
        raise FunctionalityNotSupported(
            "Functionality not available for this exchange.")
    except (ccxt.ArgumentsRequired, ccxt.BadRequest) as exception:
        exchange_class.close()
        raise BadRequest(exception)
    except (ccxt.InvalidOrder, ccxt.OrderNotFound, ccxt.OrderNotCached,
            ccxt.CancelPending, ccxt.OrderImmediatelyFillable,
            ccxt.OrderNotFillable, ccxt.DuplicateOrderId) as exception:
        raise OrderError(exception)
    except (ccxt.InsufficientFunds, ccxt.InvalidAddress, ccxt.AddressPending,
            ccxt.AccountSuspended) as exception:
        exchange_class.close()
        raise AccountError(exception)
    except (ccxt.AuthenticationError, ccxt.PermissionDenied) as exception:
        exchange_class.close()
        raise AuthtError(exception)
    except (ccxt.BadResponse, ccxt.NullResponse) as exception:
        exchange_class.close()
        raise ResponseError(exception)
    except ccxt.NetworkError as exception:
        exchange_class.close()
        raise NetworkError(exception)
    except ccxt.ExchangeError as exception:
        exchange_class.close()
        raise ExchangeError(exception)
    except Exception as exception:
        exchange_class.close()
        raise exception


async def getLatestEntryOrderBook(symbol: str, number_of_data_points: int,
                                  exchange: str, rate_limit: str) -> dict:
    """Get order book"""
    try:
        init_exchange = getattr(ccxt, exchange)
        exchange_class = init_exchange({
            'id': exchange,
            'enableRateLimit': rate_limit
        })
        if exchange_class.has['fetchOrderBook']:
            data = await exchange_class.fetchOrderBook(
                symbol, limit=number_of_data_points)
            await exchange_class.close()
            return data
        raise FunctionalityNotSupported(
            "Functionality not available for this exchange.")
    except (ccxt.ArgumentsRequired, ccxt.BadRequest) as exception:
        exchange_class.close()
        raise BadRequest(exception)
    except (ccxt.InvalidOrder, ccxt.OrderNotFound, ccxt.OrderNotCached,
            ccxt.CancelPending, ccxt.OrderImmediatelyFillable,
            ccxt.OrderNotFillable, ccxt.DuplicateOrderId) as exception:
        exchange_class.close()
        raise OrderError(exception)
    except (ccxt.InsufficientFunds, ccxt.InvalidAddress, ccxt.AddressPending,
            ccxt.AccountSuspended) as exception:
        exchange_class.close()
        raise AccountError(exception)
    except (ccxt.AuthenticationError, ccxt.PermissionDenied) as exception:
        exchange_class.close()
        raise AuthtError(exception)
    except (ccxt.BadResponse, ccxt.NullResponse) as exception:
        exchange_class.close()
        raise ResponseError(exception)
    except ccxt.NetworkError as exception:
        exchange_class.close()
        raise NetworkError(exception)
    except ccxt.ExchangeError as exception:
        exchange_class.close()
        raise ExchangeError(exception)
    except Exception as exception:
        exchange_class.close()
        raise exception


async def getLatestEntryOrderBookL2(symbol: str, number_of_data_points: int,
                                    exchange: str, rate_limit: str) -> dict:
    """Get order book"""
    try:
        init_exchange = getattr(ccxt, exchange)
        exchange_class = init_exchange({
            'id': exchange,
            'enableRateLimit': rate_limit
        })
        if exchange_class.has['fetchL2OrderBook']:
            data = await exchange_class.fetchL2OrderBook(
                symbol, limit=number_of_data_points)
            await exchange_class.close()
            return data
        raise FunctionalityNotSupported(
            "Functionality not available for this exchange.")
    except (ccxt.ArgumentsRequired, ccxt.BadRequest) as exception:
        exchange_class.close()
        raise BadRequest(exception)
    except (ccxt.InvalidOrder, ccxt.OrderNotFound, ccxt.OrderNotCached,
            ccxt.CancelPending, ccxt.OrderImmediatelyFillable,
            ccxt.OrderNotFillable, ccxt.DuplicateOrderId) as exception:
        exchange_class.close()
        raise OrderError(exception)
    except (ccxt.InsufficientFunds, ccxt.InvalidAddress, ccxt.AddressPending,
            ccxt.AccountSuspended) as exception:
        exchange_class.close()
        raise AccountError(exception)
    except (ccxt.AuthenticationError, ccxt.PermissionDenied) as exception:
        exchange_class.close()
        raise AuthtError(exception)
    except (ccxt.BadResponse, ccxt.NullResponse) as exception:
        exchange_class.close()
        raise ResponseError(exception)
    except ccxt.NetworkError as exception:
        exchange_class.close()
        raise NetworkError(exception)
    except ccxt.ExchangeError as exception:
        exchange_class.close()
        raise ExchangeError(exception)
    except Exception as exception:
        exchange_class.close()
        raise exception
