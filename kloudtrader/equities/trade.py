#Trading apis

#TODO:
'''
time_and_sales()
options and multileg order support
improve error and exception handling
'''
from time import sleep
import json
import requests 
import os


SANDBOX_API_URL="https://sandbox.tradier.com"
BROKERAGE_API_URL="https://api.tradier.com"
STREAMING_API_URL="https://stream.tradier.com"
ACCESS_TOKEN = os.environ['TRADIER_ACCESS_TOKEN']
CONSUMER_KEY=os.environ['TRADIER_CONSUMER_KEY']



def get_headers(access_token):
    headers = {"Accept":"application/json",
           "Authorization":"Bearer "+access_token}
    return headers



'''Trading'''
#Equity
def buy_preview(access_token,account_number,symbol,quantity,duration="day",action="buy",order_type="market",price=None):
    post_params={
        'class':'equity',
        'symbol':str(symbol.upper()), 
        'duration':str(duration.lower()), #time for which the order will be remain in effect (Day or GTC)
        'side':str(action), #buy or sell
        'quantity':str(quantity),
        'type':str(order_type.lower()), #market, limit, etc.
        'preview':'true'
    }
    r=requests.post(BROKERAGE_API_URL+"/v1/accounts/"+str(account_number)+"/orders/",params=post_params,headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)



def sell_preview(access_token,account_number,symbol,quantity,duration="day",action="sell",order_type="market",price=None):
    post_params={
        'class':'equity',
        'symbol':str(symbol.upper()), 
        'duration':str(duration.lower()), #time for which the order will be remain in effect (Day or GTC)
        'side':str(action), #buy or sell
        'quantity':str(quantity),
        'type':str(order_type.lower()), #market, limit, etc.
        'preview':'true'
    }
    r=requests.post(BROKERAGE_API_URL+"/v1/accounts/"+str(account_number)+"/orders/",params=post_params,headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)


def buy(access_token,account_number,symbol,quantity,duration="day",action="buy",order_type="market",price=None):
    post_params={
        'class':'equity',
        'symbol':str(symbol.upper()), 
        'duration':str(duration.lower()), #time for which the order will be remain in effect (Day or GTC)
        'side':str(action), #buy or sell
        'quantity':str(quantity),
        'type':str(order_type.lower()), #market, limit, etc.
        'price':str(price)
    }
    
    r=requests.post(BROKERAGE_API_URL+"/v1/accounts/"+str(account_number)+"/orders/",params=post_params,headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)
        

def sell(access_token,account_number,symbol,quantity,duration="day",action="sell",order_type="market",price=None):
    post_params={
        'class':'equity',
        'symbol':str(symbol.upper()), 
        'duration':str(duration.lower()), #time for which the order will be remain in effect (Day or GTC)
        'side':str(action), #buy or sell
        'quantity':str(quantity),
        'type':str(order_type.lower()), #market, limit, etc.
        'price':str(price)
    }
    
    r=requests.post(BROKERAGE_API_URL+"/v1/accounts/"+str(account_number)+"/orders/",params=post_params,headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)
       

def change_equity_order(access_token,account_number,order_id,order_type,price=None):
    put_params={
        'type':str(order_type.lower()), #limit,stop_limit
        'price':str(price)
    }
    r=requests.put(BROKERAGE_API_URL+"/v1/accounts/"+str(account_number)+"/orders/"+str(order_id),params=put_params,headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)


def cancel_equity_order(access_token,account_number,order_id):
    r=requests.delete(BROKERAGE_API_URL+"/v1/accounts/"+str(account_number)+"/orders/"+str(order_id),headers=get_headers(access_token))
    try:
        return r.json()
    except:
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code)









