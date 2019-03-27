from time import sleep
import json
import requests 
import os
from .defaults import *
import pandas as pd

BROKERAGE_API_URL="https://api.tradier.com"

def get_headers(access_token):
    headers = {"Accept":"application/json",
           "Authorization":"Bearer "+access_token}
    return headers



def user_profile(access_token=ACCESS_TOKEN,pandas=False):
    r=requests.get(BROKERAGE_API_URL+"/v1/user/profile",headers=get_headers(access_token))
    try:
        if pandas==False:
            return r.json()
        else:
            return pd.DataFrame(r.json()['profile']['account'])
    except: 
        raise Exception("Did not receive any data. Status Code: %d"%r.status_code
        )

def user_account_number(access_token=ACCESS_TOKEN,pandas=False):
    r=requests.get(BROKERAGE_API_URL+"/v1/user/profile",headers=get_headers(access_token))
    try:
        data=r.json()['profile']['account']
        account_numbers=[row['account_number'] for row in data]
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
    
