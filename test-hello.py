from hello import add, hello

def test_hello():
    result = hello()
    assert result == "hello"
def test_subtract():
    result = subtract(2, 1)
    assert result == 1
def test_add():
    result = add(1, 2)
    assert result == 3
