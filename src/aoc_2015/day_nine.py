from itertools import combinations, permutations
from math import inf
from pathlib import Path


def generate_distance_matrix(distances):
    distance_dict = {}
    place_index = {}
    idx = 0
    for line in distances:
        places, distance = line.split(" = ")
        place_a, place_b = places.split(" to ")
        for place in [place_a, place_b]:
            if place not in place_index.keys():
                place_index[place] = idx
                idx += 1
        distance_dict[(place_index[place_a], place_index[place_b])] = int(distance)
    distance_matrix = [[0] * idx for _ in range(idx)]

    for i, j in combinations(range(idx), 2):
        distance_matrix[i][j] = distance_dict[(i, j)]
        distance_matrix[j][i] = distance_dict[(i, j)]

    return distance_matrix, list(place_index.keys())


def find_path(distance_matrix, shortest=True):
    places = len(distance_matrix)
    final_path_distance = inf if shortest else -inf
    final_path_route = None
    for route in permutations(range(places)):
        route_length = sum(distance_matrix[route[idx - 1]][route[idx]] for idx in range(1, places))
        if (shortest and route_length < final_path_distance) or (
            not shortest and route_length > final_path_distance
        ):
            final_path_distance = route_length
            final_path_route = route
    return final_path_distance, final_path_route


if __name__ == "__main__":
    input_file = Path("./src/aoc_2015/input/day_nine.txt")
    puzzle_input = input_file.open().readlines()
    puzzle_input = [l.strip() for l in puzzle_input]
    distance_matrix, place_index = generate_distance_matrix(puzzle_input)

    for type, is_shortest, part in [("Shortest", True, "1"), ("Longest", False, "2")]:
        path, path_route = find_path(distance_matrix, is_shortest)
        print(f"Part {part}: {type} path is {path}")
        route_string = " -> ".join([place_index[idx] for idx in path_route])
        print(f"Part {part}: {type}path is {route_string}")
