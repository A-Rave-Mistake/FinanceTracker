from FTracker.GUI.EntryAdd import EntryAdd


EntryAddTest = EntryAdd(None, None, None, [])


# ---- Correct Values ---- #

def test_correct_values_with_amount_as_float():
    entry = EntryAddTest.is_entry_valid(name="Groceries", amount=55.0)
    assert entry is True

def test_entry_with_amount_as_zero():
    entry = EntryAddTest.is_entry_valid(name="Fuel", amount=0.0)
    assert entry is True


# ---- Incorrect Values ---- #

def test_entry_with_empty_name():
    entry = EntryAddTest.is_entry_valid(name="", amount=123.0)
    assert entry is False

def test_entry_with_name_as_int():
    entry = EntryAddTest.is_entry_valid(name=1234, amount=123.0)
    assert entry is False

def test_correct_values_with_amount_as_int():
    entry = EntryAddTest.is_entry_valid(name="Gas", amount=123)
    assert entry is False

def test_entry_with_amount_as_string():
    entry = EntryAddTest.is_entry_valid(name="Fuel", amount="123")
    assert entry is False

def test_with_amount_as_int():
    entry = EntryAddTest.is_entry_valid(name="Groceries", amount=123)
    assert entry is False

def test_entry_with_both_incorrect_inputs():
    entry = EntryAddTest.is_entry_valid(name="", amount="")
    assert entry is False