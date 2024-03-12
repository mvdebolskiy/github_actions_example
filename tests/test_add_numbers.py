import pytest
from model import add_numbers


def test_add_two_integers():
    assert add_numbers.add_two_integers(3, 4) == 7


#@pytest.mark.xfail(reason="This test MUST fail")
def test_add_two_str():
    """Test will fail!"""
    assert add_numbers.add_two_integers("3", "4") == 7
    # with pytest.raises(TypeError, match="Only integers are allowed"):
    #     add_numbers.add_two_integers('3', '4')

def test_against_kgo():
    "Regression testing"
    fl = open("./data/baseline.txt","r")
    c = fl.read()
    c = c.split()
    for i in range(0,len(c)):
        c.append(int(c[0]))
        c.pop(0)
    assert add_numbers.add_two_integers(c[0],c[1]) == c[2]