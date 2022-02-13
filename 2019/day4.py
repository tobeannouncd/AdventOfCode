from itertools import groupby
import re
import advent


def solve(inp: str):
    min_val, max_val = inp.split('-')
    candidates = set()
    for val in range(int(min_val), int(max_val)+1):
        val_str = str(val)
        if re.search(r'(\d)\1', val_str) and all(b >= a for a, b in zip(val_str, val_str[1:])):
            candidates.add(val_str)
    yield len(candidates)
    for candidate in list(candidates):
        groups = [list(g) for k, g in groupby(candidate)]
        if all(len(group) != 2 for group in groups):
            candidates.discard(candidate)
    yield len(candidates)


def main():
    year, day = 2019, 4
    inp = advent.get_input(year, day)
    advent.run(solve, inp)


if __name__ == '__main__':
    main()
