import operator
import re

import advent


class Formula:
    def __init__(self, data: str, part: int) -> None:
        self.equation = list(re.findall(r'\d+|[()+*]', data))
        if part == 1:
            self.operators = [{'*': operator.mul, '+': operator.add}]
        elif part == 2:
            self.operators = [{'+': operator.add}, {'*': operator.mul}]

    def calculate(self, eqn=None):
        if eqn is None:
            eqn = self.equation
        while '(' in eqn:
            i = eqn.index('(')
            j = i
            level = 1
            while eqn[j] != ')' or level != 0:
                j += 1
                if eqn[j] == '(':
                    level += 1
                elif eqn[j] == ')':
                    level -= 1
            sub_eqn = eqn[i+1:j]
            val = self.calculate(sub_eqn)
            eqn = eqn[:i] + [val] + eqn[j+1:]
        for op_dict in self.operators:
            while any(c in eqn for c in op_dict):
                i = min(eqn.index(c) for c in op_dict if c in eqn)
                op = eqn[i]
                left, right = eqn[i-1], eqn[i+1]
                op_func = op_dict[op]
                val = op_func(int(left), int(right))
                eqn = eqn[:i-1] + [val] + eqn[i+2:]
        assert len(eqn) == 1
        return eqn[0]


def main():
    data = advent.get_input(2020, 18)
    part_one = 0
    part_two = 0
    for line in data.strip().splitlines():
        formula_one = Formula(line, part=1)
        formula_two = Formula(line, part=2)
        part_one += formula_one.calculate()
        part_two += formula_two.calculate()
    print(part_one)
    print(part_two)


if __name__ == '__main__':
    main()
