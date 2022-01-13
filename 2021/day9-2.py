import itertools
import operator as op
from functools import reduce

import numpy as np

fname = './input/day9.txt'
caveMap = np.genfromtxt(fname, 'i', delimiter=1)


class Basin():
    def __init__(self) -> None:
        self.points = set()
        self.size = 0

    def add(self, point):
        if point not in self.points:
            self.points.add(point)
            self.size += 1


def neighborPoints(point, ar):
    i, j = point
    return set((x, y) for x, y in itertools.product([i-1, i, i+1], [j-1, j, j+1])
               if any((x == i, y == j))
               and all((x in range(ar.shape[0]), y in range(ar.shape[1]), (x, y) != (i, j))))


def combineBasins(b1, b2):
    bNew = Basin()
    for p in b1.points | b2.points:
        basins[p] = bNew
        bNew.add(p)
    return bNew


basins = {}
with np.nditer(caveMap, flags=['multi_index']) as it:
    for val in it:
        point = it.multi_index
        if val == 9:
            continue
        neighbors = neighborPoints(point, caveMap)
        bsns = set(basins[n] for n in neighbors if n in basins)
        if len(bsns):
            bsn = reduce(combineBasins, bsns)
        else:
            bsn = Basin()
        bsn.add(point)
        basins[point] = bsn

print(reduce(op.mul,sorted(bsn.size for bsn in set(basins.values()))[-3:]))
