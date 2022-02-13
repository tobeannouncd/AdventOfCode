import advent
from day12 import Assembunny, parse


class Safe(Assembunny):
    def __init__(self, program, a) -> None:
        super().__init__(program)
        self.instructions['tgl'] = self.tgl
        self['a'] = a

    def tgl(self, x):
        idx = self.idx - 1 + self.read(x)
        if idx not in range(len(self.mem)):
            return
        instruction, *args = self.mem[idx]
        if len(args) == 1:
            if instruction == 'inc':
                self.mem[idx][0] = 'dec'
            else:
                self.mem[idx][0] = 'inc'
        elif len(args) == 2:
            if instruction == 'jnz':
                self.mem[idx][0] = 'cpy'
            else:
                self.mem[idx][0] = 'jnz'
        self.optimize()


def main():
    program = list(parse(advent.get_input(2016, 23)))
    for i, solution in enumerate(solve(program), start=1):
        print(f'Part {i}: {solution}')


def solve(program):
    c = Safe(program, 7)
    c.run()
    yield c['a']
    c.__init__(program, 12)
    c.run()
    yield c['a']


if __name__ == '__main__':
    main()
