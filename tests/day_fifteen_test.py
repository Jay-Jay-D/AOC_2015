from dataclasses import dataclass
from unicodedata import name
import pytest

from aoc_2015.day_fifteen import Cookie, Ingredient

ingredient_list = [
    Ingredient("Butterscotch", -1, -2, 6, 3, 8),
    Ingredient("Cinnamon", 2, 3, -2, -1, 3),
]


def test_cookie_score():
    # Arrange
    cookie = Cookie(ingredient_list)
    # Act and Assert
    assert cookie.get_score(44, 56) == 62842880
    assert cookie.get_score(40, 60, 500) == 57600000
