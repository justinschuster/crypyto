import pytest
import pytestqt

from cui import utils

def test_convertEpochToDatetimeType(): 
    timestamp = 154730073
    correct_dt_hour = 13
    converted = utils.convertEpochToDatetime(timestamp)
    assert type(converted) is int
    assert converted == correct_dt_hour