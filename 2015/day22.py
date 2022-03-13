import re
from collections import defaultdict, namedtuple
from copy import deepcopy
from dataclasses import dataclass, field
from sys import maxsize

import advent

Spell = namedtuple('Spell', ['cost', 'dmg', 'hp', 'turns', 'armor'])

SPELLS = {
    'Magic Missile': Spell(53, 4, 0, 0, 0),
    'Drain': Spell(73, 2, 2, 0, 0),
    'Shield': Spell(113, 0, 0, 6, 7),
    'Poison': Spell(173, 0, 0, 6, 0),
    'Recharge': Spell(229, 0, 0, 5, 0)
}


@dataclass
class Game:
    boss_hp: int
    player_hp: int = 50
    player_mana: int = 500
    player_armor: int = 0
    timers: defaultdict[str, int] = field(
        default_factory=lambda: defaultdict(int))
    player_turn: bool = True
    mana_used: int = 0
    history: list = field(default_factory=list)


class Solution:
    def __init__(self, data: str) -> None:
        self.boss_hp, self.boss_dmg = map(int, re.findall(r'\d+', data))
        self.best_mana = {1: maxsize, 2: maxsize}
        self.best_path = {1: None, 2: None}

    def simulate(self, game: Game, part: int):
        if game.mana_used >= self.best_mana[part]:
            return

        if part == 2 and game.player_turn:
            game.player_hp -= 1
            if game.player_hp <= 0:
                return

        for spell_name, turns_left in game.timers.items():
            if turns_left == 0:
                continue
            if spell_name == 'Poison':
                game.boss_hp -= 3
                if game.boss_hp <= 0:
                    if game.mana_used < self.best_mana[part]:
                        self.best_mana[part] = game.mana_used
                        self.best_path[part] = game.history.copy()
                    return
            elif spell_name == 'Recharge':
                game.player_mana += 101
            elif spell_name == 'Shield' and turns_left == 1:
                game.player_armor = 0
            game.timers[spell_name] -= 1

        if game.player_turn:
            for spell_name, spell in SPELLS.items():
                if spell.cost > game.player_mana:
                    continue
                if game.timers[spell_name] > 0:
                    continue

                new_game = deepcopy(game)
                new_game.history.append(spell_name)

                new_game.player_mana -= spell.cost
                new_game.mana_used += spell.cost
                if new_game.mana_used >= self.best_mana[part]:
                    continue

                new_game.boss_hp -= spell.dmg
                if new_game.boss_hp <= 0:
                    if new_game.mana_used < self.best_mana[part]:
                        self.best_mana[part] = new_game.mana_used
                    return

                new_game.player_armor += spell.armor
                new_game.player_hp += spell.hp
                new_game.player_turn = False
                new_game.timers[spell_name] = spell.turns
                self.simulate(new_game, part)
        else:
            damage = max(0, self.boss_dmg - game.player_armor)
            game.player_hp -= damage
            if game.player_hp > 0:
                game.player_turn = True
                self.simulate(game, part)

    def part_one(self, print_path=False):
        self.simulate(Game(self.boss_hp), part=1)
        print(self.best_mana[1])
        if print_path:
            print(f'Path: {self.best_path[1]}')

    def part_two(self, print_path=False):
        self.simulate(Game(self.boss_hp), part=2)
        print(self.best_mana[2])
        if print_path:
            print(f'Path: {self.best_path[2]}')


def main():
    data = advent.get_input(2015, 22)
    s = Solution(data)
    s.part_one()
    s.part_two()


if __name__ == '__main__':
    main()
