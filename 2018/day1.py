import advent


def main(debug=False):
    freq_changes = advent.get_input(2018, 1)
    print(f'Part 1: {part1(freq_changes, debug)}')
    print(f'Part 2: {part2(freq_changes, debug)}')


def part1(txt: str, debug: bool):
    freq = 0
    for line in txt.splitlines():
        freq += int(line)
    return freq


def part2(txt: str, debug: bool):
    freq = 0
    seen = set()
    i = 0
    lst = txt.splitlines()
    llst = len(lst)
    while freq not in seen:
        seen.add(freq)
        freq += int(lst[i])
        i = (i+1) % llst
    return freq


if __name__ == '__main__':
    main()
