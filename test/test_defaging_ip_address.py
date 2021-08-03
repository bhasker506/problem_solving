import pytest
from defanging_ip_address import solution

inputs = [
    ("1.1.1.1", "1[.]1[.]1[.]1"),
    ("255.100.50.0", "255[.]100[.]50[.]0")
]


@pytest.mark.parametrize("input, expected", inputs)
def test_running_sum(input, expected):
    assert expected == solution(input)