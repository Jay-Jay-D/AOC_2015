import pytest
from aoc_2015.day_three import deliver_gifts_with_robo_santa, get_gift_coordinates

direction_cases = [
    pytest.param('>', 2, 2, id='case 1'),
    pytest.param('^>v<', 4, 3, id='case 2'),
    pytest.param('^v^v^v^v^v', 2, 11, id='case 3'),
    pytest.param('^v', 2, 3, id='case 4')
]


@pytest.mark.parametrize("directions,expected,expected_with_robo", direction_cases)
def test_gift_delivering(directions, expected, expected_with_robo):
    assert len(get_gift_coordinates(directions)) == expected
    assert len(deliver_gifts_with_robo_santa(directions)) == expected_with_robo
