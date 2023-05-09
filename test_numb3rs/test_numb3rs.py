from numb3rs import validate

def test_max():
    assert validate("255.255.255.255") == True
def test_more_than_max():
    assert validate("256.300.1000.555") == False
def test_different_value():
    assert validate("horse") == False
def test_min():
    assert validate("0.0.0.0") == True
def test_first():
    assert validate("277.20.16.1") == False
    assert validate("15.299.493.678") == False