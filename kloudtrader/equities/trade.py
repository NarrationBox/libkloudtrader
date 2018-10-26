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
ACCOUNT_NUMBER=os.environ['TRADIER_ACCOUNT_NUMBER']



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









