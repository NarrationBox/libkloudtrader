import json

import numpy as np
import pandas as pd
import requests

from libkloudtrader.equities.data import (
    ACCESS_TOKEN,
    STREAMING_API_URL,
    create_session,
    get_headers,
)
from libkloudtrader.alert_me import sms_and_email
from streamz import Stream


def df_empty(columns, dtypes, index=None):
    assert len(columns) == len(dtypes)
    df = pd.DataFrame(index=index)
    for c, d in zip(columns, dtypes):
        df[c] = pd.Series(dtype=d)
    return df


def get_quotes(symbol, sessionid):
    # gets market events
    payload = {"sessionid": sessionid, "symbols": str(symbol.upper())}
    r = requests.post(
        STREAMING_API_URL + "/v1/markets/events",
        params=payload,
        headers=get_headers(ACCESS_TOKEN),
        stream=True,
    )
    print("Starting...")
    try:
        for data in r.iter_content(chunk_size=None, decode_unicode=True):
            # print(data)
            lines = data.decode("utf-8").replace("}{", "}\n{").split("\n")
            for line in lines:
                quotes = json.loads(line)
                # print(quotes)
                if quotes["type"] == "quote":
                    # row = pd.DataFrame({"quote": float(quotes["ask"])}, index=[0])
                    stream.emit(quotes["ask"])
                    on_tick()
    except:
        raise Exception("Did not receive any data. Status Code: %d" %
                        r.status_code)


# price_table = pd.DataFrame(columns=["date", "quote"], index=[0])
# price_table = df_empty(columns=["date", "quote"], dtypes=[np.datetime64, np.float64])
price_table = pd.DataFrame(columns=["quote"])
# price_table.index = pd.to_datetime(price_table.index)
# import pdb; pdb.set_trace()
# print(price_table)
stream = Stream()
# price_stream = DataFrame(stream, example=price_table)


def on_tick():

    # print(quote["askdate"], quote["ask"])
    # row = row.set_index(pd.DatetimeIndex(row["date"]))
    # price_table = price_table.set_index(pd.DatetimeIndex(price_table["date"]))
    # print(row)
    # print(price_stream)
    # stream.sink(print)
    # rows = price_stream.window(n=5).mean()
    # rows.stream.sink(print)
    # short_mavg = price_stream.quotu.sliding_window(n=2).mean()
    # long_mavg = price_stream.quote.sliding_window(n=5).mean()
    short_mavg = stream.sliding_window(n=2)
    long_mavg = stream.sliding_window(n=5)
    prices = short_mavg.zip(long_mavg).sink(crossover_condition)
    # import pdb; pdb.set_trace()
    # short_mavg.zip(long_mavg).stream.sink(print)


def crossover_condition(price):
    short_mavg = np.mean(list(price[0]))
    long_mavg = np.mean(list(price[1]))
    print("short:", short_mavg)
    print("long:", long_mavg)
    # pass
    if (long_mavg - short_mavg) > 5:
        alert = "buy! SMA: {}, LMA: {}".format(short_mavg, long_mavg)
        print(alert)
        sms_and_email("+919871766213", "chetan@kloudtrader.com", alert)
    elif (short_mavg - long_mavg) > 3:
        alert = "sell! SMA: {}, LMA: {}".format(short_mavg, long_mavg)
        print(alert)
        sms_and_email("+919871766213", "chetan@kloudtrader.com", alert)


get_quotes("AAPL", create_session(ACCESS_TOKEN))
