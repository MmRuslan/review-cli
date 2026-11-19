from review import next_interval


def test_correct_from_3():
    assert next_interval(3,True) == 7


def test_wrong_from_7():
    assert next_interval(7, False) == 1
def test_correct_from_21():
    assert next_interval(21, True) == None