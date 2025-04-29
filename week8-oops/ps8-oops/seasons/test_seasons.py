import pytest
from seasons import main,is_valid_date,get_minutes

def test_is_valid():
    assert is_valid_date("2024-04-29") == True
    assert is_valid_date("2021-04-29") == True
    assert is_valid_date("2021/04/29") == False
    assert is_valid_date("2021-jan-20") == False
    assert is_valid_date("2021-13-36") == False