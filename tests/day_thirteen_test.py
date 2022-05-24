import pytest

from aoc_2015.day_thirteen import generate_matrix, get_optimal_seating_arrangement, parse_line

potential_happiness = [
    "Alice would gain 54 happiness units by sitting next to Bob.",
    "Alice would lose 79 happiness units by sitting next to Carol.",
    "Alice would lose 2 happiness units by sitting next to David.",
    "Bob would gain 83 happiness units by sitting next to Alice.",
    "Bob would lose 7 happiness units by sitting next to Carol.",
    "Bob would lose 63 happiness units by sitting next to David.",
    "Carol would lose 62 happiness units by sitting next to Alice.",
    "Carol would gain 60 happiness units by sitting next to Bob.",
    "Carol would gain 55 happiness units by sitting next to David.",
    "David would gain 46 happiness units by sitting next to Alice.",
    "David would lose 7 happiness units by sitting next to Bob.",
    "David would gain 41 happiness units by sitting next to Carol.",
]


cases = [
    pytest.param("Alice would gain 54 happiness units by sitting next to Bob.", "Alice", "Bob", 54),
    pytest.param("David would lose 7 happiness units by sitting next to Bob.", "David", "Bob", -7),
]


@pytest.mark.parametrize("line,expected_person_a,expected_person_b,expected_happiness", cases)
def test_parse_line(line, expected_person_a, expected_person_b, expected_happiness):
    actual_person_a, actual_person_b, actual_happiness = parse_line(line)
    assert actual_person_a == expected_person_a
    assert actual_person_b == expected_person_b
    assert actual_happiness == expected_happiness


def test_generate_matrix():
    # Arrange
    # fmt: off
    expected_happiness_matrix = [
    [  0, 54, -79,  -2], 
    [ 83,  0,  -7, -63],
    [-62, 60,   0,  55],
    [ 46, -7,  41,   0]
    ]
    # fmt: on
    # Act
    actual_happiness_matrix, _ = generate_matrix(potential_happiness)
    # Assert
    assert actual_happiness_matrix == expected_happiness_matrix


def test_get_optimal_seating_arrangement():
    # Arrange
    expected_seating_arrangement = ["Alice", "Bob", "Carol", "David"]
    # Act
    max_happiness_arrange, max_happiness = get_optimal_seating_arrangement(potential_happiness)
    # Assert
    assert max_happiness_arrange == expected_seating_arrangement
    assert max_happiness == 330
