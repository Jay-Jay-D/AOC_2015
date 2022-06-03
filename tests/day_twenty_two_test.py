from aoc_2015.day_twenty_one import Player
from aoc_2015.day_twenty_two import Effect, MatchV2, Spell, Wizard


def test_cast_spell():
    # Arrange
    spells = [Spell(name="Magic Misile", mana_cost=53, effect=Effect(damage=4))]
    player = Wizard(spells=spells)
    boss = Player()
    arena = MatchV2(player, boss)
    # Act
    arena.run_turn()
    # Assert
    assert player.mana == 447
    assert boss.hp == 96


def test_cast_healing_spell():
    pass
