from collections import Counter
from itertools import product
import numpy as np

import advent


def main():
    data = advent.get_input(2020, 17)

    print(solve(data, part=1))
    print(solve(data, part=2))


def solve(data, part: int):
    grid = np.array([[list(l) for l in data.strip().splitlines()]])
    if part == 2:
        grid = grid.reshape(grid.shape + (1,))
    for _ in range(6):
        grid = evolve(grid)
    return np.count_nonzero(grid == '#')


def pad(grid: np.ndarray) -> np.ndarray:
    n_dims = len(grid.shape)
    return np.pad(grid, tuple((1, 1) for _ in range(n_dims)), constant_values='.')


def evolve(grid: np.ndarray) -> np.ndarray:
    grid = pad(grid)
    new = grid.copy()
    for pos in product(*(range(s) for s in grid.shape)):
        val = grid[pos]
        c = Counter(neighbors(grid, pos))
        if val == '#' and c['#'] not in (2, 3):
            new[pos] = '.'
        elif val == '.' and c['#'] == 3:
            new[pos] = '#'
    return new


def neighbors(grid: np.ndarray, pos):
    for pos_change in product(range(-1, 2), repeat=len(pos)):
        if all(coord == 0 for coord in pos_change):
            continue
        new_pos = [c+d for c, d in zip(pos, pos_change)]
        if any(c < 0 for c in new_pos) or any(c == s for c, s in zip(new_pos, grid.shape)):
            continue
        yield grid.item(*new_pos)


if __name__ == '__main__':
    main()
