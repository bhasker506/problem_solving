import pytest
from problems.reverse_integer import solution

inputs = [
    (123, 321),
    (-123, -321),
    (120, 21),
    (0, 0)
]


@pytest.mark.parametrize("input, expected", inputs)
def test_reverse_number(input, expected):
    assert expected == solution(input)
