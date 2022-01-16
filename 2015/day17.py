from collections import Counter
from itertools import combinations

import advent

TARGET = 150

def main():
    containers = tuple(map(int, advent.get_input(2015, 17).splitlines()))
    ways = Counter()
    for r in range(1, len(containers)+1):
        for c in combinations(containers, r):
            if sum(c)==TARGET:
                ways[len(c)] += 1
    print('Part 1:', sum(ways.values()))
    print('Part 2:', min(ways.items())[-1])

if __name__ == '__main__':
    main()
