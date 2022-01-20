from collections import Counter
from itertools import combinations
import advent


def main(debug=False):
    candidates = advent.get_input(2018, 2).splitlines()
    print(f'Part 1: {part1(candidates, debug)}')
    print(f'Part 2: {part2(candidates, debug)}')


def part1(candidates, debug: bool):
    cnt2, cnt3 = 0, 0
    for c in candidates:
        cc = Counter(c)
        if 2 in cc.values():
            cnt2 += 1
        if 3 in cc.values():
            cnt3 += 1
    return cnt2*cnt3


def part2(candidates, debug: bool):
    if debug:
        print(num_str_diffs('abcde', 'axcye'))
        print(num_str_diffs('fghij', 'fguij'))
    out = ''
    for a,b in combinations(candidates,2):
        if num_str_diffs(a,b) == 1:
            for aa,bb in zip(a,b):
                if aa==bb:
                    out += aa
            break
    return out


def num_str_diffs(st1, st2):
    # cnt = 0
    # for a, b in zip(st1, st2):
    #     if a != b:
    #         cnt += 1
    # return cnt
    return sum(a != b for a, b in zip(st1, st2))


if __name__ == '__main__':
    main()
