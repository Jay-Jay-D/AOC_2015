from dataclasses import dataclass, field
from math import inf
from random import shuffle
from tkinter import S
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
    All = [Recharge, Poison, Shield, MagicMisile, Drain]
    ByName = {s.name: s for s in All}


@dataclass
class Wizard(Player):
    mana: int = 500
    cast_counter: int = 0
    mana_usage = 0
    spells: list[Spell] = field(default_factory=list)
    spell_cast_order: list[str] = field(default_factory=list)
    active_spells: dict[str, int] = field(default_factory=dict)
    _base_armor: int = 0
    _spells_by_name: dict[str, Spell] = field(default_factory=dict)

    def __post_init__(self):
        for s in self.spells:
            self._spells_by_name[s.name] = s

    def wizard_turn(self, is_attacking):
        # effects = self.get_active_spells()
        effects = Effect()
        if is_attacking:
            casted_spell_effect = self.cast_spell()
            if casted_spell_effect is None:
                return effects
            effects += casted_spell_effect
        effects += self.get_active_spells()
        self.hp += effects.heals
        self.mana += effects.mana
        self.armor = effects.armor if "Shield" in self.active_spells else self._base_armor
        self.update_active_spells()
        return effects

    def update_active_spells(self):
        # Finally, clean affects after turns count passed.
        for spell_name in list(self.active_spells.keys()):
            if self.active_spells[spell_name] == 0:
                del self.active_spells[spell_name]

        # Update turn count in active spells
        for spell_name in self.active_spells:
            self.active_spells[spell_name] -= 1

    def get_active_spells(self):
        active_spells_effect = Effect()
        for spell_name, effect_turns in self.active_spells.items():
            if effect_turns == self._spells_by_name[spell_name].effect.turns:
                # if effect_turns is zero, do nothing.
                # The effect will activate in the next turn.
                continue
            active_spells_effect += self._spells_by_name[spell_name].effect
        return active_spells_effect

    def cast_spell(self):
        cast_spell_effect = Effect()

        casted_spell = self._spells_by_name[self.spell_cast_order[self.cast_counter]]

        if self.mana < casted_spell.mana_cost or (
            casted_spell.name in self.active_spells and self.active_spells[casted_spell.name] > 0
        ):
            self.hp = 0
            return None

        self.cast_counter += 1
        self.mana -= casted_spell.mana_cost
        self.mana_usage += casted_spell.mana_cost

        is_spell_last_turn = (
            casted_spell.name in self.active_spells and self.active_spells[casted_spell.name] == 0
        )

        if casted_spell.effect.turns > 1:
            self.active_spells[casted_spell.name] = casted_spell.effect.turns
        else:
            cast_spell_effect += casted_spell.effect

        if is_spell_last_turn:
            cast_spell_effect += casted_spell.effect

        return cast_spell_effect


class MatchV2(Match):
    def attack(self, attacker, defender):
        effects = self.players[0].wizard_turn(isinstance(attacker, Wizard))

        self.players[1].hp -= effects.damage
        # If it's Boss turn, then make him attack.
        if not isinstance(attacker, Wizard) and self.players[1].hp > 0:
            return super().attack(attacker, defender)


def run_battle(spell_cast_order, hard_mode=False):
    player_stats = {
        "hp": 50,
        "mana": 500,
        "spells": Spells.All,
        "spell_cast_order": spell_cast_order,
    }
    boss_stats = {"hp": 71, "damage": 10}
    player = Wizard(**player_stats)
    boss = Player(**boss_stats)
    arena = MatchV2(player, boss, hard_mode=hard_mode)
    return arena.run_match(len(spell_cast_order) * 2)


if __name__ == "__main__":
    results = []
    battle_count = 0
    min_cost = inf

    spells = Spells.All.copy()
    shuffle(spells)

    for spell in spells:
        queue = [[spell.name]]
        while queue:
            path = queue.pop(0)
            node = path[-1]

            for next_spell in spells:
                new_path = list(path)
                new_path.append(next_spell.name)
                #
                path_cost = sum(Spells.ByName[s].mana_cost for s in new_path)
                if path_cost > min_cost:
                    continue

                battle = run_battle(new_path, hard_mode=True)
                battle_count += 1

                if battle is None:
                    queue.append(new_path)
                    # print(f"Battle {battle_count}  not finished")
                elif battle == "Boss":
                    # print(f"Battle {battle_count}  Boos wins!")
                    continue
                else:
                    print(
                        f"Battle {battle_count}, Mana spent {path_cost} | Spell Orde:",
                        " -> ".join(new_path),
                    )
                    results.append((path_cost, new_path))
                    if path_cost < min_cost:
                        min_cost = path_cost
