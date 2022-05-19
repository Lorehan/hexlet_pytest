"""test reverse function"""
from hexlet_pytest.example import reverse

def test_reverse():
    """test reverse function"""
    assert reverse('Hexlet') == 'telxeH'

def test_reverse_for_empty_string():
    """test reverse function in empty string"""
    assert reverse('') == ''
