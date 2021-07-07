from programs.even_numbers import even_digits

def test_even1():
    assert even_digits(10,20) == [10, 12, 14, 16, 18]

def test_even2():
    assert even_digits(15,20) == [16, 18]    

def test_even3():
    assert even_digits(21,35) == [22, 24, 26, 28, 30, 32, 34]  

def test_even4():
    assert even_digits(18,24) == [18, 20, 22]  

def test_even5():
    assert even_digits(2,10) == [2, 4, 6, 8]  