#Import all the modules that require testing
from  programs.monday_challenge import alphasort
from  programs.fibonaci_seqience import fibonaci
from  programs.count import count
from programs.factorial import fact
#Write the test for each module below.

def test_alphasort():
    assert alphasort("hello world and hello again") == {'again', 'and', 'hello', 'world'}
    assert alphasort("passing some gibberish") == {'gibberish', 'passing', 'some'}

def test_fibonaci():
    assert fibonaci(5) == 5

def test_count_zeros():
	assert count([0,0,0],0)==3

def test_count_string():
	assert count(["a","a","a"],"a")==3

def test_count_minus():
	assert count([-1,-3,-5,-4], -1)==1

def test_count_normalNum():
	assert count([1,2,3,4,5,6,6,5,4,3,2,1], 1)==2

def test_count_mixString():
    assert count(["a","a","a","b","b","z","b","c","b"],"b")==4

def test_fact1():
    assert fact(0)==1

def test_fact2():
    assert fact(5)==120
    
def test_fact3():
    assert fact(7)==5040

def test_fact4():
    assert fact(8)==40320

def test_fact5():
    assert fact(10)==3628800

