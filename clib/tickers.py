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
    return ohlcv