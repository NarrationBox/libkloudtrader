#Trading apis

#TODO:
'''
time_and_sales()
options and multileg order support
improve error and exception handling
'''
import sys
sys.path.append("..")
from time import sleep
import json
import requests 
import os


BROKERAGE_API_URL="https://sandbox.tradier.com"
STREAMING_API_URL="https://stream.tradier.com"

def get_headers(access_token):
    headers = {"Accept":"application/json",
           "Authorization":"Bearer "+access_token}
    return headers



'''Trading'''
#Equity
def buy_preview(symbol,quantity,access_token=ACCESS_TOKEN,account_number=ACCOUNT_NUMBER,duration="day",order_type="market",price=None,stop=None):
    post_params={
        'class':'equity',
        'symbol':str(symbol.upper()), 
        'duration':str(duration.lower()), 
        'side':'buy',
        'quantity':str(quantity),
        'type':str(order_type.lower()), 
        'price':price,
        'stop':stop,
        'preview':'true'

    }
    r=requests.post(BROKERAGE_API_URL+"/v1/accounts/"+str(account_number)+"/orders/",params=post_params,headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)




def sell_preview(symbol,quantity,access_token=ACCESS_TOKEN,account_number=ACCOUNT_NUMBER,duration="day",order_type="market",price=None,stop=None):
    post_params={
        'class':'equity',
        'symbol':str(symbol.upper()), 
        'duration':str(duration.lower()), 
        'side':'sell',
        'quantity':str(quantity),
        'type':str(order_type.lower()),
        'price':None,
        'stop':None,
        'preview':'true'
    }
    r=requests.post(SANDBOX_API_URL+"/v1/accounts/"+str(account_number)+"/orders/",params=post_params,headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)



def buy(symbol,quantity,access_token=ACCESS_TOKEN,account_number=ACCOUNT_NUMBER,duration="day",order_type="market",price=None,stop=None):
    post_params={
        'class':'equity',
        'symbol':str(symbol.upper()), 
        'duration':str(duration.lower()), #time for which the order will be remain in effect (Day or GTC)
        'side':'buy',
        'quantity':str(quantity),
        'type':str(order_type.lower()), #market, limit, etc.
        'price':str(price),
        'stop':str(stop)
    }
    
    r=requests.post(BROKERAGE_API_URL+"/v1/accounts/"+str(account_number)+"/orders/",params=post_params,headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)
        


def sell(symbol,quantity,access_token=ACCESS_TOKEN,account_number=ACCOUNT_NUMBER,duration="day",order_type="market",price=None,stop=None):
    post_params={
        'class':'equity',
        'symbol':str(symbol.upper()), 
        'duration':str(duration.lower()), #time for which the order will be remain in effect (Day or GTC)
        'side':'sell',
        'quantity':str(quantity),
        'type':str(order_type.lower()), #market, limit, etc.
        'price':str(price),
        'stop':str(stop)
    }
    
    r=requests.post(BROKERAGE_API_URL+"/v1/accounts/"+str(account_number)+"/orders/",params=post_params,headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)
       


def change_equity_order(order_id,access_token=ACCESS_TOKEN,account_number=ACCOUNT_NUMBER,duration="day",order_type="market",price=None,stop=None):
    put_params={
        'order_id':order_id,
        'type':str(order_type.lower()), 
        'duration':str(duration),
        'price':str(price),
        'stop':str(stop)
    }
    r=requests.put(BROKERAGE_API_URL+"/v1/accounts/"+str(account_number)+"/orders/"+str(order_id),params=put_params,headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)



def cancel_equity_order(order_id,access_token=ACCESS_TOKEN,account_number=ACCOUNT_NUMBER):
    r=requests.delete(BROKERAGE_API_URL+"/v1/accounts/"+str(account_number)+"/orders/"+str(order_id),headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)



def user_profile(access_token=ACCESS_TOKEN):
    r=requests.get(BROKERAGE_API_URL+"/v1/user/profile",headers=get_headers(access_token))
    try:
        return r.json()
    except: 
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code
        )

def user_account_number(access_token=ACCESS_TOKEN):
    r=requests.get(BROKERAGE_API_URL+"/v1/user/profile",headers=get_headers(access_token))
    try:
        data=r.json()['profile']['account']
        account_numbers=[row['account_number'] for row in data]
        if len(account_numbers)>1:
            print("You have more than one account. ")
            return account_numbers

        return account_numbers
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code
        )


def account_balance(access_token=ACCESS_TOKEN,account_number=ACCOUNT_NUMBER):
    r=requests.get(BROKERAGE_API_URL+"/v1/accounts/"+str(account_number)+"/balances",headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)

def user_balance(access_token=ACCESS_TOKEN):
    r=requests.get(BROKERAGE_API_URL+"/v1/user/balances",headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)


def account_positions(access_token=ACCESS_TOKEN,account_number=ACCOUNT_NUMBER):
    r=requests.get(BROKERAGE_API_URL+"/v1/accounts/"+str(account_number)+"/positions",headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)



def account_history(access_token=ACCESS_TOKEN,account_number=ACCOUNT_NUMBER):
    r=requests.get(BROKERAGE_API_URL+"/v1/accounts/"+str(account_number)+"/history",headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)



def account_costbasis(access_token=ACCESS_TOKEN,account_number=ACCOUNT_NUMBER):
    r=requests.get(BROKERAGE_API_URL+"/v1/accounts/"+str(account_number)+"/gainloss",headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)


def account_orders(access_token=ACCESS_TOKEN,account_number=ACCOUNT_NUMBER):
    r=requests.get(BROKERAGE_API_URL+"/v1/accounts/"+str(account_number)+"/orders",headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)


def account_specificorders(order_id,access_token=ACCESS_TOKEN,account_number=ACCOUNT_NUMBER):
    r=requests.get(BROKERAGE_API_URL+"/v1/accounts/"+str(account_number)+"/orders/"+str(order_id),headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)
    


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


def intraday_status(access_token=ACCESS_TOKEN):
    r=requests.get(BROKERAGE_API_URL+"/v1/markets/clock",headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)


def time_and_sales(symbol,interval='tick',access_token=ACCESS_TOKEN):
    

    r=requests.get(BROKERAGE_API_URL+"/v1/markets/timesales?symbol="+str(symbol),headers=get_headers(access_token),stream=True)
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








