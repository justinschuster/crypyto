import asyncio
import os
import sys
import ccxt

# Only BTC/USD Symbol for now.
symbol = 'BTC/USD'

# Only Coinbase Pro for now.

def fetchChartData(symbol, timeframe):
    # timestamp-open-high-low-close-volume
    exchange = ccxt.coinbasepro()
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe)
    time_data = []
    price_data = []
    for i in ohlcv:
        time_data.append(i[0]/1000)
        price_data.append(i[1])
    return time_data, price_data