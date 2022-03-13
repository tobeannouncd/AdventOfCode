import numpy as np

import advent

MONSTER = '''
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''.strip('\n')


class Tile:
    def __init__(self, data: str) -> None:
        foo, text = data.split('\n', 1)
        self.id = int(foo.split()[1][:-1])
        self.grid = np.array([list(l) for l in text.splitlines()])
        self.up, self.down, self.right, self.left = [None]*4

    def __repr__(self) -> str:
        return f'Tile({self.id})'

    @property
    def top_edge(self):
        return ''.join(self.grid[0])

    @property
    def bottom_edge(self):
        return ''.join(self.grid[-1])

    @property
    def left_edge(self):
        '''returns the left edge of the tile ordered from top down'''
        return ''.join(self.grid[:, 0])

    @property
    def right_edge(self):
        '''returns the right edge of the tile ordered from top down'''
        return ''.join(self.grid[:, -1])

    def __str__(self) -> str:
        out = []
        for line in self.grid:
            out.append(''.join(line))
        return '\n'.join(out)

    def rot_cw(self):
        self.grid = np.rot90(self.grid, k=1)

    def flip_lr(self):
        self.grid = np.fliplr(self.grid)

    @property
    def edges(self):
        out = set()
        flip = np.fliplr(self.grid)
        for i in range(4):
            out.add(''.join(np.rot90(self.grid, i)[0]))
            out.add(''.join(np.rot90(flip, i)[0]))
        return out

    def find_overlap(self, other):
        if not self.edges & other.edges:
            return False

        if self.top_edge in other.edges:
            self.up = other
            other.down = self
            i = 0
            while other.bottom_edge != self.top_edge:
                if i == 3:
                    other.flip_lr()
                other.rot_cw()
                i += 1
        elif self.left_edge in other.edges:
            self.left = other
            other.right = self
            i = 0
            while other.right_edge != self.left_edge:
                if i == 3:
                    other.flip_lr()
                other.rot_cw()
                i += 1
        elif self.right_edge in other.edges:
            self.right = other
            other.left = self
            i = 0
            while other.left_edge != self.right_edge:
                if i == 3:
                    other.flip_lr()
                other.rot_cw()
                i += 1
        elif self.bottom_edge in other.edges:
            self.down = other
            other.up = self
            i = 0
            while other.top_edge != self.bottom_edge:
                if i == 3:
                    other.flip_lr()
                other.rot_cw()
                i += 1

        return True


def main():
    data = advent.get_input(2020, 20)

    tiles = [Tile(g) for g in data.strip().split('\n\n')]

    unique_id, grid = part_one(tiles)
    print(unique_id)

    sea_map = part_two(grid)

    # for line in sea_map:
    #     print(''.join(line))

    print(np.count_nonzero(sea_map == '#'))


def part_two(grid, verbose=False):
    for row in grid:
        for t in row:
            assert isinstance(t, Tile)
            t.grid = t.grid[1:-1, 1:-1]
    rows = []
    for row in grid:
        rows.append(np.concatenate([t.grid for t in row], axis=1))
    sea_map = np.concatenate(rows)
    monster_coords = set()

    for i, line in enumerate(MONSTER.splitlines()):
        for j, val in enumerate(line):
            if val == '#':
                monster_coords.add((i, j))

    i = 0
    while not monster_in_grid(monster_coords, sea_map):
        if i == 3:
            sea_map = np.fliplr(sea_map)
        else:
            sea_map = np.rot90(sea_map, 1)
        i += 1

    replace_monster(monster_coords, sea_map)
    return sea_map


def monster_in_grid(monster_coords, grid: np.ndarray):
    rows, cols = grid.shape
    i_locs, j_locs = zip(*monster_coords)
    for i in range(rows - max(i_locs)):
        for j in range(cols - max(j_locs)):
            if all(grid[i+ii, j+jj] == '#' for ii, jj in monster_coords):
                return True
    return False


def replace_monster(monster_coords, grid):
    rows, cols = grid.shape
    i_locs, j_locs = zip(*monster_coords)
    for i in range(rows - max(i_locs)):
        for j in range(cols - max(j_locs)):
            if all(grid[i+ii, j+jj] == '#' for ii, jj in monster_coords):
                for ii, jj in monster_coords:
                    grid[i+ii, j+jj] = 'O'


def part_one(tiles):
    in_grid = set()
    in_grid.add(tiles[0])
    seen = set()

    while any(t not in seen for t in tiles):
        cur = [t for t in in_grid if t not in seen][0]
        seen.add(cur)

        for other in (t for t in tiles if t not in seen):
            s = cur.find_overlap(other)
            if s:
                in_grid.add(other)

    left_tile = [t for t in tiles if t.left is None if t.up is None][0]
    grid = []
    row = [left_tile]
    while row[-1].right is not None:
        row.append(row[-1].right)
    grid.append(row)
    while left_tile.down is not None:
        left_tile = left_tile.down
        row = [left_tile]
        while row[-1].right is not None:
            row.append(row[-1].right)
        grid.append(row)
    ans = 1
    for t in (grid[0][0], grid[0][-1], grid[-1][0], grid[-1][-1]):
        ans *= t.id
    return ans, grid


if __name__ == '__main__':
    main()
