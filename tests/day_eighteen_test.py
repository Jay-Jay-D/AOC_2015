import pytest

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


def get_next_step(state):
    rows = len(state)
    cols = len(state[0])
    next_state = []
    for row_idx, row in enumerate(state):
        new_row = []
        up = max(0, row_idx - 1)
        down = min(rows, row_idx + 2)
        for col_idx, light in enumerate(row):
            left = max(0, col_idx - 1)
            rigth = min(cols, col_idx + 2)

            lights_sum = 0
            for x in range(left, rigth):
                for y in range(up, down):
                    lights_sum += state[y][x]
            lights_sum -= light

            if light:
                if lights_sum in [2, 3]:
                    new_row.append(1)
                else:
                    new_row.append(0)
            else:
                if lights_sum == 3:
                    new_row.append(1)
                else:
                    new_row.append(0)
        next_state.append(new_row)
    return next_state


def parse_grid(state):
    return [[1 if light == "#" else 0 for light in row] for row in state]
