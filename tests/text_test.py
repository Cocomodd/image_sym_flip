import pytest
from flip.text_functions import flip, get_half_str, sym_left, sym_right


@pytest.mark.parametrize("test_input,expected", [
    ("1234", "4321"),
    ("12345", "54321"),
    ("abcdef", "fedcba"),
    ("123456", "654321"),
])
def test_flip(test_input, expected):
    assert flip(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [
    ("1234", "12"),
    ("12345", "123"),
    ("abcdef", "abc"),

])
def test_get_half_str(test_input, expected):
    assert get_half_str(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [
    ("1234", "1221"),
    ("12345", "12321"),
    ("abcdef", "abccba"),
    ("123456", "123321"),

])
def test_sym_left(test_input, expected):
    assert sym_left(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [
    ("1234", "4334"),
    ("12345", "54345"),
    ("abcdef", "feddef"),

])
def test_sym_right(test_input, expected):
    assert sym_right(test_input) == expected

