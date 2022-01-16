from collections import defaultdict
from itertools import product
import advent

ROWS = 100
COLS = 100
STEPS = 100


def neighbor_pts(pt: complex):
    for i, j in product(range(-1, 2), repeat=2):
        offset = complex(i, j)
        if offset == 0:
            continue
        n = pt + offset
        if any((n.real < 0, n.imag < 0, n.real >= COLS, n.imag >= ROWS)):
            continue
        yield n


def game_of_life(grid, steps=STEPS, part=1):
    d = grid.copy()
    for _ in range(steps):
        dd = d.copy()
        for i, j in product(range(ROWS), range(COLS)):
            pt = complex(i, j)
            if part == 2 and pt in (0, complex(0, COLS-1), complex(ROWS-1, COLS-1), complex(ROWS-1, 0)):
                continue
            s = sum(d[n] for n in neighbor_pts(pt))
            if d[pt] and s not in (2, 3):
                del dd[pt]
            elif not d[pt] and s == 3:
                dd[pt] = 1
        d = dd
    return d


def main():
    grid = advent.get_input(2015, 18).splitlines()
    d = defaultdict(int)
    for i, j in product(range(ROWS), range(COLS)):
        if grid[i][j] == '#':
            d[complex(i, j)] = 1

    d_a = game_of_life(d)
    print(sum(d_a.values()))
    d_b = game_of_life(d, part=2)
    print(sum(d_b.values()))


if __name__ == '__main__':
    main()
