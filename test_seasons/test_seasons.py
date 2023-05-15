from seasons import count
import pytest

def test_standard():
    assert count("2022-05-15") == "Five hundred twenty-five thousand, six hundred minutes"
def test_error():
    with pytest.raises(SystemExit):
        count("12-03-1994")
        count("12/03/1994")
        count("03/31/1994")
        count("1994/03/31")