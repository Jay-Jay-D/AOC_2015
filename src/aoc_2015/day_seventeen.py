from collections import defaultdict


def find_combinations(volume, containers_sizes):
    combinations_count = 0
    container_count = defaultdict(int)
    containers = len(containers_sizes)
    for combination_number in range(1 << containers):
        binary_representation = f"{combination_number:0{containers}b}"
        container_count = 0
        combination_sum = 0
        for size, bit in zip(containers_sizes, binary_representation):
            if bit == "1":
                combination_sum += size
                container_count += 1

        if combination_sum == volume:
            combinations_count += 1
            container_count[container_count] += 1

    return combinations_count, container_count[min(container_count.keys())]


if __name__ == "__main__":
    containers_sizes = [
        33,
        14,
        18,
        20,
        45,
        35,
        16,
        35,
        1,
        13,
        18,
        13,
        50,
        44,
        48,
        6,
        24,
        41,
        30,
        42,
    ]
    combinations_count, min_container = find_combinations(150, containers_sizes)
    print(f"Part 1: Combinations {combinations_count}")
    print(f"Part 2: Min Container count {min_container}")
