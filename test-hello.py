from hello import add


def test_hello():
    result = add(1, 2)
    assert result == 3
