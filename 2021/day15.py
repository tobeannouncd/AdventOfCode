from collections import defaultdict
from math import inf
import heapq

from numpy.core.numeric import cross


with open('input/day15.txt') as f:
    grid = list(list(map(int, line.strip())) for line in f)


def crossNeighbors(r, c, h, w):
    for i, j in ((1, 0), (0, 1), (0, -1), (-1, 0)):
        if r+i in range(h) and c+j in range(w):
            yield r+i, c+j


def dijkstra(grid):
    nRows, nCols = len(grid), len(grid[0])
    source = (0, 0)
    dest = (nRows-1, nCols-1)

    queue = [(0, source)]
    mindist = defaultdict(lambda: inf, {source: 0})
    visited = set()

    while queue:
        dist, node = heapq.heappop(queue)

        if node == dest:
            return dist

        if node in visited:
            continue

        visited.add(node)
        r, c = node
        for neighbor in filter(lambda n: n not in visited, crossNeighbors(r, c, nRows, nCols)):
            nr, nc = neighbor
            newdist = dist + grid[nr][nc]

            if newdist < mindist[neighbor]:
                mindist[neighbor] = newdist
                heapq.heappush(queue, (newdist, neighbor))
    return inf


minrisk = dijkstra(grid)
print(f'Part 1: {minrisk}')

tilew, tileh = len(grid), len(grid[0])
for _ in range(4):
    for row in grid:
        tail = row[-tilew:]
        row.extend((x+1) if x < 9 else 1 for x in tail)
for _ in range(4):
    for row in grid[-tileh:]:
        row = [(x+1) if x < 9 else 1 for x in row]
        grid.append(row)

minrisk = dijkstra(grid)
print(f'Part 2: {minrisk}')
