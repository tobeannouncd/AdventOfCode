import advent


def dist(pos: complex):
    hor, ver = map(abs, (pos.real, pos.imag))
    if ver >= hor:
        return int(hor + (ver-hor)//2)
    if hor % 2 == 0:
        return int(hor)
    return int(hor+1)


def solve(inp):
    dirs = inp.split(',')
    pos = 0j
    dir_map = {'s': -2j, 'n': 2j, 'se': 1-1j,
               'sw': -1-1j, 'ne': 1+1j, 'nw': -1+1j}
    max_dist = 0
    for dir in dirs:
        pos += dir_map[dir]
        if dist(pos)>max_dist:
            max_dist = dist(pos)
    # print(pos)
    print(dist(pos), max_dist)


def main():
    foo = advent.get_input(2017, 11)
    solve(foo)


if __name__ == '__main__':
    main()
