import pytest
from calculator import square



def test_square():
    assert square(5) == 25
    assert square(-5) == 25
    assert square(0) == 0
    assert square(1) == 1
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16


def test_str():
    with pytest.raises(TypeError):
        square("cat")