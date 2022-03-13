from collections import Counter
from itertools import product
import advent


def main():
    data = advent.get_input(2020, 11).strip()

    print(solve(data, part=1))
    print(solve(data, part=2))


def solve(data, part):
    grid = [list(l) for l in data.splitlines()]
    while True:
        next = evolve(grid, part)
        if next == grid:
            break
        grid = next
    ans = 0
    for line in grid:
        ans += line.count('#')
    return ans


def evolve(grid, part):
    new = []
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(evolve_cell(i, j, grid, part))
        new.append(row)
    return new


def evolve_cell(i, j, grid, part):
    val = grid[i][j]
    if part == 1:
        c = Counter(neighbors(i, j, grid))
    elif part == 2:
        c = Counter(visible(i, j, grid))
    if val == 'L' and c['#'] == 0:
        return '#'
    if val == '#' and c['#'] >= 4 and part == 1:
        return 'L'
    if val == '#' and c['#'] >= 5 and part == 2:
        return 'L'
    return val


def neighbors(i, j, grid):
    rows = len(grid)
    cols = len(grid[0])
    for di, dj in product(range(-1, 2), repeat=2):
        if di == dj == 0:
            continue
        ii, jj = i+di, j+dj
        if ii < 0 or jj < 0 or ii == rows or jj == cols:
            continue
        yield grid[ii][jj]


def visible(i: int, j: int, grid: list):
    rows = len(grid)
    cols = len(grid[0])
    for di, dj in product(range(-1, 2), repeat=2):
        if di == dj == 0:
            continue
        ii, jj = i+di, j+dj
        while True:
            if ii < 0 or jj < 0 or ii == rows or jj == cols:
                break
            val = grid[ii][jj]
            if val in 'L#':
                yield val
                break
            ii += di
            jj += dj


if __name__ == '__main__':
    main()
