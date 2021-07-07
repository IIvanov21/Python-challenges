from programs.vowels import vowels

def test_vowel1():
    assert vowels("potato") == 3

def test_vowel2():
    assert vowels("test") == 1

def test_vowel3():
    assert vowels("concatinate") == 5

def test_vowel4():
    assert vowels("fourty") == 2

def test_vowel5():
    assert vowels("toilet") == 3