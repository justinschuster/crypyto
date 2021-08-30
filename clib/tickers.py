import asyncio
import os
import sys
import ccxt

def fetchChartData(symbol, timeframe):
    # timestamp-open-high-low-close-volume
    exchange = ccxt.coinbasepro()

    if exchange.has['fetchOHLCV']:
        try:
            ohlcv = exchange.fetch_ohlcv(symbol, timeframe)
            time_data = []
            price_data = []
            for i in ohlcv:
                time_data.append(i[0]/1000)
                price_data.append(i[1])
            return time_data, price_data
        except KeyError as e:
            print(exchange.id, 'ccxt.fetch_ohlcv failed with:', str(e))
            return None, None