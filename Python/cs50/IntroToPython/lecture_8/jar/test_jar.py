import pytest 
from jar import Jar

def test_init():
     jar = Jar(15)
     assert jar.capacity == 15

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    assert jar.size == 0

    jar.deposit(2)
    assert jar.size == 2

    with pytest.raises(ValueError):
        jar.deposit(-1)

    with pytest.raises(ValueError):
        jar.deposit(20)

def test_withdraw():
    jar = Jar(10)

    # empty jar
    with pytest.raises(ValueError):
        jar.withdraw(1)    

    with pytest.raises(ValueError):
        jar.withdraw(-1)

    # lets 'hack' a size so we don't rely on deposit
    # fill the jar
    jar._size = 10
    jar.withdraw(5)
    assert jar.size == 5

