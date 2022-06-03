from dataclasses import asdict
import pytest
from aoc_2015.day_twenty_one import Player
from aoc_2015.day_twenty_two import Effect, MatchV2, Spell, Spells, Wizard

spells_cases = [
    pytest.param(
        [Spells.MagicMisile],
        ["Magic Misile"],
        1,
        {"Boss": {"hp": 96}, "Player": {"mana": 447}},
        id="Simple spell case",
    ),
    pytest.param(
        [Spells.Drain],
        ["Drain"],
        1,
        {"Boss": {"hp": 98}, "Player": {"mana": 427, "hp": 102}},
        id="Double effect spell case",
    ),
    pytest.param(
        [Spells.Drain, Spells.MagicMisile],
        ["Poison", "Magic Misile"],
        4,
        {"Boss": {"hp": 87}, "Player": {"mana": 274, "hp": 98}},
        id="Poison spell lasting effect case",
    ),
]


@pytest.mark.parametrize("spells,spell_cast_order,turns,expected_stats", spells_cases)
def test_cast_spell(spells, spell_cast_order, turns, expected_stats):
    # Arrange
    player = Wizard(spells=spells, spell_cast_order=spell_cast_order)
    boss = Player()
    arena = MatchV2(player, boss)
    # Act
    [arena.run_turn() for _ in range(turns)]
    # Assert
    actual_stats = {"Boss": asdict(boss), "Player": asdict(player)}
    for player, stats in expected_stats.items():
        for stat in stats:
            assert expected_stats[player][stat] == actual_stats[player][stat]


def test_sum_effects():
    # Arrange
    effect_a = Effect(damage=4)
    effect_b = Effect(damage=2, heals=2)
    effect_c = Effect(armor=2)
    effect_d = Effect()
    effect_e = Effect(mana=50)
    # Act and Assert
    assert effect_a + effect_b == Effect(damage=6, heals=2)
    assert effect_b + effect_c == Effect(damage=2, heals=2, armor=2)
    assert effect_a + effect_b + effect_c == Effect(damage=6, heals=2, armor=2)
    effect_d += effect_b
    assert effect_d == effect_d
    assert effect_d + effect_e == Effect(damage=2, heals=2, mana=50)
