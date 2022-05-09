from dis import Instruction
import pytest

from aoc_2015.day_six import decode_instruction, operate_grid, ligths_lit_sum

instructions_cases = [
    pytest.param('turn on 0,0 through 1,1', 'on', 0, 0, 1, 1, id='turn on 0,0 through 1,1'),
    pytest.param('toggle 1,0 through 2,2', 'toggle', 1,0,2,2, id='toggle 1,0 through 2,2'),
    pytest.param('turn off 0,1 through 1,2', 'off', 0,1,1,2, id='turn off 0,1 through 1,2')
]

@pytest.mark.parametrize('instruction,order,x_start,y_start,x_end,y_end', instructions_cases)
def test_decode_instruction(instruction,order,x_start,y_start,x_end,y_end):
    assert decode_instruction(instruction) == (order,x_start,y_start,x_end,y_end)

def test_grid_instructions():
    instructions = [i[0][0] for i in instructions_cases]
    grid = operate_grid(instructions, 3, 3)
    assert grid[0][0] == 1
    assert grid[0][1] == 0
    assert grid[0][2] == 0
    assert grid[1][0] == 0
    assert grid[1][1] == 0
    assert grid[1][2] == 0
    assert grid[2][0] == 1
    assert grid[2][1] == 1
    assert grid[2][2] == 1
    assert ligths_lit_sum(grid) == 4

def test_grid_instructions_v2():
    instructions = [i[0][0] for i in instructions_cases]
    grid = operate_grid(instructions, 3, 3, True)
    assert ligths_lit_sum(grid) == 13