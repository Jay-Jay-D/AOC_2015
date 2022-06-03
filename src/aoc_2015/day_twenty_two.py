from dataclasses import dataclass, field
from aoc_2015.day_twenty_one import Match, Player


@dataclass
class Effect:
    turns: int = 1
    armor: int = 0
    heals: int = 0
    damage: int = 0
    mana: int = 0


@dataclass
class Spell:
    name: str
    mana_cost: int
    effect: Effect


@dataclass
class Wizard(Player):
    spells: list[Spell] = field(default_factory=list)
    mana: int = 500

    def cast_spell(self):
        spell = self.spells[0]
        self.mana -= spell.mana_cost
        return spell


class MatchV2(Match):
    def attack(self, attacker, defender):
        # Player's turn
        if isinstance(attacker, Wizard):
            spell = attacker.cast_spell()
            defender.hp -= max((spell.effect.damage - defender.armor), 1)
            return
        return super().attack(attacker, defender)


if __name__ == "__main__":
    spells = [Spell(name="Magic Misile", mana_cost=53, effect=Effect(damage=4))]
    player = Wizard(spells=spells)
    boss = Player()
    arena = MatchV2(player, boss)
    # Act
    arena.run_turn()
