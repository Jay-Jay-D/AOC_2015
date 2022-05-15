import pytest

from aoc_2015.day_ten import say, say_many_times

cases = [
    pytest.param("1", "11"),
    pytest.param("11", "21"),
    pytest.param("21", "1211"),
    pytest.param("1211", "111221"),
    pytest.param("111221", "312211"),
]


@pytest.mark.parametrize("sequence,expected_reading", cases)
def test_look_and_say(sequence, expected_reading):
    assert say(sequence) == expected_reading


def test_look_and_say_many_times():
    assert say_many_times("1", 5) == "312211"
