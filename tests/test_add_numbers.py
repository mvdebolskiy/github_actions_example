from model import add_numbers

def test_add_two_integers():
    assert add_numbers.add_two_integers(3,4) == 7

# def test_add_two_str():
#     """Test will fail!"""
#     assert add_numbers.add_two_integers('3','4') == 7