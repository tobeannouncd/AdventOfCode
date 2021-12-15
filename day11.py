from itertools import product

import numpy as np

from advent import getData

data = getData(day=11)
d_array = np.array([[int(a) for a in line.strip()] for line in data])


def step(ar: np.ndarray) -> np.ndarray:
    q = []
    with np.nditer(ar, flags=['multi_index'], op_flags=['readwrite']) as it:
        for val in it:
            val += 1
            if val == 10:
                q.append(it.multi_index)
    while len(q):
        pt = q.pop()
        for pt2 in getNeighbors(pt, ar):
            ar[pt2] += 1
            if ar[pt2] == 10:
                q.append(pt2)
    ar[ar > 9] = 0
    return 100-np.count_nonzero(ar)


def getNeighbors(pt, ar: np.ndarray):
    x, y = pt
    rows, cols = ar.shape
    for i, j in product([-1, 0, 1], repeat=2):
        if all((x+i in range(rows),
                y+j in range(cols),
                (i, j) != (0, 0))):
            yield (x+i, y+j)


numFlashes = 0
stepNum = 0
stepFlashes = 0
while stepFlashes < 100:
    stepFlashes = step(d_array)
    stepNum += 1
    numFlashes += stepFlashes
    if stepNum == 100:
        print(numFlashes)
print(stepNum)
