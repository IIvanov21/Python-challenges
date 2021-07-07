from programs.list_of_squares import list_of_squares

def test_list1():
    assert list_of_squares(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

def test_list2():
    assert list_of_squares(6) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

def test_list3():
    assert list_of_squares(7) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

def test_list4():
    assert list_of_squares(8) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

def test_list5():
    assert list_of_squares(9) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}