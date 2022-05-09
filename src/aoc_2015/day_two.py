from itertools import combinations
from pathlib import Path


def get_box_papper_and_ribbon(suface_area):
    [a, b, c] = sorted([int(s) for s in suface_area.split('x')])
    return (2*a*b + 2*b*c + 2*a*c) + (a*b), (2*a + 2*b) + (a*b*c)


if __name__ == "__main__":
    puzzle_input = Path('./src/aoc_2015/input/day_two.txt')
    gifts = puzzle_input.open().readlines()
    total_area = 0
    total_ribbon = 0
    for side_lengths in gifts:
        papper, ribbon = get_box_papper_and_ribbon(side_lengths)
        total_area += papper
        total_ribbon += ribbon
    print(f'Total square feet of wrapping paper to order: {total_area}')
    print(f'Total feet of ribbon to order: {total_ribbon}')
