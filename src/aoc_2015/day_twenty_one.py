from dataclasses import dataclass


@dataclass
class Player:
    hp: int
    damage: int
    armor: int


class Match:
    def __init__(self, *players):
        self.players = players
        self._player_turn = True

    def run_turn(self):
        attacker = self.players[int(not self._player_turn)]
        defender = self.players[int(self._player_turn)]
        defender.hp -= max((attacker.damage - defender.armor), 1)
        self._player_turn = not self._player_turn


if __name__ == "__main__":
    player = Player(hp=10, damage=8, armor=100)
    boss = Player(hp=10, damage=8, armor=3)
    arena = Match([player, boss])
