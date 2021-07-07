#Import all the modules that require testing
from  programs.monday_challenge import alphasort
from  programs.fibonaci_seqience import fibonaci
#Write the test for each module below.

def test_alphasort():
    assert alphasort("hello world and hello again") == {'again', 'and', 'hello', 'world'}
    assert alphasort("passing some gibberish") == {'gibberish', 'passing', 'some'}

def test_fibonaci():
    assert fibonaci(5) == 5