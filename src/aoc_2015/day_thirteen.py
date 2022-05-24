from itertools import permutations


def parse_line(line):
    line_parts = line.split(" ")
    person_a = line_parts[0]
    person_b = line_parts[-1][:-1]
    happiness = int(line_parts[3])
    if line_parts[2] == "lose":
        happiness *= -1
    return person_a, person_b, happiness


def generate_matrix(potential_happiness):
    happiness_dict = {}
    name_index = {}
    idx = 0
    for line in potential_happiness:
        person_a, person_b, happiness = parse_line(line)
        for person in [person_a, person_b]:
            if person not in name_index.keys():
                name_index[person] = idx
                idx += 1
        happiness_dict[name_index[person_a], name_index[person_b]] = happiness

    happiness_matrix = [[0] * idx for _ in range(idx)]

    for i, j in permutations(range(idx), 2):
        happiness_matrix[i][j] = happiness_dict[(i, j)]
    return happiness_matrix, name_index
