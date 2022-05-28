from dataclasses import asdict

from aoc_2015.day_sixteen import aunts


aunt_sues = [
    "Sue 1: goldfish: 9, cars: 0, samoyeds: 9",
    "Sue 2: perfumes: 5, trees: 8, goldfish: 8",
    "Sue 3: pomeranians: 2, akitas: 1, trees: 5",
    "Sue 4: goldfish: 10, akitas: 2, perfumes: 9",
    "Sue 5: cats: 7, trees: 3, children: 3",
    "Sue 241: cars: 2, pomeranians: 1, samoyeds: 2",
]

looking_for = {
    "Sue": 0,
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def test_parse_aunt_sue():
    # Arrange
    aunt_sue_data = "Sue 1: goldfish: 9, cars: 0, samoyeds: 9"
    # Act
    aunt_sue = aunts.parse(aunt_sue_data)
    # Assert
    assert asdict(aunt_sue) == {
        "Sue": 1,
        "children": None,
        "cats": None,
        "samoyeds": 9,
        "pomeranians": None,
        "akitas": None,
        "vizslas": None,
        "goldfish": 9,
        "trees": None,
        "cars": 0,
        "perfumes": None,
    }


def test_match_aunt():
    # Arrange
    aunts_sue = aunts.parse_aunts(aunt_sues)
    aunt_looking_for = aunts(**looking_for)

    # Act and assert
    assert not aunts_sue[0].matches(aunt_looking_for)
    assert not aunts_sue[1].matches(aunt_looking_for)
    assert not aunts_sue[2].matches(aunt_looking_for)
    assert not aunts_sue[3].matches(aunt_looking_for)
    assert aunts_sue[4].matches(aunt_looking_for)
    assert not aunts_sue[4].matches(aunt_looking_for, True)
    assert not aunts_sue[5].matches(aunt_looking_for)
    assert aunts_sue[5].matches(aunt_looking_for, True)
