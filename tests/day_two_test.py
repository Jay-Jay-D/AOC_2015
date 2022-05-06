import pytest
from aoc_2015.day_two import position_basement

direction_cases = [
    (')', 1),
    ('()())', 5)
]

@pytest.mark.parametrize("directions,expected", direction_cases)
def test_position_basement(directions,expected):
    assert False
    assert position_basement(directions) == expected