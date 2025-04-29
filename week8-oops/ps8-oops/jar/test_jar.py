import pytest
from jar import Jar



def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_str(capsys):
    jar = Jar()
    jar.deposit(5)
    print(jar)
    captured = capsys.readouterr()
    assert captured.out.strip() == "🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        assert jar.deposit(15)
    jar.deposit(5)
    jar.size == 5


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    with pytest.raises(ValueError):
        assert jar.withdraw(15)
    jar.withdraw(7)
    assert jar.size == 3