import advent


def main():
    data = tuple(map(int, advent.get_input(2020, 15).strip().split(',')))

    solve(data, part=1)
    solve(data, part=2)


def solve(data, part):
    if part == 1:
        n = 2020
    elif part == 2:
        n = 30000000
    next = data[-1]
    i_last = {val: i for i, val in enumerate(data)}
    for i in range(len(data)-1, n-1):
        i_last[next], next = i, i-i_last.get(next, i)
    print(next)


if __name__ == '__main__':
    main()
