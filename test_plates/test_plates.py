from plates import is_valid

def test_alphabetical():
    assert is_valid("892596") == False
def test_number_placement():
    assert is_valid("AAA22A") == False
def test_zero_placement():
    assert is_valid("CS05") == False
def test_length():
    assert is_valid("OUTATIME") == False
def test_alphanum():
    assert is_valid("PI3.14") == False #для проверки добавили пунктуацию кроме букв и чисел