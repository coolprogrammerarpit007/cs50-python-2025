from bank import value

def test_value():
    assert value("Hello") == "$0"
    assert value("hello") == "$0"
    assert value("Hello, Newman") == "$0"
    assert value("hello, World!") == "$0"
    assert value("How you doing?") == "$20"
    assert value("how you doing?") == "$20"
    assert value("What's happening?") == "$100"