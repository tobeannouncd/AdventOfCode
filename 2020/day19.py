from functools import reduce
from itertools import product
import re
import advent

CASES = {
    'character': 0,
    'or': 1,
    'and': 2
}

SAMPLE_DATA = '''0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb'''


def regex_and(pattern_a: str, pattern_b: str):
    groups_a = pattern_a.split('|')
    groups_b = pattern_b.split('|')
    matches = []
    for group_a, group_b in product(groups_a, groups_b):
        matches.append(group_a + group_b)
    return '|'.join(matches)


def regex_or(pattern_a: str, pattern_b: str):
    groups = pattern_a.split('|')
    groups.extend(pattern_b.split('|'))
    return '|'.join(groups)


class Solution:
    def __init__(self, data: str) -> None:
        rules, messages = data.split('\n\n')

        self.messages = messages.splitlines()

        self.rules = {}
        for line in rules.splitlines():
            left, right = line.split(': ')
            line_num = int(left)
            if right[0] == '"':
                rule = CASES['character'], right[1]
            elif '|' in right:
                left, right = right.split(' | ')
                left_cond = tuple(map(int, left.split()))
                right_cond = tuple(map(int, right.split()))
                rule = CASES['or'], (left_cond, right_cond)
            else:
                rule = CASES['and'], tuple(map(int, right.split()))
            self.rules[line_num] = rule

    def make_regex(self, rule_num):
        case, val = self.rules[rule_num]
        if case == CASES['character']:
            return val
        if case == CASES['or']:
            foo = []
            for nums in val:
                regex_list = [self.make_regex(n) for n in nums]
                foo.append(reduce(regex_and, regex_list))
            return reduce(regex_or, foo)
        if case == CASES['and']:
            regex_list = [self.make_regex(n) for n in val]
            return reduce(regex_and, regex_list)

    def part_one(self, show_regex=False):
        pattern = self.make_regex(0)
        if show_regex:
            print(len(pattern))
        candidates = set(pattern.split('|'))
        print(len(candidates.intersection(self.messages)))

    def part_two(self):
        pass


def main():
    data = advent.get_input(2020, 19)
    # data = SAMPLE_DATA
    s = Solution(data)
    s.part_one(True)


if __name__ == '__main__':
    main()
