import re
from collections import defaultdict
from itertools import product

import advent

RE_PAT = re.compile(r'\d+')


def main(part=0, debug=False):
    claims = advent.get_input(2018, 3).splitlines()
    if part != 2:
        print(f'Part 1: {part1(claims, debug)}')
    if part != 1:
        print(f'Part 2: {part2(claims, debug)}')


def part1(claims, debug: bool):
    if debug:
        claims = """#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2""".splitlines()
    m = defaultdict(int)
    for claim in claims:
        _, col, row, w, t = map(int, RE_PAT.findall(claim))
        for i, j in product(range(col, col+w), range(row, row+t)):
            m[(i, j)] += 1
    return sum(v > 1 for v in m.values())


def part2(claims, debug: bool):
    if debug:
        claims = """#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2""".splitlines()
    m = defaultdict(int)
    claim_areas = defaultdict(set)
    for claim in claims:
        n, col, row, w, t = map(int, RE_PAT.findall(claim))
        for i, j in product(range(col, col+w), range(row, row+t)):
            m[(i, j)] += 1
            claim_areas[n].add((i, j))
    for claim_num, points in claim_areas.items():
        if all(m[point] == 1 for point in points):
            return claim_num


if __name__ == '__main__':
    main()
