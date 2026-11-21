import pytest 
from review import next_interval
import pytest 
from review import next_interval
from review import load_questions 


def test_correct_from_3():
    assert next_interval(3,True) == 7


def test_wrong_from_7():
    assert next_interval(7, False) == 1
def test_correct_from_21():
    assert next_interval(21, True) == None

def test_unknown_interval():
    with pytest.raises(ValueError):
        next_interval(5, True)

def test_load_missing_file():
    assert load_questions("no_such_file.json") == FileNotFoundError

def test_correct_from_3():
    assert next_interval(3,True) == 7


def test_wrong_from_7():
    assert next_interval(7, False) == 1
def test_correct_from_21():
    assert next_interval(21, True) == None

def test_unknown_interval():
    with pytest.raises(ValueError):
        next_interval(5, True)

def test_load_missing_file():
    assert load_questions("no_such_file.json") == []