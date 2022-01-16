from dataclasses import dataclass
from itertools import product
import advent

STARTING_HP = 100

WEAPONS = '''Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0'''

ARMOR = '''Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5'''

RINGS = '''Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3'''


@dataclass
class Item:
    name: str
    cost: int
    dmg: int = 0
    arm: int = 0


def main(debug=False):
    stat_lst = advent.get_input(2015, 21).splitlines()
    boss_stats = {}
    for line in stat_lst:
        k, v = line.split(': ')
        boss_stats[k] = int(v)
    wpns = parse_items(WEAPONS)
    armors = parse_items(ARMOR)
    rings = parse_items(RINGS, True)
    null_item = Item('none', 0)
    armors.append(null_item)
    rings.append(null_item)

    min_cost = None,None
    max_cost = 0,None
    for itms in product(wpns, armors, rings, rings):
        if itms[2] == itms[3]:
            continue
        my_hp, total_cost = battle(boss_stats, itms)
        if my_hp > 0:
            if min_cost[0] is None or min_cost[0] > total_cost:
                min_cost = total_cost,itms
        else:
            if total_cost > max_cost[0]:
                max_cost = total_cost, itms
    print(f'Part 1: {min_cost if debug else min_cost[0]}')
    print(f'Part 2: {max_cost if debug else max_cost[0]}')

def battle(boss_stats, itms):
    my_hp = STARTING_HP
    my_dmg = sum(itm.dmg for itm in itms)
    my_armr = sum(itm.arm for itm in itms)
    total_cost = sum(itm.cost for itm in itms)

    boss_hp = boss_stats['Hit Points']
    boss_dmg = boss_stats['Damage']
    boss_armr = boss_stats['Armor']

    my_turn = True
    while all(hp > 0 for hp in (my_hp, boss_hp)):
        if my_turn:
            boss_hp -= max(1, my_dmg-boss_armr)
        else:
            my_hp -= max(1, boss_dmg-my_armr)
        my_turn = not my_turn
    return my_hp,total_cost


def parse_items(r, ring=False):
    rings = []
    for line in r.splitlines():
        if ring:
            name, mod, cost, dmg, arm = line.split()
            rings.append(Item(' '.join((name, mod)),
                         int(cost), int(dmg), int(arm)))
        else:
            name, cost, dmg, arm = line.split()
            rings.append(Item(name, int(cost), int(dmg), int(arm)))

    return rings


if __name__ == '__main__':
    main()
