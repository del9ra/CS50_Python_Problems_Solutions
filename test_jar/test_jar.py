from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12

def test_init_error():
    with pytest.raises(ValueError):
        jar = Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪"

def test_deposit_error():
    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(300)

def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(4)
    assert jar.size == 6

def test_withdraw_error():
    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(5)
        jar.withdraw(8)