from streamz import Stream
import libkloudtrader.stocks as stocks

source = Stream()


def run(mode: str, strategy_name: str, symbols=list, states: list = ['open']):
    if mode == "live":
        print("{} is now entering the live markets. All the Best!".format(
            strategy_name.__name__))
        while stocks.intraday_status()['state'] in states:
            source.map(strategy_name).sink(print)
            for i in symbols:
                source.emit(i)
