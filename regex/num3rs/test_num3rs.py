import pytest
from num3rs import validate

def test_validate():
    assert validate('127.0.0.1')  == True
    assert validate('255.255.255.255')  == True
    assert validate('512.512.512.512')  == False
    assert validate('1.2.3.1000')  == False
    assert validate('cat')  == False
    assert validate('1.2.3')  == False
    assert validate('75.456.76.65')  == False
