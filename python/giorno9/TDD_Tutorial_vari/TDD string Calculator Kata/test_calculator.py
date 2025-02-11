import pytest
from calculator import *


# GOOD TDD CYCLE
# 1. Make a test that fails
# 2. make the test pass
# 3. Refactor

def test_stringcalculator_should_return_zero_on_empy_string():
    result = stringcalculator("")
    assert result == 0

def test_stringcalculator_should_return_correct_numeric_value_on_one():
    result = stringcalculator("1")
    assert result == 1

def test_stringcalculator_should_return_correct_numeric_value_on_two():
    result = stringcalculator("2")
    assert result == 2

def test_stringcalculator_should_return_correct_numeric_value_on_three():
    result = stringcalculator("3")
    assert result == 3

def test_stringcalculator_two_comma_separated_value_return_sum():
    result = stringcalculator("3,5")
    assert result == 8

def test_stringcalculator_two_newline_separated_value_return_sum():
    result = stringcalculator("3\n5")
    assert result == 8

def test_three_numbers_delimited_either_way():
    assert stringcalculator("1,2,3") == 6
    assert stringcalculator("4\n5,6") == 15

def test_negative_numbers_throw_exception():
    with pytest.raises(ValueError, match="Negatives not allowed: -3"):
        stringcalculator("1,-3,5")

def test_numbers_greater_than_1000_are_ignored():
    assert stringcalculator("2,1001") == 2
    assert stringcalculator("1000,1") == 1001

