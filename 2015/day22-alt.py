from dataclasses import dataclass, field, replace
from typing import Dict

import advent

STARTING_HP = 50
STARTING_MANA = 500


@dataclass
class Effects:
    start: dict = field(default_factory=dict)
    end: dict = field(default_factory=dict)
    perturn: dict = field(default_factory=dict)
    duration: int = 0

    def copy(self):
        return replace(self)


@dataclass
class Fighter:
    name: str
    hp: int
    dmg: int
    mana: int = 0
    spells: dict = field(default_factory=dict)
    # cooldowns: Counter = field(default_factory=Counter)
    armor: int = 0
    status: Dict[str, Effects] = field(default_factory=dict)

    def __repr__(self) -> str:
        s1 = f'Fighter({self.name}): HP={self.hp}, MANA={self.mana}, ARMOR={self.armor}'
        l = []
        for itm, val in self.status.items():
            l.append(f'{itm}: {val.duration}')
        if l:
            s1 = s1 + ', ' + ', '.join(l)
        return s1

    def attack(self, other, debug):
        other.hp -= (self.dmg - other.armor)
        if debug:
            print(
                f'{self.name} attacks {other.name} for {self.dmg-other.armor} damage')

    def available_spells(self, other):
        for k, v in self.spells.items():
            if k in self.status or k in other.status:
                continue
            if v.cost > self.mana:
                continue
            yield k

    def cast(self, other, spell: str):
        self.spells[spell].cast(self, other)


@dataclass
class Spell:
    name: str
    cost: int
    tgt_effects: Effects = field(default_factory=Effects)
    self_effects: Effects = field(default_factory=Effects)

    def cast(self, source: Fighter, tgt: Fighter):
        source.mana -= self.cost
        self.cast_setter(source, True)
        self.cast_setter(tgt, False)

    def cast_setter(self, char: Fighter, to_self: bool):
        d_effects = self.self_effects if to_self else self.tgt_effects
        for attr, mod in d_effects.start.items():
            cur_val = getattr(char, attr)
            setattr(char, attr, cur_val+mod)
        if d_effects.duration:
            char.status[self.name] = d_effects.copy()

    def copy(self):
        return replace(self)


SHIELD = Spell('Shield', 113, self_effects=Effects(
    start={'armor': 7}, end={'armor': -7}, duration=7))
MAG_MISSILE = Spell('Magic Missile', 53, tgt_effects=Effects(start={'hp': -4}))
DRAIN = Spell('Drain', 73, tgt_effects=Effects(
    start={'hp': -2}), self_effects=Effects(start={'hp': 2}))
POISON = Spell('Poison', 173, tgt_effects=Effects(
    perturn={'hp': -3}, duration=6))
RECHARGE = Spell('Recharge', 229, self_effects=Effects(
    perturn={'mana': 101}, duration=5))

SPELLS = (MAG_MISSILE, DRAIN, SHIELD, POISON, RECHARGE)


def game_loop(player: Fighter, boss: Fighter, debug, verbose):
    turn = True
    while player.hp > 0 and boss.hp > 0:
        # TODO upkeep stuff
        if debug:
            print(f"-- {'Player' if turn else 'Boss'} turn --")
            print(
                f"- Player has {player.hp} hit points, {player.armor} armor, {player.mana} mana")
            print(f"- Boss has {boss.hp} hit points")
            pass  # TODO
        upkeep(player, debug)
        upkeep(boss, debug)

        if turn:
            d = dict(enumerate(player.available_spells(boss)))
            if not d:
                print(f'No spells available! Boss wins!')
                return boss
            if verbose:
                print()
                print(player)
                print(boss)
                print()
            prompt = '\n'.join(
                f'{i}: {name} (Cost:{player.spells[name].cost}) ({player.mana} -> {player.mana-player.spells[name].cost})' for i, name in d.items())
            prompt += '\nEnter your choice:'
            while (choice := int(input(prompt))) not in d:
                print('Invalid choice, pick again')
            player.cast(boss, d[choice])
        else:
            boss.attack(player, debug)
        turn = not turn
    return player if player.hp > 0 else boss


def upkeep(player: Fighter, debug):
    for n, eff in player.status.copy().items():
        for attr, mod in eff.perturn.items():
            cur_val = getattr(player, attr)
            setattr(player, attr, cur_val+mod)
            if debug:
                print(
                    f'{n} changes {player.name}\'s {attr} by {mod}, new value is {getattr(player,attr)}')
        player.status[n].duration -= 1
        if debug:
            print(f'Timer for {n} down to {player.status[n].duration}')
        if player.status[n].duration == 0:
            for attr, mod in eff.end.items():
                cur_val = getattr(player, attr)
                setattr(player, attr, cur_val+mod)
            if debug:
                print(f'{n} ends on {player.name}')
            del player.status[n]


def main(debug=False, verbose=False):
    hp_str, dmg_str = advent.get_input(2015, 22).splitlines()
    boss_hp = int(hp_str.split()[-1])
    boss_dmg = int(dmg_str.split()[-1])
    boss = Fighter('boss', boss_hp, boss_dmg)
    player = Fighter('player', STARTING_HP, 0, STARTING_MANA)
    for spell in SPELLS:
        c = spell.copy()
        player.spells[c.name] = c
    winner = game_loop(player, boss, debug, verbose)
    print(winner.name)


if __name__ == '__main__':
    main(verbose=True)
