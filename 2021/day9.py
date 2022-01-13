from io import StringIO
import itertools

import numpy as np
import numpy.ma as ma

inputfile = './input/day9.txt'
# inputfile = StringIO('''2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678''')


def neighbors(ar, i, j):
    return {ar[i-1,j],
            ar[i+1,j],
            ar[i,j-1],
            ar[i,j+1]}


a = np.genfromtxt(inputfile, dtype='i', delimiter=1)
nRows, nCols = a.shape
b = np.pad(a, ((1, 1), (1, 1)), constant_values=10)
lowPoints = []
for i, j in itertools.product(range(1, nRows+1), range(1, nCols+1)):
    if all(b[i,j] < foo for foo in neighbors(b,i,j)):
        lowPoints.append(b[i,j])
print(sum(1+n for n in lowPoints))
