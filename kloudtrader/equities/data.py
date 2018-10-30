import json
import os
from datetime import datetime
import requests
from botocore.docs import params


STREAMING_API_URL="https://stream.tradier.com"
BROKERAGE_API_URL="https://api.tradier.com"
SANDBOX_API_URL="https://sandbox.tradier.com"
ACCESS_TOKEN = os.environ['TRADIER_ACCESS_TOKEN']
CONSUMER_KEY=os.environ['TRADIER_CONSUMER_KEY']
ACCOUNT_NUMBER=os.environ['TRADIER_ACCOUNT_NUMBER']

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

def historical_prices(symbol,start,end,interval='daily',access_token=ACCESS_TOKEN):
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
    

def intrday_status(access_token=ACCESS_TOKEN):
    r=requests.get(BROKERAGE_API_URL+"/v1/markets/clock",headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)


def time_and_sales(symbol,start,end,interval='tick',access_token=ACCESS_TOKEN):
    
    start=start.replace(' ','%20')
    end=end.replace(' ','%20')
    r=requests.get(BROKERAGE_API_URL+"/v1/markets/timesales?symbol="+str(symbol)+str(interval)+"&start="+start+"&end="+end,headers=get_headers(access_token),stream=True)
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)

    
#print(time_and_sales('AAPL','2018-10-24','2018-10-26'))

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

