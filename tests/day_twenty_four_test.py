import pytest
from aoc_2015.day_twenty_four import get_groups


expected_groups_cases = [
    pytest.param([{11, 9}, {10, 8, 2}, {7, 5, 4, 3, 1}], 3),
    pytest.param([{11, 4}, {10, 5}, {9, 2, 3, 1}, {8, 7}], 4),
]


@pytest.mark.parametrize("expected_groups, group_count", expected_groups_cases)
def test_find_groups(expected_groups, group_count):
    # Arrange
    packages = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
    # Act
    actual_groups = get_groups(packages, group_count)
    # Arrange
    assert len(expected_groups) == len(actual_groups)
    assert all(group in expected_groups for group in actual_groups)
