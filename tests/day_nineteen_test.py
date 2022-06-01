import pytest

from aoc_2015.day_nineteen import count_distinct_molecules


replacements = [
    "H => HO",
    "H => OH",
    "O => HH",
]

base_molecule_cases = [
    pytest.param("HOH", 4),
    pytest.param("HOHOHO", 7),
]


@pytest.mark.parametrize("base_molecule, expected", base_molecule_cases)
def test_count_distinct_molecules(base_molecule, expected):
    assert count_distinct_molecules(base_molecule, replacements) == expected
