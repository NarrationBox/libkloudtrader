import json
import os
import sys
from datetime import datetime
from time import sleep
import pandas as pd
import requests
import io
sys.path.append("..")
from libkloudtrader.defaults import ACCESS_TOKEN, ACCOUNT_NUMBER



STREAMING_API_URL="https://stream.tradier.com"
BROKERAGE_API_URL="https://api.tradier.com"
SANDBOX_API_URL="https://sandbox.tradier.com"




def get_headers(access_token):
    headers = {"Accept":"application/json",
           "Authorization":"Bearer "+access_token}
    return headers

def get_content_headers():
    headers = {
    'Accept': 'application/json',
    }

    return headers

'''Market Data'''

def quotes(symbols, access_token=ACCESS_TOKEN):
    r=requests.get(BROKERAGE_API_URL+"/v1/markets/quotes?"+"symbols="+str(symbols.upper()),headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)

def OHLCV(symbol,start,end,interval='daily',access_token=ACCESS_TOKEN):
    params = {
    'symbol': str(symbol.upper()),
    'start':str(start),
    'end' :str(end),
    'interval': str(interval.lower()),
    }
    r=requests.get(BROKERAGE_API_URL+"/v1/markets/history?",params=params,
    headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)
    
def close_prices(symbol,start,end,interval='daily',access_token=ACCESS_TOKEN):
    data=OHLCV(symbol,start,end,interval='daily',access_token=ACCESS_TOKEN)
    try:
        close_data=[dict(date=rows['date'], close=rows['close']) for rows in data['history']['day']]
        return close_data
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)

def open_prices(symbol,start,end,interval='daily',access_token=ACCESS_TOKEN):
    data=OHLCV(symbol,start,end,interval='daily',access_token=ACCESS_TOKEN)
    try:
        open_data=[dict(date=rows['date'], open=rows['open']) for rows in data['history']['day']]
        return open_data
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)

def high_prices(symbol,start,end,interval='daily',access_token=ACCESS_TOKEN):
    data=OHLCV(symbol,start,end,interval='daily',access_token=ACCESS_TOKEN)
    try:
        high_data=[dict(date=rows['date'], high=rows['high']) for rows in data['history']['day']]
        return high_data
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)

def low_prices(symbol,start,end,interval='daily',access_token=ACCESS_TOKEN):
    data=OHLCV(symbol,start,end,interval='daily',access_token=ACCESS_TOKEN)
    try:
        low_data=[dict(date=rows['date'], low=rows['low']) for rows in data['history']['day']]
        return low_data
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)
    
def volume(symbol,start,end,interval='daily',access_token=ACCESS_TOKEN):
    data=OHLCV(symbol,start,end,interval='daily',access_token=ACCESS_TOKEN)
    try:
        volume_data=[dict(date=rows['date'], volume=rows['volume']) for rows in data['history']['day']]
        return volume_data
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)

def tick_data(symbol,start=None,end=None,data_filter='all',access_token=ACCESS_TOKEN):
    params={
        'symbol':str.upper(symbol),
        'interval':'tick',
        'start':start,
        'end':end,
        'session_filter':str(data_filter)
    }
    r=requests.get(BROKERAGE_API_URL+"/v1/markets/timesales",headers=get_headers(access_token),params=params)
    try:
        return r.json()['series']['data']
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)

def min5_bar_data(symbol,start=None,end=None,data_filter='all',access_token=ACCESS_TOKEN):
    params={
        'symbol':str.upper(symbol),
        'interval':'5min',
        'start':start,
        'end':end,
        'session_filter':str(data_filter)
    }
    r=requests.get(BROKERAGE_API_URL+"/v1/markets/timesales",headers=get_headers(access_token),params=params)
    try:
        return r.json()['series']['data']
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)

def min15_bar_data(symbol,start=None,end=None,data_filter='all',access_token=ACCESS_TOKEN):
    params={
         'symbol':str.upper(symbol),
        'interval':'15min',
        'start':start,
        'end':end,
        'session_filter':str(data_filter)
    }
    r=requests.get(BROKERAGE_API_URL+"/v1/markets/timesales",headers=get_headers(access_token),params=params)
    try:
        return r.json()['series']['data']
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)

def list_of_companies(exchange='all'):
    try:
        nasdaq_request=requests.get('https://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download')
        nasdaq_companies=nasdaq_request.content
        nasdaq_df=pd.read_csv(io.StringIO(nasdaq_companies.decode('utf-8')))
        nyse_request=requests.get("https://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nyse&render=download")
        nyse_companies=nyse_request.content
        nyse_df=pd.read_csv(io.StringIO(nyse_companies.decode('utf-8')))
        amex_request=requests.get("https://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=amex&render=download")
        amex_companies=amex_request.content
        amex_df=pd.read_csv(io.StringIO(amex_companies.decode('utf-8')))
        if exchange=="all":
            df = nyse_df.append(nasdaq_df, ignore_index=True)
            df=df.append(amex_df, ignore_index=True)
        elif exchange.upper()=='NYSE':
            df = nyse_df
        elif exchange.upper()=='NASDAQ':
            df = nasdaq_df
        elif exchange.upper()=="AMEX":
            df = amex_df
        else:
            return 'Invalid Exchange!'
        df=df.drop(columns=['Summary Quote','Unnamed: 8'])
        return df
    except:
        raise Exception("Did not receive any data. Status Code: %d"%nyse_request.status_code)

def intraday_status(access_token=ACCESS_TOKEN):
    r=requests.get(BROKERAGE_API_URL+"/v1/markets/clock",headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)


def market_calendar(month,year):
    params = {
    'year': year,
    'month': month
    }
    
    r=requests.get(BROKERAGE_API_URL+"/v1/markets/calendar",headers=get_content_headers(),params=params)
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)

def symbol_search(company_name, indexes=True,access_token=ACCESS_TOKEN):
    r=requests.get(BROKERAGE_API_URL+"/v1/markets/search?q="+str(company_name)+"&indexes="+str(indexes),headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)

def symbol_lookup(symbol,access_token=ACCESS_TOKEN):
    r=requests.get(BROKERAGE_API_URL+"/v1/markets/lookup?q="+str(symbol),headers=get_headers(access_token))
    try:
        return r.json()['securities']
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)

def company_fundamentals(symbol,access_token=ACCESS_TOKEN):
    r=requests.get(BROKERAGE_API_URL+"/beta/markets/fundamentals/company?symbols="+str(symbol.upper()),headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)

def corporate_calendar(symbols,access_token=ACCESS_TOKEN):
    r=requests.get(BROKERAGE_API_URL+"/beta/markets/fundamentals/calendars?symbols="+str(symbols.upper()),headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)
    
def dividend_information(symbols,access_token=ACCESS_TOKEN):
    r=requests.get(BROKERAGE_API_URL+"/beta/markets/fundamentals/dividends?symbols="+str(symbols.upper()),headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)

def dividend_information(symbols,access_token=ACCESS_TOKEN):
    r=requests.get(BROKERAGE_API_URL+"/beta/markets/fundamentals/dividends?symbols="+str(symbols.upper()),headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)

def corporate_actions(symbols,access_token=ACCESS_TOKEN):
    r=requests.get(BROKERAGE_API_URL+"/beta/markets/fundamentals/corporate_actions?symbols="+str(symbols.upper()),headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)

def operation_ratio(symbols,access_token=ACCESS_TOKEN):
    r=requests.get(BROKERAGE_API_URL+"/beta/markets/fundamentals/ratios?symbols="+str(symbols.upper()),headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)

def corporate_financials(symbols,access_token=ACCESS_TOKEN):
    r=requests.get(BROKERAGE_API_URL+"/beta/markets/fundamentals/financials?symbols="+str(symbols.upper()),headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)

def price_statistics(symbols,access_token=ACCESS_TOKEN):
    r=requests.get(BROKERAGE_API_URL+"/beta/markets/fundamentals/statistics?symbols="+str(symbols.upper()),headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)

'''Live data'''
def create_session(access_token=ACCESS_TOKEN):
    # creates a streaming session
    r = requests.post(
        BROKERAGE_API_URL+"/v1/markets/events/session", headers=get_headers(access_token)
    )
    try:
        stream = r.json()["stream"]
        sessionid = str(stream["sessionid"])
        return sessionid
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)

def live_quotes(symbols, sessionid):
    # gets market events
    payload = {"sessionid": sessionid, "symbols": str(symbols.upper())}
    r = requests.post(
        STREAMING_API_URL+"/v1/markets/events",
        params=payload,
        headers=get_headers(ACCESS_TOKEN),
        stream=True,
    )
    try:
        for data in r.iter_content(chunk_size=None, decode_unicode=True):
            lines = data.decode("utf-8").replace('}{', '}\n{').split('\n')
            for line in lines:
                quotes=json.loads(line)
                if quotes['type']=='quote':
                    return quotes

    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)


def live_trades(symbols, sessionid):
    # gets market events
    payload = {"sessionid": sessionid, "symbols": str(symbols.upper())}
    r = requests.post(
        STREAMING_API_URL+"/v1/markets/events",
        params=payload,
        headers=get_headers(ACCESS_TOKEN),
        stream=True,
    )
    try:
        for data in r.iter_content(chunk_size=None, decode_unicode=True):
            lines = data.decode("utf-8").replace('}{', '}\n{').split('\n')
            for line in lines:
                quotes=json.loads(line)
                if quotes['type']=='trade':
                    return quotes

    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)
