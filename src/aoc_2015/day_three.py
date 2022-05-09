from pathlib import Path


def deliver_gifts_with_robo_santa(directions):
    santa_gift_coordinates = get_gift_coordinates(directions[::2])
    robo_gift_coordinates = get_gift_coordinates(directions[1::2])
    return santa_gift_coordinates.union(robo_gift_coordinates)


def get_gift_coordinates(directions):
    x = 0
    y = 0
    coordinates = [(x, y)]
    for direction in directions:
        if direction == '^':
            y += 1
        elif direction == '>':
            x += 1
        elif direction == 'v':
            y += -1
        else:
            x += -1

        coordinates.append((x, y))
    return set(coordinates)


if __name__ == "__main__":
    puzzle_input = Path('./src/aoc_2015/input/day_three.txt')
    directions = puzzle_input.open().readline()
    print(
        f'Houses that received at least one present: {len(get_gift_coordinates(directions))}')
    print(
        f'Houses that received at least one present with RoboSanta: {len(deliver_gifts_with_robo_santa(directions))}')
