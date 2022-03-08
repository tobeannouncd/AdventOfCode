from collections import Counter
from copy import deepcopy
from itertools import product
import advent


def adjacent_values(i, j, area):
    rows = len(area)
    cols = len(area[0])
    for di, dj in product(range(-1, 2), repeat=2):
        if di == 0 and dj == 0:
            continue
        ii, jj = i + di, j + dj
        if ii not in range(rows) or jj not in range(cols):
            continue
        yield area[ii][jj]


def area_string(area):
    out = []
    for row in area:
        line = ''.join(row)
        out.append(line)
    return '\n'.join(out)


def main():
    data = advent.get_input(2018, 18)
#     data = '''.#.#...|#.
# .....#|##|
# .|..|...#.
# ..|#.....#
# #.#|||#|#|
# ...#.||...
# .|....|...
# ||...#|.#|
# |.||||..|.
# ...#.|..|.'''

    area = [list(row) for row in data.splitlines()]
    solution(deepcopy(area))
    solution(deepcopy(area), part=2)


def solution(area, part=1, verbose=False):
    if verbose:
        print(area_string(area))
    rows = len(area)
    cols = len(area[0])

    cycles = [area_string(area)]

    while True:
        new_area = [[None]*cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                c = Counter(adjacent_values(i, j, area))
                val = area[i][j]
                if val == '.' and c['|'] >= 3:
                    new_area[i][j] = '|'
                elif val == '|' and c['#'] >= 3:
                    new_area[i][j] = '#'
                elif val == '#' and (c['|'] == 0 or c['#'] == 0):
                    new_area[i][j] = '.'
                else:
                    new_area[i][j] = area[i][j]
        area = new_area
        stop = 10 if part == 1 else 1_000_000_000
        if len(cycles) == stop:
            break
        a_str = area_string(area)
        if a_str in cycles:
            i = cycles.index(a_str)
            cycle_len = len(cycles) - i
            current = len(cycles)
            print(f'repeating pattern of {cycle_len} steps starts after {current} iterations')
            remaining = stop - current
            offset = remaining % cycle_len
            area = cycles[i+offset]
            break

        cycles.append(a_str)
        if verbose:
            print()
            print(f'Part {part}: {area_string(area)}')

    c = Counter()
    for row in area:
        c += Counter(row)
    print(c['|']*c['#'])


if __name__ == '__main__':
    main()
