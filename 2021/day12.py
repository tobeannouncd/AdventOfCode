from collections import Counter
from advent import getData


class Cave():
    def __init__(self) -> None:
        self.neighbors = set()

    def addNeighbor(self, n):
        self.neighbors.add(n)


def makeNodes(data):
    nodeDict = {}
    for line in data:
        a, b = line.strip().split('-')
        for node in [a, b]:
            if node not in nodeDict:
                nodeDict[node] = Cave()
        nodeDict[a].addNeighbor(b)
        nodeDict[b].addNeighbor(a)
    return nodeDict


def getPaths(nodes, maxSmallVisits):
    paths = set()
    q = []
    c = Counter()
    numPaths = 0
    for n in nodes['start'].neighbors:
        if n.islower() and n != 'end':
            if c[n] < maxSmallVisits:
                cn = c.copy()
                cn[n] += 1
                q.append((n, cn))
        elif n != 'end':
            q.append((n, c.copy()))
        else:
            pass
    pass


data = getData(12)

nodes = makeNodes(data)  # TODO

part1 = getPaths(nodes, 1)  # TODO
