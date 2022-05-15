from aoc_2015.day_nine import find_shortest_path, generate_distance_matrix


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


def test_find_shortest_path():
    # Arrange
    distance_matrix, _ = generate_distance_matrix(distances)
    # Act
    shortest_path = find_shortest_path(distance_matrix)
    # Assert
    assert shortest_path == 605
