from functools import reduce
from math import prod
import advent
import re
from itertools import product

RE_PAT = re.compile(
    r'(\w+):.+?(-?\d+).+?(-?\d+).+?(-?\d+).+?(-?\d+).+?(-?\d+)')


def main():
    inp = advent.get_input(2015, 15).splitlines()
    d = {}
    for line in inp:
        g = RE_PAT.match(line).groups()
        name = g[0]
        d[name] = tuple(map(int, g[1:]))
    l = list(d.values())
    # print(l)
    best_score = 0, None
    for p in product(range(101), repeat=len(d)):
        if sum(p) != 100:
            continue
        sc = [0]*4
        for n, props in zip(p, l):
            for i, prop in enumerate(props[:4]):
                sc[i] += n*prop
        if any(s <= 0 for s in sc):
            continue
        tot_score = prod(sc)
        if tot_score > best_score[0]:
            best_score = tot_score, p
    print(best_score)

    best_score = 0,None
    for p in product(range(101), repeat=len(d)):
        if sum(p) != 100:
            continue
        if sum(qty*props[-1] for qty, props in zip(p, l)) != 500:
            continue
        sc = [0]*4
        for n, props in zip(p, l):
            for i, prop in enumerate(props[:4]):
                sc[i] += n*prop
        if any(s <= 0 for s in sc):
            continue
        tot_score = prod(sc)
        if tot_score > best_score[0]:
            best_score = tot_score, p
    print(best_score)
        

if __name__ == '__main__':
    main()
