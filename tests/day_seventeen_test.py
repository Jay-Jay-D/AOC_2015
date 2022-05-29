from aoc_2015.day_seventeen import find_combinations


containers_sizes = [20, 15, 10, 5, 5]


def test_find_combinations():
    combinations_count, min_container = find_combinations(25, containers_sizes)
    assert combinations_count == 4
    assert min_container == 3
