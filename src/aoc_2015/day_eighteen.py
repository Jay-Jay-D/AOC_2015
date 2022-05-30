import itertools
from pathlib import Path


def get_next_step(state, corners_stuck=False):
    next_state = []
    for row_idx, row in enumerate(state):
        new_row = [check_light(state, row_idx, col_idx) for col_idx in range(len(row))]
        next_state.append(new_row)
    if corners_stuck:
        next_state[0][0] = 1
        next_state[0][-1] = 1
        next_state[-1][0] = 1
        next_state[-1][-1] = 1
    return next_state


def check_light(state, row_idx, col_idx):
    rows = len(state)
    cols = len(state[0])
    light = state[row_idx][col_idx]
    up = max(0, row_idx - 1)
    down = min(rows, row_idx + 2)
    left = max(0, col_idx - 1)
    rigth = min(cols, col_idx + 2)
    lights_sum = (
        sum(state[r][c] for r, c in itertools.product(range(up, down), range(left, rigth))) - light
    )
    return int(light and lights_sum in [2, 3] or not light and lights_sum == 3)


def parse_grid(state):
    return [[1 if light == "#" else 0 for light in row] for row in state]


def run_grid(initial_state, steps, corners_stuck=False):
    state = get_next_step(initial_state, corners_stuck)
    for _ in range(steps - 1):
        state = get_next_step(state, corners_stuck)
    return state, sum(sum(r) for r in state)


if __name__ == "__main__":
    input_file = Path("./src/aoc_2015/input/day_eighteen.txt")
    state = [l.strip() for l in input_file.open().readlines()]
    initial_state = parse_grid(state)

    final_sate, lights_on = run_grid(initial_state, 100)
    print(f"Part 1: After 100 steps there are {lights_on} lights on.")

    final_sate, lights_on = run_grid(initial_state, 100, True)
    print(f"Part 2: After 100 steps there are {lights_on} lights on.")
