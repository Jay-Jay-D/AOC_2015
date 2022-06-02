from aoc_2015.day_twenty_one import Match, Player


def test_player_attack_boos():
    # Arrange
    player = Player(hp=10, damage=8, armor=100)
    boss = Player(hp=10, damage=8, armor=3)
    arena = Match(player, boss)
    # Act
    arena.run_turn()
    # Assert
    assert boss.hp == 5
    # Act
    arena.run_turn()
    # Assert
    assert player.hp == 9
