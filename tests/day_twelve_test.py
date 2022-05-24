from aoc_2015.day_twelve import JsonExplorer
import pytest

cases = [pytest.param(False, 1990), pytest.param(True, 1837)]


@pytest.mark.parametrize("ignore_red,expected", cases)
def test_read_json(ignore_red, expected):
    # Arrange and Act
    explorer = JsonExplorer("./tests/test_data/day_twelve.json", ignore_red)
    # Assert
    assert explorer.integer_sum == expected
