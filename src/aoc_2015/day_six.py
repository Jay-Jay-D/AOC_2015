from pathlib import Path


def decode_instruction(instruction):
    part_a, part_b = instruction.split('through')
    x_end, y_end = part_b.split(',')
    part_a = part_a.strip().split(' ')
    x_start, y_start = part_a[-1].split(',')
    order = part_a[1] if part_a[0] == 'turn' else part_a[0]
    return order, int(x_start), int(y_start), int(x_end), int(y_end)

def operate_grid(instructions, x_size=1000, y_size=1000):
    grid = [[0 for j in range (y_size)] for i in range(x_size)]
    for instruction in instructions:
        order,x_start,y_start,x_end,y_end = decode_instruction(instruction)
        for x in range(x_start, x_end+1):
            for y in range(y_start, y_end+1):
                if order == 'toggle':
                    grid[x][y] = 1 if grid[x][y] == 0 else 0
                else:
                    state = 1 if order == 'on' else 0
                    grid[x][y] = state
    return grid

def ligths_lit_sum(grid):
    lit = 0
    for row in grid:
        for cell in row:
            lit += cell
    return lit

if __name__ == "__main__":
    puzzle_input = Path('./src/aoc_2015/input/day_six.txt')
    instructions = puzzle_input.open().readlines()
    grid = operate_grid(instructions)
    print(f'How many lights are lit?: {ligths_lit_sum(grid)}')
