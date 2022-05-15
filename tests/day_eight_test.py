import pytest

from aoc_2015.day_eight import (
    count_code_representation,
    count_new_encode_diff,
    count_string_characters,
)

cases = [
    pytest.param(r'""', 2, 0, 4),
    pytest.param(r'"abc"', 5, 3, 4),
    pytest.param(r'"aaa\"aaa"', 10, 7, 6),
    pytest.param(r'"\x27"', 6, 1, 5),
]


@pytest.mark.parametrize(
    "str_lit,expected_code_len,expected_string_len,expected_new_encode_diff", cases
)
def test_string_cases(str_lit, expected_code_len, expected_string_len, expected_new_encode_diff):
    assert count_code_representation(str_lit) == expected_code_len
    assert count_string_characters(str_lit) == expected_string_len
    assert count_new_encode_diff(str_lit) == expected_new_encode_diff
