from pathlib import Path


def deliver_gifts_with_robo_santa(directions):
    santa_gift_coordinates = get_gift_coordinates(directions[::2])
    robo_gift_coordinates = get_gift_coordinates(directions[1::2])
    houses = set(santa_gift_coordinates.keys()).union(set(robo_gift_coordinates.keys()))
    return len(houses)


def get_gift_coordinates(directions):
    x=0
    y=0    
    coordinates = {(x,y):1}
    for direction in directions:
        if direction == '^':
            y+=1
        elif direction == '>':
            x+=1
        elif direction == 'v':
            y+=-1
        else:
            x+=-1

        next_coordinate = (x, y)
        if next_coordinate in coordinates:
            coordinates[next_coordinate] += 1
        else:
            coordinates[next_coordinate] = 1
    return coordinates
    #return sum([1 for house in coordinates.values() if house >= 1])

if __name__ == "__main__":
    puzzle_input = Path('./src/aoc_2015/day_three_input.txt')
    directions = puzzle_input.open().readline()
    print(f'Houses that received at least one present: {len(get_gift_coordinates(directions))}')
    print(f'Houses that received at least one present with RoboSanta: {deliver_gifts_with_robo_santa(directions)}')
