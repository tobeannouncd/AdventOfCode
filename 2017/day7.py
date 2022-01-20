from collections import Counter, defaultdict
from functools import cache
import re
from typing import Dict, Iterable, List
import advent


class Program:
    def __init__(self, name: str, weight) -> None:
        self.name = name
        self.weight = weight
        self.holding = {}
        self.held_by = None

    def weight_tower(self):
        return self.weight + sum(child.weight_tower() for child in self.holding.values())

    def is_balanced(self):
        if not self.holding:
            return True
        if len(set(child.weight_tower() for child in self.holding.values())) == 1:
            return True
        return False

    def odd_child(self):
        for child in self.holding.values():
            if not child.is_balanced():
                return child
        l = list(self.holding)
        w = []
        for n in l:
            w.append(self.holding[n].weight_tower())
        c = Counter(w)
        if len(c) == 2:
            ww, _ = c.most_common(2)[1]
            i = w.index(ww)
            return self.holding[l[i]]
        return False


def main(debug=False):
    tree = advent.get_input(2017, 7).splitlines()
    programs = {}
    parent = part1(tree, programs, debug)
    print(f'Part 1: {parent}')
    print(f'Part 2: {part2(programs, parent, debug)}')


def part1(txt: list, programs, debug: bool):
    for line in txt:
        name, *carrying = re.findall('[a-z]+', line)
        weight = int(*re.findall(r'\d+', line))
        p = program_factory(programs, name, weight)
        for child in carrying:
            pp = program_factory(programs, child)
            p.holding[child] = pp
            pp.held_by = p
    while pp.held_by is not None:
        pp = pp.held_by
    return pp.name


def program_factory(program_dict: dict, name: str, weight=None):
    if name not in program_dict:
        program_dict[name] = Program(name, weight)
    p = program_dict[name]
    if p.weight is None and weight is not None:
        p.weight = weight
    return p


def part2(programs: Dict[str, Program], parent: str, debug: bool):
    p = programs[parent]
    pp = p.odd_child()
    while pp:
        p = pp
        pp = p.odd_child()

    prnt = p.held_by
    # sibling_names = list(prnt.holding)
    wt = p.weight_tower()
    ss = set(prnt.holding[nm].weight_tower() for nm in prnt.holding)-{wt}
    ret = p.weight-(wt-ss.pop())

    return ret


if __name__ == '__main__':
    main()
