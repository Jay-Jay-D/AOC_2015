from functools import reduce
from itertools import combinations
from operator import mul
from pathlib import Path


def get_groups(packages, group_count=3):
    total_weight = sum(packages)
    group_weight = total_weight / group_count
    groups = [
        # packages, # packages, product packages
        (set(seq), len(seq), reduce(mul, seq, 1))
        for i in range(len(packages) - group_count, 0, -1)
        for seq in combinations(packages, i)
        if sum(seq) == group_weight
    ]
    groups = sorted(groups, key=lambda x: (x[1], x[2]))
    groups_in_sleigh = [groups[0][0]]
    for group in groups:
        if any(bool(group[0] & group_in_sleigh) for group_in_sleigh in groups_in_sleigh):
            continue
        else:
            groups_in_sleigh.append(group[0])
    return groups_in_sleigh


if __name__ == "__main__":
    puzzle_input = Path("./src/aoc_2015/input/day_twenty_four.txt")
    packages = [int(line.strip()) for line in puzzle_input.open().readlines()]
    groups_in_sleigh = get_groups(packages)
    quantum_entanglement = reduce(mul, groups_in_sleigh[0], 1)
    print(
        f"Part 1: The quantum entanglement of the first group of packages is {quantum_entanglement}"
    )
    groups_in_sleigh = get_groups(packages, 4)
    quantum_entanglement = reduce(mul, groups_in_sleigh[0], 1)
    print(
        f"Part 2: The quantum entanglement of the first group of packages is {quantum_entanglement}"
    )
