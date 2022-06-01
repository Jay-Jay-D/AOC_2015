import pytest

from aoc_2015.day_twenty import get_gifts_to_house, get_house_with_gifts


def test_get_gifts_to_house():
    assert get_gifts_to_house(30) == (30, 720)
    assert get_gifts_to_house([1, 2, 3, 4]) == [(1, 10), (2, 30), (3, 40), (4, 70)]
    assert get_gifts_to_house([49, 50, 51, 52, 99, 100, 101, 102, 103], True) == [
        (49, 627),
        (50, 1023),
        (51, 781),
        (52, 1067),
        (99, 1705),
        (100, 2376),
        (101, 1111),
        (102, 2343),
        (103, 1133),
    ]


def test_get_house_with_gifts():
    get_house_with_gifts(720) == 30
    get_house_with_gifts(3012, True) == 96
