import pytest

from aoc_2015.day_eleven import get_next_password, incremment_string

adder_cases = [
    pytest.param("a", "b"),
    pytest.param("m", "n"),
    pytest.param("z", "a"),
    pytest.param("aa", "ab"),
    pytest.param("hj", "hk"),
    pytest.param("cz", "da"),
    pytest.param("czzz", "daaa"),
    pytest.param("cxzz", "cyaa"),
    pytest.param("zzzz", "aaaa"),
    pytest.param("zzhz", "zzja"),
]

passwords_cases = [pytest.param("abcdefgh", "abcdffaa"), pytest.param("ghijklmn", "ghjaabcc")]


@pytest.mark.parametrize("input,expected", adder_cases)
def test_increment_string(input, expected):
    assert incremment_string(input) == expected


@pytest.mark.parametrize("password,expected", passwords_cases)
def test_increment_password(password, expected):
    assert get_next_password(password) == expected
