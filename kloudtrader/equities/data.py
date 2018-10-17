#everything related to data
from streamz import Stream
from datetime import datetime
import requests
import intrinio 
import os
import json
from streamz import Stream
stream=Stream()


STREAMING_API_URL="https://stream.tradier.com"
BROKERAGE_API_URL="https://api.tradier.com"
intrinio.client.username=os.environ['INTRINIO_USERNAME']
intrinio.client.password=os.environ['INTRINIO_PASSWORD']
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





def prices(ticker,start_date,end_date,frequency):
    try:
        return intrinio.prices(str(ticker), str(start_date),str(end_date),str(frequency),sort_order='asc')
    except:
        raise Exception("Did not receive any data.")


def open_prices(ticker,start_date,end_date,frequency):
    try:
        return intrinio.prices(str(ticker), str(start_date),str(end_date),str(frequency),sort_order='asc')['open']
    except:
        raise Exception("Did not receive any data.")


def high_prices(ticker,start_date,end_date,frequency):
    try:
        return intrinio.prices(str(ticker), str(start_date),str(end_date),str(frequency),sort_order='asc')['high']
    except:
        raise Exception("Did not receive any data.")


def low_prices(ticker,start_date,end_date,frequency):
    try:
        return intrinio.prices(str(ticker), str(start_date),str(end_date),str(frequency),sort_order='asc')['low']
    except:
        raise Exception("Did not receive any data.")


def close_prices(ticker,start_date,end_date,frequency):
    try:
        return intrinio.prices(str(ticker), str(start_date),str(end_date),str(frequency),sort_order='asc')['close']
    except:
        raise Exception("Did not receive any data.")


def volume(ticker,start_date,end_date,frequency):
    try:
        return intrinio.prices(str(ticker), str(start_date),str(end_date),str(frequency),sort_order='asc')['volume']
    except:
        raise Exception("Did not receive any data.")




#yearly fundamentals including PE ratio, net debt, total capital and over 100 other variables
def fundamentals(symbol):
    try:
        return intrinio.financials(str(symbol.upper()))
    except:
        raise Exception("Did not receive any data.")


def company_information(symbol):
    try:
        return intrinio.companies(str(symbol.upper()))
    except:
        raise Exception("Did not receive any data.")


#get cik, lei, name and ticker of companies with the passed quey in their company name
def search_company(query):
    try:
        return intrinio.companies(query=query)
    except:
        raise Exception("Did not receive any data.")

def datapoint(ticker,item):
    try:
        datapoint=requests.get('https://api.intrinio.com/data_point?'+'identifier='+str(ticker)+'&'+'item='+str(item),auth=(intrinio_username,intrinio_password))          
        return {datapoint.json()['item']:datapoint.json()['value']}
    except:
        raise Exception("Did not receive any data. Status Code: %d"%datapoint.status_code)



'''Market Data'''

def get_latest_quotes(symbols, access_token=ACCESS_TOKEN):
    r=requests.get(BROKERAGE_API_URL+"/v1/markets/quotes?"+"symbols="+str(symbols.upper()),headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)


def time_and_sales(symbols, access_token=ACCESS_TOKEN):
    r=requests.get(BROKERAGE_API_URL+"/v1/markets/timesales?symbol="+str(symbols.upper()),headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)


def intraday_status(access_token=ACCESS_TOKEN):
    r=requests.get(BROKERAGE_API_URL+"/v1/markets/clock", headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)

def market_calendar(month,year): #goes back till 2013
    params = {
    'year': year,
    'month': month
    }
    
    r=requests.get(BROKERAGE_API_URL+"/v1/markets/calendar",headers=get_content_headers(),params=params)
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)


#search for securities' symbol and the exchanges they are listed on by entering comapny name
def symbol_search(company_name, access_token=ACCESS_TOKEN):
    r=requests.get(BROKERAGE_API_URL+"/v1/markets/search?q="+str(company_name),headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)
    

 #search for securities using symbol 
def symbol_lookup(symbol,access_token=ACCESS_TOKEN):
    r=requests.get(BROKERAGE_API_URL+"/v1/markets/lookup?q="+str(symbol),headers=get_headers(access_token))
    try:
        return r.json()['securities']
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)


def corporate_calendar(symbols,access_token=ACCESS_TOKEN):
    r=requests.get(BROKERAGE_API_URL+"/beta/markets/fundamentals/company?symbols="+str(symbols.upper()),headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)


'''Live Data'''
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


def get_live_quotes(symbol, sessionid):
    # gets market events
    payload = {"sessionid": sessionid, "symbols": str(symbol.upper())}
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
                    
                    
                    return stream.sink(quotes["ask"])

    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)

def get_live_trades(symbol, sessionid):
    # gets market events
    payload = {"sessionid": sessionid, "symbols": str(symbol.upper())}
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
