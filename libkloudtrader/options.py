"""This module contains all functions related to options"""

import requests
import os
import typing
import datetime
import pandas
from .exceptions import (
    InvalidBrokerage,
    InvalidStockExchange,
    BadRequest,
    InvalidCredentials,
)
from .logs import start_logger

logger = start_logger(__name__)
"""Data APIs start"""
"""Config starts"""
USER_ACCESS_TOKEN = os.environ['USER_ACCESS_TOKEN']
USER_ACCOUNT_NUMBER = os.environ['USER_ACCOUNT_NUMBER']
USER_BROKERAGE = os.environ['USER_BROKERAGE']
TR_STREAMING_API_URL = "https://stream.tradier.com"
TR_BROKERAGE_API_URL = "https://production-api.tradier.com"
TR_SANDBOX_BROKERAGE_API_URL = "https://production-sandbox.tradier.com"


def tr_get_headers(access_token: str) -> dict:
    '''headers for TR brokerage'''
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer " + access_token
    }
    return headers


def tr_get_content_headers() -> dict:
    '''content headers for TR brokerage'''
    headers = {
        'Accept': 'application/json',
    }
    return headers


"""Config ends"""


def chains(underlying_symbol: str,
           expiration: str,
           greeks: bool = False,
           brokerage: typing.Any = USER_BROKERAGE,
           access_token: str = USER_ACCESS_TOKEN,
           dataframe: bool = True) -> dict:
    """Get options chains"""
    try:
        if brokerage == "Tradier Inc.":
            url = TR_BROKERAGE_API_URL
        elif brokerage == "miscpaper":
            url = TR_SANDBOX_BROKERAGE_API_URL
        else:
            logger.error('Oops! An error Occurred ⚠️')
            raise InvalidBrokerage
        params = {
            'symbol': underlying_symbol.upper(),
            'expiration': str(expiration),
            'greeks': 'true'
        }
        response = requests.get("{}/v1/markets/options/chains".format(url),
                                headers=tr_get_headers(access_token),
                                params=params)
        if greeks:
            return response.json()
        if response:
            if response.json()['options'] != None:
                data = response.json()
                for i in data['options']['option']:
                    i['trade_date'] = datetime.datetime.fromtimestamp(
                        float(i['trade_date']) /
                        1000.0).strftime("%Y-%m-%d %H:%M:%S")
                    i['bid_date'] = datetime.datetime.fromtimestamp(
                        float(i['bid_date']) /
                        1000.0).strftime("%Y-%m-%d %H:%M:%S")
                    i['ask_date'] = datetime.datetime.fromtimestamp(
                        float(i['ask_date']) /
                        1000.0).strftime("%Y-%m-%d %H:%M:%S")
                if dataframe == False:
                    return data['options']['option']
                else:
                    data = pandas.DataFrame(data['options']['option'])
                    dataframe = pandas.DataFrame(data)
                    dataframe.set_index(['symbol'], inplace=True)
                    return dataframe
            else:
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


def expirations(underlying_symbol: str,
                includeAllRoots: bool = True,
                strikes: bool = True,
                brokerage: typing.Any = USER_BROKERAGE,
                access_token: str = USER_ACCESS_TOKEN) -> dict:
    """Get expiration dates for a particular underlying."""
    try:
        if brokerage == "Tradier Inc.":
            url = TR_BROKERAGE_API_URL
        elif brokerage == "miscpaper":
            url = TR_SANDBOX_BROKERAGE_API_URL
        else:
            logger.error('Oops! An error Occurred ⚠️')
            raise InvalidBrokerage
        params = {
            'symbol': underlying_symbol.upper(),
            'includeAllRoots': includeAllRoots,
            'strikes': strikes
        }
        response = requests.get(
            "{}/v1/markets/options/expirations".format(url),
            headers=tr_get_headers(access_token),
            params=params)
        if response:
            if response.json()['expirations'] != None:
                return response.json()['expirations']['expiration']
            else:
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


def strikes(underlying_symbol: str,
            expiration: str,
            brokerage: typing.Any = USER_BROKERAGE,
            access_token: str = USER_ACCESS_TOKEN) -> dict:
    """Get an options strike prices for a specified expiration date."""
    try:
        if brokerage == "Tradier Inc.":
            url = TR_BROKERAGE_API_URL
        elif brokerage == "miscpaper":
            url = TR_SANDBOX_BROKERAGE_API_URL
        else:
            logger.error('Oops! An error Occurred ⚠️')
            raise InvalidBrokerage
        params = {
            'symbol': underlying_symbol.upper(),
            'expiration': str(expiration)
        }
        response = requests.get("{}/v1/markets/options/strikes".format(url),
                                headers=tr_get_headers(access_token),
                                params=params)
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


"""Data APIs end"""
""""Trading APIs begin"""


def buy_to_open_preview(underlying_symbol: str,
                        option_symbol: str,
                        quantity: int,
                        order_type: str = "market",
                        duration: str = "gtc",
                        price: typing.Any = None,
                        stop: typing.Any = None,
                        brokerage: typing.Any = USER_BROKERAGE,
                        access_token: str = USER_ACCESS_TOKEN,
                        account_number: str = USER_ACCOUNT_NUMBER) -> dict:
    """Place buy to open Options order to trade a single option."""
    try:
        if brokerage == "Tradier Inc.":
            url = TR_BROKERAGE_API_URL
        elif brokerage == "miscpaper":
            url = TR_SANDBOX_BROKERAGE_API_URL
        else:
            logger.error('Oops! An error Occurred ⚠️')
            raise InvalidBrokerage
        params = {
            'symbol': str(underlying_symbol.upper()),
            'class': 'option',
            'option_symbol': str(option_symbol.upper()),
            'side': 'buy_to_open',
            'quantity': quantity,
            'type': order_type,
            'duration': duration,
            'price': price,
            'stop': stop,
            'preview': True
        }
        response = requests.post("{}/v1/accounts/{}/orders".format(
            url, account_number),
                                 headers=tr_get_headers(access_token),
                                 params=params)
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


def buy_to_close_preview(underlying_symbol: str,
                         option_symbol: str,
                         quantity: int,
                         order_type: str = "market",
                         duration: str = "gtc",
                         price: typing.Any = None,
                         stop: typing.Any = None,
                         brokerage: typing.Any = USER_BROKERAGE,
                         access_token: str = USER_ACCESS_TOKEN,
                         account_number: str = USER_ACCOUNT_NUMBER) -> dict:
    """Place buy to close Options order to trade a single option."""
    try:
        if brokerage == "Tradier Inc.":
            url = TR_BROKERAGE_API_URL
        elif brokerage == "miscpaper":
            url = TR_SANDBOX_BROKERAGE_API_URL
        else:
            logger.error('Oops! An error Occurred ⚠️')
            raise InvalidBrokerage
        params = {
            'symbol': underlying_symbol.upper(),
            'class': 'option',
            'option_symbol': option_symbol,
            'side': 'buy_to_close',
            'quantity': quantity,
            'type': order_type,
            'duration': duration,
            'price': price,
            'stop': stop,
            'preview': True
        }
        response = requests.post("{}/v1/accounts/{}/orders".format(
            url, account_number),
                                 headers=tr_get_headers(access_token),
                                 params=params)
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


def sell_to_open_preview(underlying_symbol: str,
                         option_symbol: str,
                         quantity: int,
                         order_type: str = "market",
                         duration: str = "gtc",
                         price: typing.Any = None,
                         stop: typing.Any = None,
                         brokerage: typing.Any = USER_BROKERAGE,
                         access_token: str = USER_ACCESS_TOKEN,
                         account_number: str = USER_ACCOUNT_NUMBER) -> dict:
    """Place buy to open Options order to trade a single option."""
    try:
        if brokerage == "Tradier Inc.":
            url = TR_BROKERAGE_API_URL
        elif brokerage == "miscpaper":
            url = TR_SANDBOX_BROKERAGE_API_URL
        else:
            logger.error('Oops! An error Occurred ⚠️')
            raise InvalidBrokerage
        params = {
            'symbol': underlying_symbol.upper(),
            'class': 'option',
            'option_symbol': option_symbol,
            'side': 'sell_to_open',
            'quantity': quantity,
            'type': order_type,
            'duration': duration,
            'price': price,
            'stop': stop,
            'preview': True
        }
        response = requests.post("{}/v1/accounts/{}/orders".format(
            url, account_number),
                                 headers=tr_get_headers(access_token),
                                 params=params)
        if response:
            logger.error('Oops! An error Occurred ⚠️')
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


def sell_to_close_preview(underlying_symbol: str,
                          option_symbol: str,
                          quantity: int,
                          order_type: str = "market",
                          duration: str = "gtc",
                          price: typing.Any = None,
                          stop: typing.Any = None,
                          brokerage: typing.Any = USER_BROKERAGE,
                          access_token: str = USER_ACCESS_TOKEN,
                          account_number: str = USER_ACCOUNT_NUMBER) -> dict:
    """Place sell to close Options order to trade a single option."""
    try:
        if brokerage == "Tradier Inc.":
            url = TR_BROKERAGE_API_URL
        elif brokerage == "miscpaper":
            url = TR_SANDBOX_BROKERAGE_API_URL
        else:
            logger.error('Oops! An error Occurred ⚠️')
            raise InvalidBrokerage
        params = {
            'symbol': underlying_symbol.upper(),
            'class': 'option',
            'option_symbol': option_symbol,
            'side': 'sell_to_close',
            'quantity': quantity,
            'type': order_type,
            'duration': duration,
            'price': price,
            'stop': stop,
            'preview': True
        }
        response = requests.post("{}/v1/accounts/{}/orders".format(
            url, account_number),
                                 headers=tr_get_headers(access_token),
                                 params=params)
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


def buy_to_open(underlying_symbol: str,
                option_symbol: str,
                quantity: int,
                order_type: str = "market",
                duration: str = "day",
                price: typing.Any = None,
                stop: typing.Any = None,
                brokerage: typing.Any = USER_BROKERAGE,
                access_token: str = USER_ACCESS_TOKEN,
                account_number: str = USER_ACCOUNT_NUMBER) -> dict:
    """Place buy to open Options order to trade a single option."""
    try:
        if brokerage == "Tradier Inc.":
            url = TR_BROKERAGE_API_URL
        elif brokerage == "miscpaper":
            url = TR_SANDBOX_BROKERAGE_API_URL
        else:
            logger.error('Oops! An error Occurred ⚠️')
            raise InvalidBrokerage
        params = {
            'symbol': underlying_symbol.upper(),
            'class': 'option',
            'option_symbol': option_symbol,
            'side': 'buy_to_open',
            'quantity': quantity,
            'type': order_type,
            'duration': duration,
            'price': price,
            'stop': stop
        }
        response = requests.post("{}/v1/accounts/{}/orders".format(
            url, account_number),
                                 headers=tr_get_headers(access_token),
                                 params=params)
        if response:
            logger.error('Oops! An error Occurred ⚠️')
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


def buy_to_close(underlying_symbol: str,
                 option_symbol: str,
                 quantity: int,
                 order_type: str = "market",
                 duration: str = "gtc",
                 price: typing.Any = None,
                 stop: typing.Any = None,
                 brokerage: typing.Any = USER_BROKERAGE,
                 access_token: str = USER_ACCESS_TOKEN,
                 account_number: str = USER_ACCOUNT_NUMBER) -> dict:
    """Place buy to close Options order to trade a single option."""
    try:
        if brokerage == "Tradier Inc.":
            url = TR_BROKERAGE_API_URL
        elif brokerage == "miscpaper":
            url = TR_SANDBOX_BROKERAGE_API_URL
        else:
            logger.error('Oops! An error Occurred ⚠️')
            raise InvalidBrokerage
        params = {
            'symbol': underlying_symbol.upper(),
            'class': 'option',
            'option_symbol': option_symbol,
            'side': 'buy_to_close',
            'quantity': quantity,
            'type': order_type,
            'duration': duration,
            'price': price,
            'stop': stop
        }
        response = requests.post("{}/v1/accounts/{}/orders".format(
            url, account_number),
                                 headers=tr_get_headers(access_token),
                                 params=params)
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


def sell_to_open(underlying_symbol: str,
                 option_symbol: str,
                 quantity: int,
                 order_type: str = "market",
                 duration: str = "gtc",
                 price: typing.Any = None,
                 stop: typing.Any = None,
                 brokerage: typing.Any = USER_BROKERAGE,
                 access_token: str = USER_ACCESS_TOKEN,
                 account_number: str = USER_ACCOUNT_NUMBER) -> dict:
    """Place sell to open Options order to trade a single option."""
    try:
        if brokerage == "Tradier Inc.":
            url = TR_BROKERAGE_API_URL
        elif brokerage == "miscpaper":
            url = TR_SANDBOX_BROKERAGE_API_URL
        else:
            logger.error('Oops! An error Occurred ⚠️')
            raise InvalidBrokerage
        params = {
            'symbol': underlying_symbol.upper(),
            'class': 'option',
            'option_symbol': option_symbol,
            'side': 'sell_to_open',
            'quantity': quantity,
            'type': order_type,
            'duration': duration,
            'price': price,
            'stop': stop
        }
        response = requests.post("{}/v1/accounts/{}/orders".format(
            url, account_number),
                                 headers=tr_get_headers(access_token),
                                 params=params)
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


def sell_to_close(underlying_symbol: str,
                  option_symbol: str,
                  quantity: int,
                  order_type: str = "market",
                  duration: str = "gtc",
                  price: typing.Any = None,
                  stop: typing.Any = None,
                  brokerage: typing.Any = USER_BROKERAGE,
                  access_token: str = USER_ACCESS_TOKEN,
                  account_number: str = USER_ACCOUNT_NUMBER) -> dict:
    """Place sell to close Options order to trade a single option."""
    try:
        if brokerage == "Tradier Inc.":
            url = TR_BROKERAGE_API_URL
        elif brokerage == "miscpaper":
            url = TR_SANDBOX_BROKERAGE_API_URL
        else:
            logger.error('Oops! An error Occurred ⚠️')
            raise InvalidBrokerage
        params = {
            'symbol': underlying_symbol.upper(),
            'class': 'option',
            'option_symbol': option_symbol,
            'side': 'sell_to_close',
            'quantity': quantity,
            'type': order_type,
            'duration': duration,
            'price': price,
            'stop': stop
        }
        response = requests.post("{}/v1/accounts/{}/orders".format(
            url, account_number),
                                 headers=tr_get_headers(access_token),
                                 params=params)
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


def change_order(order_id: str,
                 duration: str,
                 order_type: str,
                 price: typing.Any = None,
                 stop: typing.Any = None,
                 brokerage: typing.Any = USER_BROKERAGE,
                 access_token: str = USER_ACCESS_TOKEN,
                 account_number: str = USER_ACCOUNT_NUMBER) -> dict:
    '''Change an order if it is not filled yet.'''
    try:
        if brokerage == "Tradier Inc.":
            url = TR_BROKERAGE_API_URL
        elif brokerage == "miscpaper":
            url = TR_SANDBOX_BROKERAGE_API_URL
        else:
            raise InvalidBrokerage
        put_params = {
            'order_id': order_id,
            'type': str(order_type.lower()),
            'duration': str(duration),
            'price': str(price),
            'stop': str(stop)
        }
        response = requests.put("{}/v1/accounts/{}/orders/{}".format(
            url, account_number, order_id),
                                data=put_params,
                                headers=tr_get_headers(access_token))
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
                 brokerage: typing.Any = USER_BROKERAGE,
                 access_token: str = USER_ACCESS_TOKEN,
                 account_number: str = USER_ACCOUNT_NUMBER) -> dict:
    '''Cancel an order if it is not filled yet.'''
    try:
        if brokerage == "Tradier Inc.":
            url = TR_BROKERAGE_API_URL
        elif brokerage == "miscpaper":
            url = TR_SANDBOX_BROKERAGE_API_URL
        else:
            logger.error('Oops! An error Occurred ⚠️')
            raise InvalidBrokerage
        response = requests.delete("{}/v1/accounts/{}/orders/{}".format(
            url, account_number, order_id),
                                   headers=tr_get_headers(access_token))
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


"""Trading APIs end"""
