import pytest
from aoc_2015.day_four import find_value_for_key

cases = [
    pytest.param('abcdef', 609043, id='case 1'),
    pytest.param('pqrstuv', 1048970, id='case 2')
]


@pytest.mark.parametrize('secret_key,expected', cases)
def test_value_for_key(secret_key, expected):
    assert find_value_for_key(secret_key) == expected
