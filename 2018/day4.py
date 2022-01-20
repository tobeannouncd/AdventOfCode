from datetime import datetime
import re
import advent

RE_DIGITS = re.compile(r'\d+')


def to_datetime(s):
    yy, mm, dd, h, m = map(int, RE_DIGITS.findall(s))
    return datetime(yy, mm, dd, h, m)


def main(part=0, debug=False):
    records = advent.get_input(2018, 4)
    if part != 2:
        print(f'Part 1: {part1(records, debug)}')
    if part != 1:
        print(f'Part 2: {part2(records, debug)}')


def part1(txt: str, debug: bool):
    # for line in txt.splitlines():
    #     d,a = line[:18],line[18:]
    #     # if debug:
    #     #     print(d)
    #     dd = to_datetime(d)
    #     if debug:
    #         print(dd)
    l = txt.splitlines()
    ls = sorted(l, key=lambda x: to_datetime(x[:18]))
    if debug:
        print(*ls[:10], sep='\n')
    pass


def part2(txt, debug: bool):
    pass


if __name__ == '__main__':
    main(1, debug=True)
