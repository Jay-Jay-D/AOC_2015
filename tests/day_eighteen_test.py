from aoc_2015.day_eighteen import get_next_step, parse_grid

initial_state = [
    ".#.#.#",
    "...##.",
    "#....#",
    "..#...",
    "#.#..#",
    "####..",
]

step_one = [
    "..##..",
    "..##.#",
    "...##.",
    "......",
    "#.....",
    "#.##..",
]


def test_parse_lights_state():
    # Arrange
    expected_state = [
        [0, 1, 0, 1, 0, 1],
        [0, 0, 0, 1, 1, 0],
        [1, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 0, 0],
    ]
    # Act
    actual_state = parse_grid(initial_state)
    # Assert
    assert expected_state == actual_state


def test_get_next_state():
    # Act
    next_step = get_next_step(parse_grid(initial_state))
    # Assert
    assert parse_grid(step_one) == next_step
