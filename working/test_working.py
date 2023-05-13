import pytest
from working import convert
def test_wrong_empty_one():
    with pytest.raises(ValueError):
        convert("24:19 PM - 24:00 AM")
        convert("")
        convert("1")
        convert("25")

def test_25pm_am():
    with pytest.raises(ValueError):
        convert("25 AM to 25 PM")
        convert("25 AM - 25 PM")
        convert("25 - 25")

def test_25():
    with pytest.raises(ValueError):
        convert("25:00 AM to 25:00 PM")

def test_out_of_range_min():
    with pytest.raises(ValueError):
        convert("2:191 AM to 3:022 PM")

def test_out_of_range():
    with pytest.raises(ValueError):
        convert("07:00 AM to 12:00 PM")
        convert("12:00 AM to 12:00 PM")
        convert("9:00 AM to 02:00 PM")
        convert("7:60 AM to 12:85 PM")

def test_spaces_score():
    with pytest.raises(ValueError):
        convert("-1:-1 AM to -1:-1 PM")
        convert("10 am to 1 pm")
        convert("10am to 1pm")
        convert("10 AM to 1 pm")
        convert("10 am to 1 PM")
        convert("10:01 am to 1:19 pm")
        convert("10:01 AM to 1:19 pm")
        convert("10:01 am to 1:19 PM")
        convert("10:01am to 1:19pm")

def test_omits_to():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_words():
    with pytest.raises(ValueError):
        convert("scarf AM to love PM")
        convert("scarf love")
        convert("AM to PM")

def test_format():
    assert convert("2:19 PM to 8:00 AM") == "14:19 to 08:00"
def test_no_minutes():
    assert convert("7 AM to 11 PM") == "07:00 to 23:00"
