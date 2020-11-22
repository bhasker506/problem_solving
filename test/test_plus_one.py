import pytest
from plus_one import solution

inputs = [
    ([1, 2, 3], [1, 2, 4]),
    ([1, 2, 9], [1, 3, 0]),
    ([0], [1]),
    ([9], [1, 0]),
    ([9, 9], [1, 0, 0])
]


@pytest.mark.parametrize("input, expected", inputs)
def test_reverse_number(input, expected):
    assert expected == solution(input)