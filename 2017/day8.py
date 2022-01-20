import operator as op
from collections import defaultdict

import advent

COMPARISONS = {'!=': op.ne, '>=': op.ge, '<=': op.le,
               '>': op.gt, '==': op.eq, '<': op.lt}

OPERATORS = {'inc': op.add, 'dec': op.sub}


def main(debug=False):
    instructions = advent.get_input(2017, 8)
    ans1, ans2 = part1(instructions, debug)
    print(f'Part 1: {ans1}')
    print(f'Part 2: {ans2}')


def part1(txt: str, debug: bool):
    reg_dict = defaultdict(int)
    highest_val = 0
    for line in txt.splitlines():
        left, right = line.split(' if ')
        reg, oper, val = left.split()
        reg_comp, comp, val_comp = right.split()
        if COMPARISONS[comp](reg_dict[reg_comp], int(val_comp)):
            reg_dict[reg] = OPERATORS[oper](reg_dict[reg], int(val))
            highest_val = max(highest_val, max(reg_dict.values()))
    return max(reg_dict.values()), highest_val


if __name__ == '__main__':
    main()
