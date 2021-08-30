import pytest

from clib import tickers

time_frames = [
    '1m',
    '1h',
    '1d',
    '1M', # Giving KeyError
    '1y' # Giving KeyError
]

def test_fetchChartDataOutputExists():
    # Failing for timeframes 1M and 1Y
    for time_frame in time_frames:
        time_data, price_data = tickers.fetchChartData('BTC/USD', time_frame)
        assert time_data is not None
        assert price_data is not None