from dataclasses import dataclass, field
from aoc_2015.day_twenty_one import Match, Player


@dataclass
class Effect:
    turns: int = 1
    armor: int = 0
    heals: int = 0
    damage: int = 0
    mana: int = 0

    def __add__(self, other):
        return Effect(
            armor=self.armor + other.armor,
            heals=self.heals + other.heals,
            damage=self.damage + other.damage,
            mana=self.mana + other.mana,
        )


@dataclass
class Spell:
    name: str
    mana_cost: int
    effect: Effect


class Spells:
    MagicMisile = Spell(name="Magic Misile", mana_cost=53, effect=Effect(damage=4))
    Drain = Spell(name="Drain", mana_cost=73, effect=Effect(damage=2, heals=2))
    Poison = Spell(name="Poison", mana_cost=173, effect=Effect(damage=3, turns=6))


@dataclass
class Wizard(Player):
    mana: int = 500
    spells: list[Spell] = field(default_factory=list)
    spell_cast_order: list[str] = field(default_factory=list)
    cast_counter = 0
    active_spells: dict[str, int] = field(default_factory=dict)
    _spells_by_name: dict[str, Spell] = field(default_factory=dict)

    def __post_init__(self):
        for s in self.spells:
            self._spells_by_name[s.name] = s

    def update_active_spells(self):
        # Finally, clean affects after turns count passed.
        for spell_name in self.active_spells:
            if self.active_spells[spell_name] == self._spells_by_name[spell_name].effect.turns:
                del self.active_spells[spell_name]

        # Update turn count in active spells
        for spell_name in self.active_spells:
            self.active_spells[spell_name] += 1

    def get_active_spells(self):
        active_spells_effect = Effect()
        for spell_name, effect_turns in self.active_spells.items():
            if effect_turns == 0:
                # if effect_turns is zero, do nothing.
                # The effect will activate in the next turn.
                continue
            active_spells_effect += self._spells_by_name[spell_name].effect
        return active_spells_effect

    def cast_spell(self):
        cast_spell_effect = Effect()
        casted_spell = self._spells_by_name[self.spell_cast_order[self.cast_counter]]
        self.cast_counter += 1
        self.mana -= casted_spell.mana_cost

        if casted_spell.effect.turns > 1:
            self.active_spells[casted_spell.name] = 0
        else:
            cast_spell_effect += casted_spell.effect

        return cast_spell_effect


class MatchV2(Match):
    def attack(self, attacker, defender):
        # Player zero is always Little Henry Case, the Wizard
        effects = self.players[0].get_active_spells()
        # Player's turn
        if isinstance(attacker, Wizard):
            effects += attacker.cast_spell()
            attacker.hp += effects.heals
            attacker.mana += effects.mana
            attacker.armor += effects.armor

        defender.hp -= effects.damage

        self.players[0].update_active_spells()

        # If it's Boss turn, then make it attack
        if not isinstance(attacker, Wizard):
            return super().attack(attacker, defender)


if __name__ == "__main__":
    spells = [Spell(name="Magic Misile", mana_cost=53, effect=Effect(damage=4))]
    player = Wizard(
        spells=[Spells.Poison, Spells.MagicMisile], spell_cast_order=["Poison", "Magic Misile"]
    )
    boss = Player()
    arena = MatchV2(player, boss)
    # Act
    for _ in range(4):
        arena.run_turn()
