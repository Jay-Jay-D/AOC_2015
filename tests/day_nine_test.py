import pytest
from aoc_2015.day_nine import find_path, generate_distance_matrix


distances = ["London to Dublin = 464", "London to Belfast = 518", "Dublin to Belfast = 141"]


def test_distance_matrix():
    distance_matrix, _ = generate_distance_matrix(distances)
    assert distance_matrix[0][0] == 0
    assert distance_matrix[1][1] == 0
    assert distance_matrix[2][2] == 0
    assert distance_matrix[0][1] == 464
    assert distance_matrix[1][0] == 464
    assert distance_matrix[0][2] == 518
    assert distance_matrix[2][0] == 518
    assert distance_matrix[1][2] == 141
    assert distance_matrix[2][1] == 141


cases = [
    pytest.param(True, 605, id="Shortest path case"),
    pytest.param(False, 982, id="Longest path case"),
]


@pytest.mark.parametrize("shortest,expected_distance", cases)
def test_find_shortest_path(shortest, expected_distance):
    # Arrange
    distance_matrix, _ = generate_distance_matrix(distances)
    # Act
    actual_distance, _ = find_path(distance_matrix, shortest)
    # Assert
    assert actual_distance == expected_distance
