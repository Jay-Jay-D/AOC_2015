from dataclasses import asdict
import pytest
from aoc_2015.day_twenty_one import Player
from aoc_2015.day_twenty_two import Effect, MatchV2, Spell, Spells, Wizard

spells_test_cases = [
    pytest.param(
        [Spells.MagicMisile],
        ["Magic Misile"],
        1,
        None,
        {"Boss": {"hp": 96}, "Player": {"mana": 447}},
        id="Simple spell case",
    ),
    pytest.param(
        [Spells.Drain],
        ["Drain"],
        1,
        None,
        {"Boss": {"hp": 98}, "Player": {"mana": 427, "hp": 102}},
        id="Double effect spell case",
    ),
    pytest.param(
        [Spells.Poison, Spells.MagicMisile],
        ["Poison", "Magic Misile"],
        4,
        None,
        {"Boss": {"hp": 87}, "Player": {"mana": 274, "hp": 98}},
        id="Poison spell lasting effect case",
    ),
    pytest.param(
        [Spell(name="Poison", mana_cost=10, effect=Effect(damage=5, turns=2)), Spells.MagicMisile],
        ["Poison", "Magic Misile"],
        4,
        None,
        {"Boss": {"hp": 86}, "Player": {"mana": 437, "hp": 98}},
        id="Poison spell lasting effect case until it ends.",
    ),
    pytest.param(
        [
            Spell(name="Shield", mana_cost=100, effect=Effect(armor=5, turns=2)),
            Spell(name="Magic Misile", mana_cost=50, effect=Effect(damage=5)),
        ],
        ["Shield", "Magic Misile"],
        4,
        {"damage": 10},
        {"Boss": {"hp": 95}, "Player": {"mana": 350, "armor": 0, "hp": 85}},
        id="Shield spell case, lasting effect armor stats.",
    ),
    pytest.param(
        [
            Spell(name="Recharge", mana_cost=10, effect=Effect(mana=50, turns=2)),
            Spell(name="Magic Misile", mana_cost=50, effect=Effect(damage=5)),
        ],
        ["Recharge", "Magic Misile"],
        4,
        {"damage": 10},
        {"Boss": {"hp": 95}, "Player": {"mana": 540, "hp": 80}},
        id="Shield spell case, lasting effect armor stats.",
    ),
]


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


@pytest.mark.parametrize(
    "spells,spell_cast_order,turns,boss_stats,expected_stats", spells_test_cases
)
def test_cast_spell(spells, spell_cast_order, turns, boss_stats, expected_stats):
    # Arrange
    player = Wizard(spells=spells, spell_cast_order=spell_cast_order)
    boss = Player()
    if boss_stats is not None:
        boss = Player(**boss_stats)
    arena = MatchV2(player, boss)
    # Act
    [arena.run_turn() for _ in range(turns)]
    # Assert
    actual_stats = {"Boss": asdict(boss), "Player": asdict(player)}
    for player, stats in expected_stats.items():
        for stat in stats:
            assert expected_stats[player][stat] == actual_stats[player][stat]


battles_cases = [
    pytest.param(
        {
            "hp": 10,
            "mana": 250,
            "spells": Spells.All,
            "spell_cast_order": ["Poison", "Magic Misile"],
        },
        {"hp": 13, "damage": 8},
        "Player",
        4,
        {"Boss": {"hp": 0}, "Player": {"mana": 24, "hp": 2}},
        id="Battle 1",
    ),
    pytest.param(
        {
            "hp": 10,
            "mana": 250,
            "spells": Spells.All,
            "spell_cast_order": ["Recharge", "Shield", "Drain", "Poison", "Magic Misile"],
        },
        {"hp": 14, "damage": 8},
        "Player",
        10,
        {"Boss": {"hp": -1}, "Player": {"mana": 114, "hp": 1}},
        id="Battle 2",
    ),
    pytest.param(
        {
            "hp": 10,
            "mana": 50,
            "spells": Spells.All,
            "spell_cast_order": ["Magic Misile"],
        },
        {"hp": 10},
        "Boss",
        1,
        {"Boss": {"hp": 10}, "Player": {"mana": 50, "hp": 0}},
        id="Battle 3 - Player runs out of mana.",
    ),
]


@pytest.mark.parametrize("player_stats,boss_stats,winner,turns,expected_stats", battles_cases)
def test_run_match(player_stats, boss_stats, winner, turns, expected_stats):
    # Arrange
    player = Wizard(**player_stats)
    boss = Player(**boss_stats)
    arena = MatchV2(player, boss)
    # Act
    arena.run_match()
    # Assert
    assert arena.turns == turns
    assert arena.winner == winner

    actual_stats = {"Boss": asdict(boss), "Player": asdict(player)}
    for player, stats in expected_stats.items():
        for stat in stats:
            assert expected_stats[player][stat] == actual_stats[player][stat]
