import pytest
from aoc_2015.day_two import get_box_papper_and_ribbon

suface_area_cases = [
    pytest.param('2x3x4', 58, 34, id='case 1'),
    pytest.param('1x1x10', 43, 14, id='case 2'),
    pytest.param('4x23x21', 1402, 1982, id='case 3'),
]


@pytest.mark.parametrize("side_lengths,expected_area,expected_ribbon", suface_area_cases)
def test_get_box_surface_area(side_lengths, expected_area, expected_ribbon):
    assert get_box_papper_and_ribbon(side_lengths) == (
        expected_area, expected_ribbon)
