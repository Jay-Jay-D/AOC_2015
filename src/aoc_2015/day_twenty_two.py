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
    Shield = Spell(name="Shield", mana_cost=113, effect=Effect(armor=7, turns=6))
    Poison = Spell(name="Poison", mana_cost=173, effect=Effect(damage=3, turns=6))
    Recharge = Spell(name="Recharge", mana_cost=229, effect=Effect(mana=101, turns=5))
    All = [MagicMisile, Drain, Shield, Poison, Recharge]


@dataclass
class Wizard(Player):
    mana: int = 500
    cast_counter: int = 0
    spells: list[Spell] = field(default_factory=list)
    spell_cast_order: list[str] = field(default_factory=list)
    active_spells: dict[str, int] = field(default_factory=dict)
    _spells_by_name: dict[str, Spell] = field(default_factory=dict)
    _base_armor: int = 0

    def __post_init__(self):
        for s in self.spells:
            self._spells_by_name[s.name] = s

    def wizard_turn(self, is_attacking):
        effects = self.get_active_spells()
        if is_attacking:
            effects += self.cast_spell()
        self.hp += effects.heals
        self.mana += effects.mana
        self.armor = effects.armor if "Shield" in self.active_spells else self._base_armor
        self.update_active_spells()
        return effects

    def update_active_spells(self):
        # Finally, clean affects after turns count passed.
        for spell_name in list(self.active_spells.keys()):
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
        effects = self.players[0].wizard_turn(isinstance(attacker, Wizard))

        self.players[1].hp -= effects.damage
        # If it's Boss turn, then make him attack.
        if not isinstance(attacker, Wizard) and self.players[1].hp > 0:
            return super().attack(attacker, defender)


if __name__ == "__main__":
    spell_cast_order = ["Poison", "Magic Misile"]
    player_stats = {
        "hp": 10,
        "mana": 250,
        "spells": Spells.All,
        "spell_cast_order": spell_cast_order,
    }
    boss_stats = {"hp": 13, "damage": 8}
    player = Wizard(**player_stats)
    boss = Player(**boss_stats)
    arena = MatchV2(player, boss)
    # Act
    arena.run_match()
