import pytest

from running_sum import solution

inputs = [
    ([1, 2, 3, 4], [1, 3, 6, 10]),
    ([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]),
    ([3, 1, 2, 10, 1], [3, 4, 6, 16, 17])
]


@pytest.mark.parametrize("input, expected", inputs)
def test_running_sum(input, expected):
    assert expected == solution(input)
