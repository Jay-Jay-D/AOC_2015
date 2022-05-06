import pytest
from aoc_2015.day_one import run

def test_first_floor_is_zero():
    # Arrange
    directions = ''
    # Act and test 
    assert run(directions) == 0

def test_go_up():
    # Arrange
    directions = '('
    # Act and test 
    assert run(directions) == 1

def test_go_down():
    # Arrange
    directions = ')'
    # Act and test 
    assert run(directions) == -1

direction_cases = [
    pytest.param('(())', 0, id='case 1'),
    pytest.param('()()', 0, id='case 2'),
    pytest.param('(((', 3,  id='case 3'),
    pytest.param('(()(()(', 3, id='case 4'),
    pytest.param('())', -1, id='case 5'),
    pytest.param('))(', -1, id='case 6'),
    pytest.param(')))', -3, id='case 7'),
    pytest.param(')())())', -3, id='case 8')
]

@pytest.mark.parametrize("directions,expected", direction_cases)
def test_run_directions(directions,expected):
    assert run(directions) == expected


