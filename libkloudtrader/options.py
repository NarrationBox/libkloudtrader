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


def chains(symbol: str,
           expiration: str,
           brokerage: typing.Any = USER_BROKERAGE,
           access_token: str = USER_ACCESS_TOKEN,
           pandas: bool = False) -> dict:
    """Get options chains"""
    if brokerage == "Tradier Inc.":
        url = TR_BROKERAGE_API_URL
    elif brokerage == "miscpaper":
        url = TR_SANDBOX_BROKERAGE_API_URL
    else:
        raise InvalidBrokerage
    params = {'symbol': symbol.upper(), 'expiration': str(expiration)}
    response = requests.get("{}/v1/markets/options/chains".format(url),
                            headers=tr_get_headers(access_token),
                            params=params)
    if response:
        data = response.json()
        for i in data['options']['option']:
            i['trade_date'] = datetime.datetime.fromtimestamp(
                float(i['trade_date']) / 1000.0).strftime("%Y-%m-%d %H:%M:%S")
            i['bid_date'] = datetime.datetime.fromtimestamp(
                float(i['bid_date']) / 1000.0).strftime("%Y-%m-%d %H:%M:%S")
            i['ask_date'] = datetime.datetime.fromtimestamp(
                float(i['ask_date']) / 1000.0).strftime("%Y-%m-%d %H:%M:%S")
        if pandas == False:
            return data
        else:
            return pandas.DataFrame(data)
    if response.status_code == 400:
        raise BadRequest(response.text)
    if response.status_code == 401:
        raise InvalidCredentials(response.text)


def expirations(symbol: str,
                includeAllRoots: bool = True,
                strikes: bool = True,
                brokerage: typing.Any = USER_BROKERAGE,
                access_token: str = USER_ACCESS_TOKEN) -> dict:
    """Get expiration dates for a particular underlying."""
    if brokerage == "Tradier Inc.":
        url = TR_BROKERAGE_API_URL
    elif brokerage == "miscpaper":
        url = TR_SANDBOX_BROKERAGE_API_URL
    else:
        raise InvalidBrokerage
    params = {
        'symbol': symbol.upper(),
        'includeAllRoots': includeAllRoots,
        'strikes': strikes
    }
    response = requests.get("{}/v1/markets/options/expirations".format(url),
                            headers=tr_get_headers(access_token),
                            params=params)
    if response:
        return response.json()
    if response.status_code == 400:
        raise BadRequest(response.text)
    if response.status_code == 401:
        raise InvalidCredentials(response.text)


def strikes(symbol: str,
            expiration: str,
            brokerage: typing.Any = USER_BROKERAGE,
            access_token: str = USER_ACCESS_TOKEN) -> dict:
    """Get an options strike prices for a specified expiration date."""
    if brokerage == "Tradier Inc.":
        url = TR_BROKERAGE_API_URL
    elif brokerage == "miscpaper":
        url = TR_SANDBOX_BROKERAGE_API_URL
    else:
        raise InvalidBrokerage
    params = {'symbol': symbol.upper(), 'expiration': str(expiration)}
    response = requests.get("{}/v1/markets/options/strikes".format(url),
                            headers=tr_get_headers(access_token),
                            params=params)
    if response:
        return response.json()
    if response.status_code == 400:
        raise BadRequest(response.text)
    if response.status_code == 401:
        raise InvalidCredentials(response.text)


"""Data APIs end"""
""""Trading APIs begin"""


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
    if brokerage == "Tradier Inc.":
        url = TR_BROKERAGE_API_URL
    elif brokerage == "miscpaper":
        url = TR_SANDBOX_BROKERAGE_API_URL
    else:
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
        return response.json()
    if response.status_code == 400:
        raise BadRequest(response.text)
    if response.status_code == 401:
        raise InvalidCredentials(response.text)


def buy_to_close(underlying_symbol: str,
                 option_symbol: str,
                 quantity: int,
                 order_type: str = "market",
                 duration: str = "day",
                 price: typing.Any = None,
                 stop: typing.Any = None,
                 brokerage: typing.Any = USER_BROKERAGE,
                 access_token: str = USER_ACCESS_TOKEN,
                 account_number: str = USER_ACCOUNT_NUMBER) -> dict:
    """Place buy to close Options order to trade a single option."""
    if brokerage == "Tradier Inc.":
        url = TR_BROKERAGE_API_URL
    elif brokerage == "miscpaper":
        url = TR_SANDBOX_BROKERAGE_API_URL
    else:
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
        raise BadRequest(response.text)
    if response.status_code == 401:
        raise InvalidCredentials(response.text)


def sell_to_open(underlying_symbol: str,
                 option_symbol: str,
                 quantity: int,
                 order_type: str = "market",
                 duration: str = "day",
                 price: typing.Any = None,
                 stop: typing.Any = None,
                 brokerage: typing.Any = USER_BROKERAGE,
                 access_token: str = USER_ACCESS_TOKEN,
                 account_number: str = USER_ACCOUNT_NUMBER) -> dict:
    """Place buy to close Options order to trade a single option."""
    if brokerage == "Tradier Inc.":
        url = TR_BROKERAGE_API_URL
    elif brokerage == "miscpaper":
        url = TR_SANDBOX_BROKERAGE_API_URL
    else:
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
        raise BadRequest(response.text)
    if response.status_code == 401:
        raise InvalidCredentials(response.text)


def sell_to_close(underlying_symbol: str,
                  option_symbol: str,
                  quantity: int,
                  order_type: str = "market",
                  duration: str = "day",
                  price: typing.Any = None,
                  stop: typing.Any = None,
                  brokerage: typing.Any = USER_BROKERAGE,
                  access_token: str = USER_ACCESS_TOKEN,
                  account_number: str = USER_ACCOUNT_NUMBER) -> dict:
    """Place buy to close Options order to trade a single option."""
    if brokerage == "Tradier Inc.":
        url = TR_BROKERAGE_API_URL
    elif brokerage == "miscpaper":
        url = TR_SANDBOX_BROKERAGE_API_URL
    else:
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
        raise BadRequest(response.text)
    if response.status_code == 401:
        raise InvalidCredentials(response.text)


"""Trading APIs end"""
