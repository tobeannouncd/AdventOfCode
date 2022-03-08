from dataclasses import dataclass, field
from operator import attrgetter

import advent


@dataclass
class Amphipod:
    variety: str
    pos: tuple[int, int]
    move_cost: int = field(init=False)

    def __post_init__(self):
        if self.variety == 'A':
            self.move_cost = 1
        elif self.variety == 'B':
            self.move_cost = 10
        if self.variety == 'C':
            self.move_cost = 100
        elif self.variety == 'D':
            self.move_cost = 1000


def parse(input_string: str):
    amphipods = []
    grid = {}
    for x in range(11):
        grid[x, 0] = None
    for y in (1, 2):
        for x in (2, 4, 6, 8):
            grid[x, y] = None

    for y, line in enumerate(input_string.splitlines()[1:]):
        for x, char in enumerate(line[1:]):
            if char in 'ABCD':
                a = Amphipod(char, (x, y))
                amphipods.append(a)
                grid[x, y] = a

    return grid, amphipods


def print_grid(grid):
    out = ['#'*13]

    line = '#'
    for x in range(11):
        if grid[x, 0] is None:
            line += '.'
        elif isinstance(grid[x, 0], Amphipod):
            line += grid[x, 0].variety
    out.append(line+'#')

    line = '##'
    for x in range(2, 9, 2):
        line += '#'
        if grid[x, 1] is None:
            line += '.'
        elif isinstance(grid[x, 1], Amphipod):
            line += grid[x, 1].variety
    out.append(line+'###')

    line = '  '
    for x in range(2, 9, 2):
        line += '#'
        if grid[x, 2] is None:
            line += '.'
        elif isinstance(grid[x, 2], Amphipod):
            line += grid[x, 2].variety
    out.append(line+'#')
    out.append('  ' + '#'*9)

    print('\n'.join(out))


def move(grid, amphipod: Amphipod, destination):
    """moves amphipod to destination, returns cost of move"""
    x, y = amphipod.pos
    xx, yy = destination
    dist = abs(x-xx) + abs(y-yy)
    cost = dist*amphipod.move_cost
    grid[x, y] = None
    grid[destination] = amphipod
    amphipod.pos = destination
    return cost


def path_empty(grid, start, finish):
    """returns true if path between start and finish (exclusive of endpoints) is empty"""
    x, y = start
    xx, yy = finish
    if y == 0:
        # left case
        if xx < x:
            for i in range(xx, x):
                if grid[i, 0] is not None:
                    return False
        # right case
        elif x < xx:
            for i in range(x+1, xx+1):
                if grid[i, 0] is not None:
                    return False
        # check spaces in hole
        for j in range(1, yy):
            if grid[xx, j] is not None:
                return False
    else:
        # check above
        for j in range(y):
            if grid[x, j] is not None:
                return False
        # left case
        if xx < x:
            for i in range(xx+1, x):
                if grid[i,0] is not None:
                    return False
        # right case
        elif x < xx:
            for i in range(x+1, xx):
                if grid[i,0] is not None:
                    return False
    return True


def valid_targets(grid, amphipod: Amphipod):
    if amphipod.pos[1] == 0:  # next destination must be home column
        # find home column
        home_x = ('ABCD'.index(amphipod.variety))*2 + 2
        if grid[home_x, 1] is not None:
            return
        if not path_empty(grid, amphipod.pos, (home_x, 1)):
            return
        if grid[home_x, 2] is None:
            yield home_x, 2
        elif grid[home_x, 2].variety == amphipod.variety:
            yield home_x, 1
        return
    for x in (0, 1, 3, 5, 7, 9, 10):
        if grid[x, 0] is None and path_empty(grid, amphipod.pos, (x, 0)):
            yield x, 0


def solved(grid):
    if any(grid[x, 0] is not None for x in range(11)):
        return False
    for x in (2, 4, 6, 8):
        idx = x//2 - 1
        for y in (1, 2):
            if grid[x, y].variety != 'ABCD'[idx]:
                return False
    return True

def solve(grid, amphipods: list[Amphipod]):

    pass

def grid_to_state(grid):
    state = ''
    for x in range(11):
        y = 0
        if grid[x,y] is None:
            state += '.'
        else:
            state += grid[x,y].variety
    for x in (2, 4, 6, 8):
        for y in (1, 2):
            if grid[x,y] is None:
                state += '.'
            else:
                state += grid[x,y].variety
    return state
                
def state_to_grid(state):
    grid = {}
    for i, char in enumerate(state[:11]):
        x, y = i, 0
        if char == '.':
            grid[x,y] = None
        else:
            grid[x,y] = Amphipod(char,(x,y))
    for i, char in enumerate(state[11:]):
        x = 2*(i//2 + 1)
        y = i % 2 + 1
        if char == '.':
            grid[x,y] = None
        else:
            grid[x,y] = Amphipod(char,(x,y))
    return grid
        

def main():
    input_text = advent.get_input(2021, 23)
    grid, amphipods = parse(input_text)
    # for a in sorted(amphipods, key=attrgetter('pos')):
    #     print(a)
    print_grid(grid)
    for a in amphipods:
        print(a)
        print(list(valid_targets(grid, a)))

    pass


def test():
    g, _ = parse('''#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #########''')
    s = grid_to_state(g)
    print(s)
    g = state_to_grid(s)
    print_grid(g)


if __name__ == '__main__':
    main()
    # test()
