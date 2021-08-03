import pytest

from roman_integer import solution

inputs = [
    ('III', 3),
    ('IV', 4),
    ("IX", 9),
    ("LVIII", 58),
    ("MCMXCIV", 1994),

]


@pytest.mark.parametrize("input, expected", inputs)
def test_roman_number(input, expected):
    assert expected == solution(input)