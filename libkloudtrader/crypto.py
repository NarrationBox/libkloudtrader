"""Trading and Data APIs for Crypto Currencies"""
import requests
import os
from typing import Any
import datetime
import pandas
import asyncio
from libkloudtrader.exceptions import BadRequest, InvalidCredentials
from libkloudtrader.logs import start_logger
from libkloudtrader.crypto_operations import *
"""Config starts"""

logger = start_logger(__name__)

CRYPTO_EXCHANGE = os.environ['CRYPTO_EXCHANGE']
CRYPTO_API_KEY = os.environ['CRYPTO_API_KEY']
CRYPTO_API_SECRET = os.environ['CRYPTO_API_SECRET']
CRYPTO_API_PASSWORD = os.environ['CRYPTO_API_PASSWORD']
CRYPTO_API_UID = os.environ['CRYPTO_API_UID']
CRYPTO_URL_LIVE = "https://api.kloudtrader.com/crypto/live"
CRYPTO_URL_TEST = "https://api.kloudtrader.com/crypto/test"


def crypto_get_headers(api_key, api_secret, exchange_password, exchange_uid):
    headers = {
        'X-API-KEY': api_key,
        'X-API-SECRET': api_secret,
        'X-EXCHANGE-PASSWORD': exchange_password,
        'X-EXCHANGE-UID': exchange_uid
    }
    return headers


"""Config ends"""
"""Data APis start"""


def list_of_exchanges(test_mode: bool = False) -> list:
    """Get List of Exchanges available"""
    try:
        return ListOfExchanges(test_mode=test_mode)
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def exchange_structure(exchange: str = CRYPTO_EXCHANGE) -> dict:
    """No Docs needed. Get the structure of an exchange"""
    try:
        check_exchange_existence(exchange=exchange)
        return ExchangeStructure(exchange=exchange)
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def exchange_attribute(attribute: str,
                       exchange: str = CRYPTO_EXCHANGE) -> dict:
    """No Docs needed. Return asked attribute of the given exchange"""
    try:
        check_exchange_existence(exchange=exchange)
        return ExchangeAttribute(attribute=attribute, exchange=exchange)
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def markets(exchange: str = CRYPTO_EXCHANGE, rate_limit: bool = True) -> dict:
    """Get all the markets available in the exchange and their market structures"""
    try:
        check_exchange_existence(exchange=exchange)
        return asyncio.get_event_loop().run_until_complete(
            ExchangeMarkets(exchange=exchange, rate_limit=rate_limit))
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def market_structure(symbol: str,
                     exchange: str = CRYPTO_EXCHANGE,
                     rate_limit: bool = True) -> dict:
    """Get the market structure of a particular symbol"""
    try:
        check_exchange_existence(exchange=exchange)
        return asyncio.get_event_loop().run_until_complete(
            MarketStructure(symbol=symbol,
                            exchange=exchange,
                            rate_limit=rate_limit))
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def latest_price_info(symbol: str,
                      exchange: str = CRYPTO_EXCHANGE,
                      rate_limit: bool = True) -> dict:
    """Get quotes/ticker data for a given symbool from the given exchange"""
    try:
        check_exchange_existence(exchange=exchange)
        return asyncio.get_event_loop().run_until_complete(
            latestPriceInfo(symbol=symbol,
                            exchange=exchange,
                            rate_limit=rate_limit))
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def latest_price_info_for_all_symbols(exchange: str = CRYPTO_EXCHANGE,
                                      rate_limit: bool = True) -> dict:
    """Get quotes/ticker data for all symbols listed on an exchange"""
    try:
        check_exchange_existence(exchange=exchange)
        return asyncio.get_event_loop().run_until_complete(
            latestPriceInfoForAllSymbols(exchange=exchange,
                                         rate_limit=rate_limit))
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def ohlcv(symbol: str,
          start: Any,
          end: Any,
          interval: str = "1d",
          exchange: str = CRYPTO_EXCHANGE,
          dataframe: bool = True,
          rate_limit: bool = True) -> dict:
    """Get OHLCV/bar data. 
    Most exchanges don't go very back in time. 
    The very few that go need pagination which will be released soon. 
    Some exchanges return data for today only if interval is very less like 1m, 5m, etc.
    Supported time interval: ["1m","5m","15m","30m","1h","1d","1w","1M"]
    %Y-%m-%d date format for "1d","1w","1M" and %Y-%m-%d %H:%M:%S for others
    """
    try:
        check_exchange_existence(exchange=exchange)
        return asyncio.get_event_loop().run_until_complete(
            getOHLCV(symbol=symbol,
                     start=start,
                     end=end,
                     interval=interval,
                     exchange=exchange,
                     dataframe=dataframe,
                     rate_limit=rate_limit))
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def trades(symbol: str,
           number_of_data_points: int = 1,
           exchange: str = CRYPTO_EXCHANGE,
           rate_limit: bool = True):
    """Get recent trades for a particular trading symbol."""
    try:
        check_exchange_existence(exchange=exchange)
        return asyncio.get_event_loop().run_until_complete(
            latestTrades(symbol=symbol,
                         number_of_data_points=number_of_data_points,
                         exchange=exchange,
                         rate_limit=rate_limit))
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def latest_order_book_entry(symbol: str,
                            exchange: str = CRYPTO_EXCHANGE,
                            rate_limit: bool = True):
    """Get latest orderbook entry for a particular market trading symbol."""
    try:
        check_exchange_existence(exchange=exchange)
        response = asyncio.get_event_loop().run_until_complete(
            getOrderBook(symbol=symbol,
                         number_of_data_points=1,
                         exchange=exchange,
                         rate_limit=rate_limit))
        latest_orderbook_entry_dict = {}
        latest_orderbook_entry_dict['symbol'] = symbol
        latest_orderbook_entry_dict['ask'] = response['asks'][0][0] if len(
            response['asks']) > 0 else None
        latest_orderbook_entry_dict['asksize'] = response['asks'][0][1] if len(
            response['asks']) > 0 else None
        latest_orderbook_entry_dict['bid'] = response['bids'][0][0] if len(
            response['bids']) > 0 else None
        latest_orderbook_entry_dict['bidsize'] = response['bids'][0][1] if len(
            response['bids']) > 0 else None
        latest_orderbook_entry_dict['datetime'] = response['datetime']
        latest_orderbook_entry_dict['nonce'] = response['nonce']
        return latest_orderbook_entry_dict
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def latest_L2_order_book_entry(symbol: str,
                               exchange: str = CRYPTO_EXCHANGE,
                               rate_limit: bool = True):
    """Get latest orderbook entry for a particular market trading symbol."""
    try:
        check_exchange_existence(exchange=exchange)
        response = asyncio.get_event_loop().run_until_complete(
            getOrderBookL2(symbol=symbol,
                           number_of_data_points=1,
                           exchange=exchange,
                           rate_limit=rate_limit))
        latest_orderbook_entry_dict = {}
        latest_orderbook_entry_dict['symbol'] = symbol
        latest_orderbook_entry_dict['ask'] = response['asks'][0][0] if len(
            response['asks']) > 0 else None
        latest_orderbook_entry_dict['asksize'] = response['asks'][0][1] if len(
            response['asks']) > 0 else None
        latest_orderbook_entry_dict['bid'] = response['bids'][0][0] if len(
            response['bids']) > 0 else None
        latest_orderbook_entry_dict['bidsize'] = response['bids'][0][1] if len(
            response['bids']) > 0 else None
        latest_orderbook_entry_dict['datetime'] = response['datetime']
        latest_orderbook_entry_dict['nonce'] = response['nonce']
        return latest_orderbook_entry_dict
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def order_book(symbol: str,
               number_of_data_points: int = 1,
               exchange: str = CRYPTO_EXCHANGE,
               rate_limit: bool = True):
    """Get order book for a particular symbol."""
    try:
        check_exchange_existence(exchange=exchange)
        return asyncio.get_event_loop().run_until_complete(
            getOrderBook(symbol=symbol,
                         number_of_data_points=number_of_data_points,
                         exchange=exchange,
                         rate_limit=rate_limit))
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def L2_order_book(symbol: str,
                  number_of_data_points: int = 1,
                  exchange: str = CRYPTO_EXCHANGE,
                  rate_limit: bool = True):
    """Level 2 (price-aggregated) order book for a particular symbol."""
    try:
        check_exchange_existence(exchange=exchange)
        return asyncio.get_event_loop().run_until_complete(
            getOrderBookL2(symbol=symbol,
                           number_of_data_points=number_of_data_points,
                           exchange=exchange,
                           rate_limit=rate_limit))
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def currencies(exchange: str = CRYPTO_EXCHANGE,
               rate_limit: bool = True) -> dict:
    """Get all Currencies available on an exchange"""
    try:
        check_exchange_existence(exchange=exchange)
        return asyncio.get_event_loop().run_until_complete(
            getCurrencies(exchange=exchange, rate_limit=rate_limit))
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


"""Data APis end"""
"""User APIs start"""


def user_balance(exchange: str = CRYPTO_EXCHANGE,
                 api_key: str = CRYPTO_API_KEY,
                 api_secret: str = CRYPTO_API_SECRET,
                 exchange_password: Any = CRYPTO_API_PASSWORD,
                 exchange_uid: Any = CRYPTO_API_UID,
                 test_mode: bool = False) -> Any:
    """Get your account balance"""
    try:
        if test_mode == True:
            url = CRYPTO_URL_TEST
        else:
            url = CRYPTO_URL_LIVE
        response = requests.post('{}/balance/{}'.format(url, exchange),
                                 headers=crypto_get_headers(
                                     api_key, api_secret, exchange_password,
                                     exchange_uid))
        if response:
            return response.json()
        if response.status_code == 400:
            logger.error('Oops! An error Occurred ⚠️')
            raise BadRequest(response.text)
        if response.status_code == 401:
            logger.error('Oops! An error Occurred ⚠️')
            raise InvalidCredentials(response.text)
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def user_ledger(currency_code: str,
                exchange: str = CRYPTO_EXCHANGE,
                api_key: str = CRYPTO_API_KEY,
                api_secret: str = CRYPTO_API_SECRET,
                exchange_password: Any = CRYPTO_API_PASSWORD,
                exchange_uid: Any = CRYPTO_API_UID,
                test_mode: bool = False) -> Any:
    """Get your latest ledger history"""
    try:
        if test_mode == True:
            url = CRYPTO_URL_TEST
        else:
            url = CRYPTO_URL_LIVE
        payload = {'currency_code': currency_code}
        response = requests.post('{}/ledger/{}'.format(url, exchange),
                                 headers=crypto_get_headers(
                                     api_key, api_secret, exchange_password,
                                     exchange_uid),
                                 json=payload)
        if response:
            return response.json()
        if response.status_code == 400:
            logger.error('Oops! An error Occurred ⚠️')
            raise BadRequest(response.text)
        if response.status_code == 401:
            logger.error('Oops! An error Occurred ⚠️')
            raise InvalidCredentials(response.text)
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def user_trades(symbol: str,
                exchange: str = CRYPTO_EXCHANGE,
                api_key: str = CRYPTO_API_KEY,
                api_secret: str = CRYPTO_API_SECRET,
                exchange_password: Any = CRYPTO_API_PASSWORD,
                exchange_uid: Any = CRYPTO_API_UID,
                test_mode: bool = False):
    """Get your trades"""
    try:
        if test_mode == True:
            url = CRYPTO_URL_TEST
        else:
            url = CRYPTO_URL_LIVE
        payload = {'symbol': symbol.upper(), 'start': "", 'end': ""}
        response = requests.post('{}/my_trades/{}'.format(url, exchange),
                                 headers=crypto_get_headers(
                                     api_key, api_secret, exchange_password,
                                     exchange_uid),
                                 json=payload)
        if response:
            return response.json()
        if response.status_code == 400:
            logger.error('Oops! An error Occurred ⚠️')
            raise BadRequest(response.text)
        if response.status_code == 401:
            logger.error('Oops! An error Occurred ⚠️')
            raise InvalidCredentials(response.text)
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def user_closed_orders(symbol: str,
                       exchange: str = CRYPTO_EXCHANGE,
                       api_key: str = CRYPTO_API_KEY,
                       api_secret: str = CRYPTO_API_SECRET,
                       exchange_password: Any = CRYPTO_API_PASSWORD,
                       exchange_uid: Any = CRYPTO_API_UID,
                       test_mode: bool = False) -> Any:
    """Get all of your closed orders"""
    try:
        if test_mode == True:
            url = CRYPTO_URL_TEST
        else:
            url = CRYPTO_URL_LIVE
        payload = {'symbol': symbol.upper(), 'start': "", 'end': ""}
        response = requests.post('{}/closed_orders/{}'.format(url, exchange),
                                 headers=crypto_get_headers(
                                     api_key, api_secret, exchange_password,
                                     exchange_uid),
                                 json=payload)
        if response:
            return response.json()
        if response.status_code == 400:
            logger.error('Oops! An error Occurred ⚠️')
            raise BadRequest(response.text)
        if response.status_code == 401:
            logger.error('Oops! An error Occurred ⚠️')
            raise InvalidCredentials(response.text)
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def get_order(order_id: str,
              symbol: str,
              exchange: str = CRYPTO_EXCHANGE,
              api_key: str = CRYPTO_API_KEY,
              api_secret: str = CRYPTO_API_SECRET,
              exchange_password: Any = CRYPTO_API_PASSWORD,
              exchange_uid: Any = CRYPTO_API_UID,
              test_mode: bool = False) -> Any:
    """Get information about a specific order"""
    try:
        if test_mode == True:
            url = CRYPTO_URL_TEST
        else:
            url = CRYPTO_URL_LIVE
        payload = {'order_id': str(order_id), 'symbol': symbol.upper()}
        response = requests.post('{}/get_order/{}'.format(url, exchange),
                                 headers=crypto_get_headers(
                                     api_key, api_secret, exchange_password,
                                     exchange_uid),
                                 json=payload)
        if response:
            return response.json()
        if response.status_code == 400:
            logger.error('Oops! An error Occurred ⚠️')
            raise BadRequest(response.text)
        if response.status_code == 401:
            logger.error('Oops! An error Occurred ⚠️')
            raise InvalidCredentials(response.text)
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def user_orders(symbol: str,
                exchange: str = CRYPTO_EXCHANGE,
                api_key: str = CRYPTO_API_KEY,
                api_secret: str = CRYPTO_API_SECRET,
                exchange_password: Any = CRYPTO_API_PASSWORD,
                exchange_uid: Any = CRYPTO_API_UID,
                test_mode: bool = False) -> Any:
    """Get all of your orders"""
    try:
        if test_mode == True:
            url = CRYPTO_URL_TEST
        else:
            url = CRYPTO_URL_LIVE
        payload = {'symbol': symbol.upper(), 'start': "", 'end': ""}
        response = requests.post('{}/get_orders/{}'.format(url, exchange),
                                 headers=crypto_get_headers(
                                     api_key, api_secret, exchange_password,
                                     exchange_uid),
                                 json=payload)
        if response:
            return response.json()
        if response.status_code == 400:
            logger.error('Oops! An error Occurred ⚠️')
            raise BadRequest(response.text)
        if response.status_code == 401:
            logger.error('Oops! An error Occurred ⚠️')
            raise InvalidCredentials(response.text)
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def user_positions(exchange: str = CRYPTO_EXCHANGE,
                   api_key: str = CRYPTO_API_KEY,
                   api_secret: str = CRYPTO_API_SECRET,
                   exchange_password: Any = CRYPTO_API_PASSWORD,
                   exchange_uid: Any = CRYPTO_API_UID,
                   test_mode: bool = False) -> Any:
    """get your positions"""
    try:
        if test_mode == True:
            url = CRYPTO_URL_TEST
        else:
            url = CRYPTO_URL_LIVE
        response = requests.post('{}/positions/{}'.format(url, exchange),
                                 headers=crypto_get_headers(
                                     api_key, api_secret, exchange_password,
                                     exchange_uid))
        if response:
            return response.json()
        if response.status_code == 400:
            logger.error('Oops! An error Occurred ⚠️')
            raise BadRequest(response.text)
        if response.status_code == 401:
            logger.error('Oops! An error Occurred ⚠️')
            raise InvalidCredentials(response.text)
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def create_deposit_address(currency_code: str,
                           exchange: str = CRYPTO_EXCHANGE,
                           api_key: str = CRYPTO_API_KEY,
                           api_secret: str = CRYPTO_API_SECRET,
                           exchange_password: Any = CRYPTO_API_PASSWORD,
                           exchange_uid: Any = CRYPTO_API_UID,
                           test_mode: bool = False) -> Any:
    """Not in docs yet. Needs to be tested. Create a deposit address"""
    try:
        if test_mode == True:
            url = CRYPTO_URL_TEST
        else:
            url = CRYPTO_URL_LIVE
        payload = {'currency_code': currency_code}
        response = requests.post(
            '{}/create_deposit_address/{}'.format(url, exchange),
            headers=crypto_get_headers(api_key, api_secret, exchange_password,
                                       exchange_uid),
            json=payload)
        if response:
            return response.json()
        if response.status_code == 400:
            logger.error('Oops! An error Occurred ⚠️')
            raise BadRequest(response.text)
        if response.status_code == 401:
            logger.error('Oops! An error Occurred ⚠️')
            raise InvalidCredentials(response.text)
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def user_deposits(currency_code: str,
                  exchange: str = CRYPTO_EXCHANGE,
                  api_key: str = CRYPTO_API_KEY,
                  api_secret: str = CRYPTO_API_SECRET,
                  exchange_password: Any = CRYPTO_API_PASSWORD,
                  exchange_uid: Any = CRYPTO_API_UID,
                  test_mode: bool = False) -> Any:
    """Not in docs yet. Needs to be tested.Get your Deposits"""
    try:
        if test_mode == True:
            url = CRYPTO_URL_TEST
        else:
            url = CRYPTO_URL_LIVE
        payload = {'currency_code': currency_code}
        response = requests.post('{}/deposits/{}'.format(url, exchange),
                                 headers=crypto_get_headers(
                                     api_key, api_secret, exchange_password,
                                     exchange_uid),
                                 json=payload)
        if response:
            return response.json()
        if response.status_code == 400:
            logger.error('Oops! An error Occurred ⚠️')
            raise BadRequest(response.text)
        if response.status_code == 401:
            logger.error('Oops! An error Occurred ⚠️')
            raise InvalidCredentials(response.text)
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def user_deposit_address(currency_code: str,
                         exchange: str = CRYPTO_EXCHANGE,
                         api_key: str = CRYPTO_API_KEY,
                         api_secret: str = CRYPTO_API_SECRET,
                         exchange_password: Any = CRYPTO_API_PASSWORD,
                         exchange_uid: Any = CRYPTO_API_UID,
                         test_mode: bool = False) -> Any:
    """Not in docs yet. Needs to be tested.Get your Deposit addresses"""
    try:
        if test_mode == True:
            url = CRYPTO_URL_TEST
        else:
            url = CRYPTO_URL_LIVE
        payload = {'currency_code': currency_code}
        response = requests.post('{}/deposit_address/{}'.format(url, exchange),
                                 headers=crypto_get_headers(
                                     api_key, api_secret, exchange_password,
                                     exchange_uid),
                                 json=payload)
        if response:
            return response.json()
        if response.status_code == 400:
            logger.error('Oops! An error Occurred ⚠️')
            raise BadRequest(response.text)
        if response.status_code == 401:
            logger.error('Oops! An error Occurred ⚠️')
            raise InvalidCredentials(response.text)
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def user_withdrawls(currency_code: str,
                    exchange: str = CRYPTO_EXCHANGE,
                    api_key: str = CRYPTO_API_KEY,
                    api_secret: str = CRYPTO_API_SECRET,
                    exchange_password: Any = CRYPTO_API_PASSWORD,
                    exchange_uid: Any = CRYPTO_API_UID,
                    test_mode: bool = False) -> Any:
    """Not in docs yet. Needs to be tested.Get your withdrawls"""
    try:
        if test_mode == True:
            url = CRYPTO_URL_TEST
        else:
            url = CRYPTO_URL_LIVE
        payload = {'currency_code': currency_code}
        response = requests.post('{}/withdrawls/{}'.format(url, exchange),
                                 headers=crypto_get_headers(
                                     api_key, api_secret, exchange_password,
                                     exchange_uid),
                                 json=payload)
        if response:
            return response.json()
        if response.status_code == 400:
            logger.error('Oops! An error Occurred ⚠️')
            raise BadRequest(response.text)
        if response.status_code == 401:
            logger.error('Oops! An error Occurred ⚠️')
            raise InvalidCredentials(response.text)
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def user_transactions(currency_code: str,
                      exchange: str = CRYPTO_EXCHANGE,
                      api_key: str = CRYPTO_API_KEY,
                      api_secret: str = CRYPTO_API_SECRET,
                      exchange_password: Any = CRYPTO_API_PASSWORD,
                      exchange_uid: Any = CRYPTO_API_UID,
                      test_mode: bool = False) -> Any:
    """Get your transactions"""
    try:
        if test_mode == True:
            url = CRYPTO_URL_TEST
        else:
            url = CRYPTO_URL_LIVE
        payload = {'currency_code': currency_code}
        response = requests.post('{}/transactions/{}'.format(url, exchange),
                                 headers=crypto_get_headers(
                                     api_key, api_secret, exchange_password,
                                     exchange_uid),
                                 json=payload)
        if response:
            return response.json()
        if response.status_code == 400:
            logger.error('Oops! An error Occurred ⚠️')
            raise BadRequest(response.text)
        if response.status_code == 401:
            logger.error('Oops! An error Occurred ⚠️')
            raise InvalidCredentials(response.text)
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


'''User APIs end'''
'''Trading APIs begin'''


def buy(symbol: str,
        quantity: Any,
        order_type: str = "market",
        price: Any = None,
        exchange: str = CRYPTO_EXCHANGE,
        api_key: str = CRYPTO_API_KEY,
        api_secret: str = CRYPTO_API_SECRET,
        exchange_password: Any = CRYPTO_API_PASSWORD,
        exchange_uid: Any = CRYPTO_API_UID,
        test_mode: bool = False) -> Any:
    """Create a buy order"""
    try:
        if test_mode == True:
            url = CRYPTO_URL_TEST
        else:
            url = CRYPTO_URL_LIVE
        payload = {
            'symbol': symbol.upper(),
            'quantity': quantity,
            'order_type': order_type,
            'limitPrice': price
        }
        response = requests.post('{}/buy/{}'.format(url, exchange),
                                 headers=crypto_get_headers(
                                     api_key, api_secret, exchange_password,
                                     exchange_uid),
                                 json=payload)
        if response:
            return response.json()
        if response.status_code == 400:
            logger.error('Oops! An error Occurred ⚠️')
            raise BadRequest(response.text)
        if response.status_code == 401:
            logger.error('Oops! An error Occurred ⚠️')
            raise InvalidCredentials(response.text)
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def sell(symbol: str,
         quantity: Any,
         order_type: str = "market",
         price: Any = None,
         exchange: str = CRYPTO_EXCHANGE,
         api_key: str = CRYPTO_API_KEY,
         api_secret: str = CRYPTO_API_SECRET,
         exchange_password: Any = CRYPTO_API_PASSWORD,
         exchange_uid: Any = CRYPTO_API_UID,
         test_mode: bool = False) -> Any:
    """Create a sell order"""
    try:
        if test_mode == True:
            url = CRYPTO_URL_TEST
        else:
            url = CRYPTO_URL_LIVE
        payload = {
            'symbol': symbol.upper(),
            'quantity': quantity,
            'order_type': order_type,
            'limitPrice': price
        }
        response = requests.post('{}/sell/{}'.format(url, exchange),
                                 headers=crypto_get_headers(
                                     api_key, api_secret, exchange_password,
                                     exchange_uid),
                                 json=payload)
        if response:
            return response.json()
        if response.status_code == 400:
            logger.error('Oops! An error Occurred ⚠️')
            raise BadRequest(response.text)
        if response.status_code == 401:
            logger.error('Oops! An error Occurred ⚠️')
            raise InvalidCredentials(response.text)
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


def cancel_order(order_id: str,
                 exchange: str = CRYPTO_EXCHANGE,
                 api_key: str = CRYPTO_API_KEY,
                 api_secret: str = CRYPTO_API_SECRET,
                 exchange_password: Any = CRYPTO_API_PASSWORD,
                 exchange_uid: Any = CRYPTO_API_UID,
                 test_mode: bool = False) -> Any:
    """Cancel a specific order"""
    try:
        if test_mode == True:
            url = CRYPTO_URL_TEST
        else:
            url = CRYPTO_URL_LIVE
        payload = {'order_id': order_id}
        response = requests.post('{}/cancel_order/{}'.format(url, exchange),
                                 headers=crypto_get_headers(
                                     api_key, api_secret, exchange_password,
                                     exchange_uid),
                                 json=payload)
        if response:
            return response.json()
        if response.status_code == 400:
            logger.error('Oops! An error Occurred ⚠️')
            raise BadRequest(response.text)
        if response.status_code == 401:
            logger.error('Oops! An error Occurred ⚠️')
            raise InvalidCredentials(response.text)
    except Exception as exception:
        logger.error('Oops! An error Occurred ⚠️')
        raise exception


'''Functions not in documentation'''


def incoming_tick_data_handler(symbol: str,
                               number_of_data_points: int = 1,
                               fake_feed: bool = False):
    latest_orderbook_entry = order_book(symbol, number_of_data_points=1)
    latest_trades = trades(symbol, number_of_data_points=1)
    latest_orderbook_entry_dict = {}
    latest_orderbook_entry_dict['symbol'] = symbol
    latest_orderbook_entry_dict['ask'] = latest_orderbook_entry['asks'][0][
        0] if len(latest_orderbook_entry['asks']) > 0 else None
    latest_orderbook_entry_dict['asksize'] = latest_orderbook_entry['asks'][0][
        1] if len(latest_orderbook_entry['asks']) > 0 else None
    latest_orderbook_entry_dict['bid'] = latest_orderbook_entry['bids'][0][
        0] if len(latest_orderbook_entry['bids']) > 0 else None
    latest_orderbook_entry_dict['bidsize'] = latest_orderbook_entry['bids'][0][
        1] if len(latest_orderbook_entry['bids']) > 0 else None
    latest_orderbook_entry_dict['quotedate'] = latest_orderbook_entry[
        'datetime']
    latest_orderbook_entry_dict['nonce'] = latest_orderbook_entry['nonce']
    latest_orderbook_entry_dict['price'] = latest_trades[0]['price']
    latest_orderbook_entry_dict['tradesize'] = latest_trades[0]['amount']
    latest_orderbook_entry_dict['tradedate'] = latest_trades[0]['datetime']
    return latest_orderbook_entry_dict


def incoming_tick_data_handler_level2(symbol: str,
                                      number_of_data_points: int = 1,
                                      fake_feed: bool = False):
    latest_orderbook_entry = L2_order_book(symbol, number_of_data_points=1)
    latest_trades = trades(symbol, number_of_data_points=1)
    latest_orderbook_entry_dict = {}
    latest_orderbook_entry_dict['symbol'] = symbol
    latest_orderbook_entry_dict['ask'] = latest_orderbook_entry['asks'][0][
        0] if len(latest_orderbook_entry['asks']) > 0 else None
    latest_orderbook_entry_dict['asksize'] = latest_orderbook_entry['asks'][0][
        1] if len(latest_orderbook_entry['asks']) > 0 else None
    latest_orderbook_entry_dict['bid'] = latest_orderbook_entry['bids'][0][
        0] if len(latest_orderbook_entry['bids']) > 0 else None
    latest_orderbook_entry_dict['bidsize'] = latest_orderbook_entry['bids'][0][
        1] if len(latest_orderbook_entry['bids']) > 0 else None
    latest_orderbook_entry_dict['quotedate'] = latest_orderbook_entry[
        'datetime']
    latest_orderbook_entry_dict['nonce'] = latest_orderbook_entry['nonce']
    latest_orderbook_entry_dict['price'] = latest_trades[0]['price']
    latest_orderbook_entry_dict['tradesize'] = latest_trades[0]['amount']
    latest_orderbook_entry_dict['tradedate'] = latest_trades[0]['datetime']
    return latest_orderbook_entry_dict
