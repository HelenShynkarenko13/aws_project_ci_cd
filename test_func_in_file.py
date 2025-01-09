# test_func_in_file.py
from func_in_file import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    
    assert subtract(3, 5) == -2

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0

def test_divide():
    assert divide(10, 5) == 2
    assert divide(9, 3) == 3
    try:
        divide(5, 0)
    except ValueError as e:
        assert str(e) == "Division by zero is not allowed."
