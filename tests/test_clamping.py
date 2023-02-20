import pytest

from FTracker.utils import clamping



# ---- Correct Values ---- #

# Test will pass if it doesn't raise an exception

def test_with_correct_input_dot():
    clamping.string_to_float("50.5")

def test_with_correct_input_comma():
    clamping.string_to_float("33,33")

def test_with_correct_input_int_representation():
    clamping.string_to_float("123")


# ---- Incorrect Values ---- #

# Tests below take incorrect input and should raise an exception
# 'TypeError' exception occurs when input argument is not of type str

def test_with_incorrect_type_int():
    with pytest.raises(TypeError):
        clamping.string_to_float(165)

def test_with_incorrect_type_float():
    with pytest.raises(TypeError):
        clamping.string_to_float(12.75)