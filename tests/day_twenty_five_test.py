import pytest

from aoc_2015.day_twenty_five import get_code, get_order

coord_to_order_cases = [
    pytest.param((1, 1), 1),
    pytest.param((4, 1), 7),
    pytest.param((1, 4), 10),
    pytest.param((4, 3), 18),
    pytest.param((3, 4), 19),
    pytest.param((2, 5), 20),
]

order_to_code_cases = [
    pytest.param(1, 20151125),
    pytest.param(7, 24592653),
    pytest.param(10, 30943339),
    pytest.param(18, 21345942),
    pytest.param(19, 7981243),
    pytest.param(20, 15514188),
]


@pytest.mark.parametrize("coord, expected_order", coord_to_order_cases)
def test_get_code_order_from_coord(coord, expected_order):
    # Act
    actual_order = get_order(coord)
    # Assert
    assert expected_order == actual_order


@pytest.mark.parametrize("order, expected_code", order_to_code_cases)
def test_get_code_from_order(order, expected_code):
    # Act
    actual_code = get_code(order)
    # Assert
    assert expected_code == actual_code
