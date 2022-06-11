from aoc_2015.day_twenty_four import get_groups


expected_groups = [{11, 9}, {10, 8, 2}, {7, 5, 4, 3, 1}]


def test_find_groups():
    # Arrange
    packages = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
    # Act
    actual_groups = get_groups(packages)
    # Arrange
    assert expected_groups == actual_groups
