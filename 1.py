import libkloudtrader.stocks as stocks

list_of_exchanges=['all','nyse','nasdaq','amex']
for x in list_of_exchanges:
    print(stocks.list_of_companies(x))