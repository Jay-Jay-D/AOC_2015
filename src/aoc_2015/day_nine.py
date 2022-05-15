from itertools import combinations, permutations
from math import inf


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

    return distance_matrix, place_index


def find_shortest_path(distance_matrix):
    places = len(distance_matrix)
    shortest_path = inf
    for route in permutations(range(places)):
        route_length = sum(distance_matrix[route[idx - 1]][route[idx]] for idx in range(1, places))
        if route_length < shortest_path:
            shortest_path = route_length
    return shortest_path
