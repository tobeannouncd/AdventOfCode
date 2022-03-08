from itertools import count
from time import perf_counter
import advent


class ALU:
    def __init__(self, inp=None) -> None:
        self.mem = []
        self.i = 0
        self.vars = dict.fromkeys('wxyz', 0)
        self.input_buffer = []
        if inp is not None:
            self.mem = list(self.parse_program(inp))

    def parse_program(self, inp: str):
        for line in inp.splitlines():
            yield line.strip().split()

    def execute(self, debug):
        command, a, *args = self.mem[self.i]
        self.i += 1
        if args and args[0] in self.vars:
            b = self.vars[args[0]]
        elif args:
            b = int(args[0])

        if command == 'inp':
            self.inp(a)
        elif command == 'add':
            self.add(a, b)
        elif command == 'mul':
            self.mul(a, b)
        elif command == 'div':
            self.div(a, b)
        elif command == 'mod':
            self.mod(a, b)
        elif command == 'eql':
            self.eql(a, b)

    def inp(self, a):
        self.vars[a] = int(self.input_buffer.pop())

    def add(self, a, b):
        self.vars[a] += b

    def mul(self, a, b):
        self.vars[a] *= b

    def div(self, a, b):
        self.vars[a] //= b

    def mod(self, a, b):
        self.vars[a] %= b

    def eql(self, a, b):
        self.vars[a] == int(self.vars[a] == b)

    def MONAD(self, num, debug=False):
        lst = list(str(num))
        if len(lst) != 14:
            return False
        while lst:
            digit = lst.pop()
            if digit == '0':
                return False
            self.input_buffer.append(digit)
        while self.i < len(self.mem):
            self.execute(debug)
        return self.vars['z'] == 0

    def reset(self):
        self.i = 0
        self.input_buffer.clear()
        for var in self.vars:
            self.vars[var] = 0


def solve(inp):
    c = count(pow(10, 14)-1, -1)
    alu = ALU(inp)
    t = perf_counter()
    for model_num in c:
        if perf_counter() - t > 5:
            t += 5
            print(f'current: {model_num}')
        if alu.MONAD(model_num):
            return model_num
        alu.reset()



def main():
    inp = advent.get_input(2021, 24)
    print(solve(inp))


if __name__ == '__main__':
    main()
