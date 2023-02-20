import pytest

from FTracker.utils.clamping import string_to_float



# ---- Correct Values ---- #

def test_with_correct_input_dot():
    string_to_float("50.5")

def test_with_correct_input_comma():
    string_to_float("33,33")

def test_with_correct_input_int_representation():
    string_to_float("123")


# ---- Incorrect Values ---- #
# Tests below take incorrect input and should raise an exception
# 'TypeError' exception occurs when input argument is not of type str

def test_with_incorrect_type_int():
    with pytest.raises(TypeError):
        string_to_float(165)

def test_with_incorrect_type_float():
    with pytest.raises(TypeError):
        string_to_float(12.75)