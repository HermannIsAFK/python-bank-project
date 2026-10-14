def multiply(a, b):
    return a * b

def test_positive_numbers():
    result = multiply(2, 3)
    assert result == 6

def test_negative_number():
    result = multiply(-2, 3)
    assert result == -6

def test_zero():
    result = multiply(0, 3)
    assert result == 0