import advent


def main(debug=False):
    offsets = list(map(int, advent.get_input(2017, 5).splitlines()))
    part1(offsets.copy())
    part2(offsets.copy())


def part1(lst):
    domain = range(len(lst))
    i = 0
    n = 0
    while i in domain:
        dist = lst[i]
        lst[i] += 1
        i += dist
        n += 1
    print(n)


def part2(lst):
    domain = range(len(lst))
    i = 0
    n = 0
    while i in domain:
        dist = lst[i]
        lst[i] += 1 if lst[i] < 3 else -1
        i += dist
        n += 1
    print(n)


if __name__ == '__main__':
    main()
