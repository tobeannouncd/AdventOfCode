from collections import defaultdict

import advent

DIRS = {
    'w': -2,
    'nw': -1+1j,
    'sw': -1-1j,
    'e': 2,
    'ne': 1+1j,
    'se': 1-1j
}


def dest(line: str):
    dist = 0
    cur = ''
    for char in line:
        if char in 'ns':
            cur = char
        elif char in 'ew':
            cur += char
            dist += DIRS[cur]
            cur = ''
    if cur != '':
        dist += DIRS[cur]
    return dist


def adjacent_positions(pos):
    for d in DIRS.values():
        yield pos+d


def evolve(black_points: set):
    white_points = set(adj for p in black_points for adj in adjacent_positions(p)
                       if adj not in black_points)
    new_black = set()
    for p in black_points:
        n_adj_black = len(black_points.intersection(adjacent_positions(p)))
        if n_adj_black in (1, 2):
            new_black.add(p)
    for p in white_points:
        n_adj_black = len(black_points.intersection(adjacent_positions(p)))
        if n_adj_black == 2:
            new_black.add(p)
    return new_black


def main():
    data = advent.get_input(2020, 24).strip().splitlines()
    black_tiles = part_one(data)
    print(sum(black_tiles.values()))
    black_points = set(p for p, v in black_tiles.items() if v)
    for _ in range(100):
        black_points = evolve(black_points)
    print(len(black_points))


def part_one(data):
    black_tiles = defaultdict(bool)
    for line in data:
        d = dest(line)
        black_tiles[d] = not black_tiles[d]
    return black_tiles


if __name__ == '__main__':
    main()
