from itertools import permutations
from math import inf
from pathlib import Path


def parse_line(line):
    line_parts = line.strip().split(" ")
    person_a = line_parts[0]
    # remove period after lasta name.
    person_b = line_parts[-1][:-1]
    happiness = int(line_parts[3])
    if line_parts[2] == "lose":
        happiness *= -1
    return person_a, person_b, happiness


def generate_matrix(potential_happiness):
    happiness_dict = {}
    name_to_index = {}
    index_to_name = {}
    idx = 0
    for line in potential_happiness:
        person_a, person_b, happiness = parse_line(line)
        for person in [person_a, person_b]:
            if person not in name_to_index.keys():
                name_to_index[person] = idx
                index_to_name[idx] = person
                idx += 1
        happiness_dict[name_to_index[person_a], name_to_index[person_b]] = happiness

    happiness_matrix = [[0] * idx for _ in range(idx)]

    for i, j in permutations(range(idx), 2):
        happiness_matrix[i][j] = happiness_dict[(i, j)]
    return happiness_matrix, index_to_name


def get_optimal_seating_arrangement(potential_happiness):
    happiness_matrix, index_to_name = generate_matrix(potential_happiness)
    guests_count = len(index_to_name)
    max_happiness = -inf
    max_happiness_arrange = None
    for arrange in permutations(range(guests_count)):
        arrange_happiness = 0
        for position in range(guests_count):
            guest = arrange[position]  # <- row
            left_guest = arrange[position - 1]
            right_guest = arrange[position + 1 if position + 1 < guests_count else 0]
            arrange_happiness += (
                happiness_matrix[guest][left_guest] + happiness_matrix[guest][right_guest]
            )
        if arrange_happiness > max_happiness:
            max_happiness = arrange_happiness
            max_happiness_arrange = [index_to_name[guest] for guest in arrange]
    return max_happiness_arrange, max_happiness


if __name__ == "__main__":
    input_file = Path("./src/aoc_2015/input/day_thirteen.txt")
    potential_happiness = input_file.open().readlines()
    max_happiness_arrange, max_happiness = get_optimal_seating_arrangement(potential_happiness)
    print(f"Part 1: Best arrange {' -> '.join(max_happiness_arrange)}")
    print(f"Part 1: Best arrange happiness {max_happiness}")
