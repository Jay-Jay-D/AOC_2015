import pytest
from aoc_2015.day_five import (three_vowel, letter_in_a_row,
                               forbiden_string, letter_in_a_row_2,
                               repeated_letter)

conditions = [three_vowel, letter_in_a_row,
              forbiden_string, letter_in_a_row_2, repeated_letter]

word_cases = [
    pytest.param('aei', 0, True, id='three vowels case 1'),
    pytest.param('xazegov', 0, True, id='three vowels case 2'),
    pytest.param('aeiouaeiouaeiou', 0, True, id='three vowels case 3'),
    pytest.param('xyz', 0, False, id='three vowels case 4'),
    pytest.param('xx', 1, True, id='letter in a row case 1'),
    pytest.param('abcdde', 1, True, id='letter in a row case 2'),
    pytest.param('aabbccdd', 1, True, id='letter in a row case 3'),
    pytest.param('xyz', 1, False, id='letter in a row case 4'),
    pytest.param('acdasd', 2, True, id='forbiden string case 1'),
    pytest.param('xgz', 2, False, id='forbiden string case 2'),
    pytest.param('xyxy', 3, True, id='letter in a row 2 case 1'),
    pytest.param('aabcdefgaa', 3, True, id='letter in a row 2 case 2'),
    pytest.param('aaa', 3, False, id='letter in a row 2 case 3'),
    pytest.param('xyx', 4, True, id='repeated letter case 1'),
    pytest.param('abcdefeghi', 4, True, id='repeated letter case 2'),
    pytest.param('efe', 4, True, id='repeated letter case 3'),
    pytest.param('qwerty', 4, False, id='repeated letter case 4'),
]


@pytest.mark.parametrize('word,condition,expected', word_cases)
def test_three_vowel_condition(word, condition, expected):
    c = conditions[condition].search(word)
    if expected:
        assert c is not None
    else:
        assert c is None
