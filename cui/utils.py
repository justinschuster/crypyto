import datetime

def convertEpochToDatetime(t):
    return int(datetime.datetime.fromtimestamp(t/1000).strftime('%H'))