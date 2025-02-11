import pytest

import my_functions

# per far girare il comando da terminale
# pytest test_my_functions.py
def test_add():
    result = my_functions.add(1,4)
    assert result == 5

def test_add_string():
    result = my_functions.add("I like ", "burgers")
    assert result == "I like burgers"
    
def test_divide():
    result = my_functions.divide(6,2)
    assert result == 3

def test_divide_byzero():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(6, 0)
