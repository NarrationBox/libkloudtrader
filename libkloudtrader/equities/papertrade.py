from time import sleep
from requests import get,post
import sys
sys.path.append("..")
from libkloudtrader.defaults import PT_ACCESS_TOKEN,PT_ACCOUNT_NUMBER

API_URL="http://127.0.0.1:8000/"


def get_headers(access_token):
    headers = {
    'accept': 'application/json',
    'PT_ACCESS_TOKEN': access_token,
    }
    return headers
    


'''Account related wrappers'''
def account_info(access_token=PT_ACCESS_TOKEN,account_number=PT_ACCOUNT_NUMBER):
    response=get(API_URL+"account_info/"+str(account_number),headers=get_headers(access_token))
    try:
        return response.json()
    except:
        raise ("Did not recieve any data. Status Code: {}".format(response.status_code))

'''Trading related wrappers'''
def buy(symbol,quantity,access_token=PT_ACCESS_TOKEN,account_number=PT_ACCOUNT_NUMBER,asset_class="equity",order_type="market",duration="day",stop=None,price=None):
    payload={
    "account_number":account_number,
    "asset_class": asset_class,
     "side": "buy",
     "symbol": symbol,
     "order_type": order_type,
     "quantity": quantity,
     "duration": duration,
    "price": price,
    "stop": stop
    }
    response=post(API_URL+"order",headers=get_headers(access_token),json=payload)
    try:
        return response.json()
    except:
        raise ("Did not recieve any data. Status Code: {}".format(response.status_code))


def sell(symbol,quantity,access_token=PT_ACCESS_TOKEN,account_number=PT_ACCOUNT_NUMBER,asset_class="equity",order_type="market",duration="day",stop=None,price=None):
    payload={
    "account_number":account_number,
    "asset_class": asset_class,
     "side": "sell",
     "symbol": symbol,
     "order_type": order_type,
     "quantity": quantity,
     "duration": duration,
    "price": price,
    "stop": stop
    }
    response=post(API_URL+"order",headers=get_headers(access_token),json=payload)
    try:
        return response.json()
    except:
        raise ("Did not recieve any data. Status Code: {}".format(response.status_code))






















''' data related wrappers'''
def get_all_quotes():
    response=get(API_URL+"quotes")
    try:
        return response.json()
    except:
        raise ("Did not recieve any data. Status Code: {}".format(response.status_code))


def get_quotes(symbol):
    response=get(API_URL+"quotes/"+symbol)
    try:
        return response.json()
    except:
        raise ("Did not recieve any data. Status Code: {}".format(response.status_code))

def get_all_trades():
    response=get(API_URL+"trades/")
    try:
        return response.json()
    except:
        raise ("Did not recieve any data. Status Code: {}".format(response.status_code))

def get_trades(symbol):
    response=get(API_URL+"trades/"+symbol)
    try:
        return response.json()

            
    except:
        raise ("Did not recieve any data. Status Code: {}".format(response.status_code))

