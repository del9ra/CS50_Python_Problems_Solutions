from fuel import convert, gauge
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError) as e_info:
        if convert("1/0"):
            raise ZeroDivisionError("Error")
def test_value():
    with pytest.raises(ValueError) as exc_info:
        if convert("cat/dog"):
            raise ValueError("value must be int")
def test_value_bigger_x():
    with pytest.raises(ValueError) as exc_info:
        if convert("5/4"):
            raise ValueError("x must be less than y")
def test_empty_gauge():
    assert gauge(convert("1/100")) == "E" #добавила gauge(convert(s)) чтобы тестировать все функции сразу
def test_full():
    assert gauge(convert("99/100")) == "F"
def test_percent_gauge():
    assert gauge(convert("1/4")) == "25%"
    assert gauge(convert("1/2")) == "50%"