from aoc_2015.day_twenty_one import Item, Match, Player


def test_default_player():
    # Act
    player = Player()
    # Assert
    assert player.damage == 0
    assert player.armor == 0
    assert player.hp == 100


def test_run_turns():
    # Arrange
    player = Player(hp=10, damage=8, armor=10)
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


def test_run_match():
    # Arrange
    player = Player(hp=8, damage=5, armor=5)
    boss = Player(hp=12, damage=7, armor=2)
    arena = Match(player, boss)
    # check arena winner is not set
    arena.winner = None
    # Act
    arena.run_match()
    # Assert
    arena.winner = "Player"
    arena.turns = 7


def test_use_item():
    # Arrange
    player = Player(hp=8, damage=5, armor=5)
    items = [
        Item(name="dagger", cost=8, damage=4),
        Item(name="leather", cost=13, armor=1),
        Item(name="defense3", cost=80, armor=3),
        None,
    ]
    # Act
    player.use(items)
    # Assert
    assert player.items == items[:3]
    assert player.gold_spent == 101
    assert player.damage == 9
    assert player.armor == 9
