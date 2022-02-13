from dataclasses import dataclass, field
import advent

SPELL_COSTS = {'Missile': 53, 'Drain': 73,
               'Shield': 113, 'Poison': 173, 'Recharge': 229}

STARTING_HP = 50
STARTING_MANA = 500


@dataclass
class Player:
    boss_health: int
    boss_damage: int
    hp: int = STARTING_HP
    mana: int = STARTING_MANA
    manaspent: int = 0
    effects: dict = field(default_factory=dict)

    def cast(self, spell):
        if spell == 'Missile':
            self.boss_health -= 4
        elif spell == 'Drain':
            self.boss_health -= 2
            self.hp += 2
        elif spell == 'Shield':
            self.effects['Shield'] = 6
        elif spell == 'Poison':
            self.effects['Poison'] = 6
        elif spell == 'Recharge':
            self.effects['Recharge'] = 5
        self.mana -= SPELL_COSTS[spell]
        self.manaspent += SPELL_COSTS[spell]

    def upkeep(self):
        for e, v in self.effects.items():
            if e == 'Poison':
                self.boss_health -= 3
            elif e == 'Recharge':
                self.mana += 101
            v -= 1
        for e, v in self.effects.copy().items():
            if v == 0:
                del self.effects[e]

    def boss_attack(self):
        dmg = max(self.boss_damage - (7 if 'Shield' in self.effects else 0), 1)
        self.hp -= dmg

    def who_is_dead(self):
        if self.hp <= 0:
            return 'Player has died'
        elif self.boss_health <= 0:
            return 'Boss has died'
        return False


def game(boss_hp, boss_dmg):





def main():
    sInput = advent.get_input(2015, 22).splitlines()
    boss_hp = int(sInput[0].split()[-1])
    boss_dmg = int(sInput[1].split()[-1])
    players = [Player(boss_hp, boss_dmg))]
    


if __name__ == '__main__':
    main()
