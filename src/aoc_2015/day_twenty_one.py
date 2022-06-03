from itertools import combinations, product
from math import inf
from dataclasses import dataclass


@dataclass
class Item:
    name: str
    cost: int = 0
    damage: int = 0
    armor: int = 0


@dataclass
class Player:
    hp: int = 100
    damage: int = 0
    armor: int = 0

    def __post_init__(self):
        self.items = []
        self.gold_spent = 0

    def use(self, items):
        self.items = [i for i in items if i is not None]
        self.gold_spent = sum(i.cost for i in self.items)
        self.damage += sum(i.damage for i in self.items)
        self.armor += sum(i.armor for i in self.items)


class Match:
    def __init__(self, *players):
        self.players = players
        self.winner = None
        self.turns = 0
        self._player_turn = True

    def run_turn(self):
        attacker = self.players[int(not self._player_turn)]
        defender = self.players[int(self._player_turn)]
        self.attack(attacker, defender)
        self._player_turn = not self._player_turn

    def attack(self, attacker, defender):
        defender.hp -= max((attacker.damage - defender.armor), 1)

    def run_match(self):
        while all(p.hp > 0 for p in self.players):
            self.run_turn()
            self.turns += 1
        self.winner = "Boss" if self._player_turn else "Player"


class Store:
    weapons = [
        Item(name="dagger", cost=8, damage=4, armor=0),
        Item(name="shortsword", cost=10, damage=5, armor=0),
        Item(name="warhammer", cost=25, damage=6, armor=0),
        Item(name="longsword", cost=40, damage=7, armor=0),
        Item(name="greataxe", cost=74, damage=8, armor=0),
    ]
    armors = [
        Item(name="leather", cost=13, damage=0, armor=1),
        Item(name="chainmail", cost=31, damage=0, armor=2),
        Item(name="splintmail", cost=53, damage=0, armor=3),
        Item(name="bandedmail", cost=75, damage=0, armor=4),
        Item(name="platemail", cost=102, damage=0, armor=5),
    ]
    rings = [
        Item(name="damage1", cost=25, damage=1, armor=0),
        Item(name="damage2", cost=50, damage=2, armor=0),
        Item(name="damage3", cost=100, damage=3, armor=0),
        Item(name="defense1", cost=20, damage=0, armor=1),
        Item(name="defense2", cost=40, damage=0, armor=2),
        Item(name="defense3", cost=80, damage=0, armor=3),
    ]


def generate_all_combinations():
    all_combinations = []
    weapons = Store.weapons
    armors = [*Store.armors, None]
    rings = [*Store.rings, None]
    rings.extend(iter(combinations(Store.rings, 2)))
    for weapon, armor in product(weapons, armors):
        for ring in rings:
            items = [weapon, armor]
            if isinstance(ring, tuple):
                items.extend(iter(ring))
            else:
                items.append(ring)
            all_combinations.append(items)
    return all_combinations


if __name__ == "__main__":
    min_cost = inf
    max_cost = -inf
    for match_count, items in enumerate(generate_all_combinations(), start=1):
        player = Player()
        player.use(items)
        boss = Player(hp=104, damage=8, armor=1)
        arena = Match(player, boss)
        arena.run_match()

        print(
            f"Match {match_count} => {arena.winner} win after {arena.turns} turns: gold spent {player.gold_spent}."
        )
        if arena.winner == "Player":
            min_cost = min(player.gold_spent, min_cost)
        else:
            max_cost = max(player.gold_spent, max_cost)

    print(f"Part one: the least amount of gold you can spend and still win is {min_cost}")
    print(f"Part two: the most amount of gold you can spend and still lose is {max_cost}")
