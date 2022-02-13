from itertools import chain
import advent


class Assembunny:
    def __init__(self, program) -> None:
        self.registers = dict.fromkeys('abcd', 0)
        self.mem = [list(line) for line in program]
        self.idx = 0
        self.instructions = {'cpy': self.cpy, 'inc': self.inc,
                             'dec': self.dec, 'jnz': self.jnz,
                             'add': self.add, 'incmul': self.incmul}
        self.opt = {}
        self.optimize()

    def __setitem__(self, key, value):
        if key not in self.registers:
            raise KeyError
        self.registers[key] = value

    def __getitem__(self, key):
        return self.registers[key]

    def read(self, value):
        try:
            return self[value]
        except KeyError:
            return int(value)

    def process(self):
        if self.idx in self.opt:
            instruction, *args = self.opt[self.idx]
        else:
            instruction, *args = self.mem[self.idx]
        self.idx += 1
        func = self.instructions[instruction]
        func(*args)

    def optimize(self):
        self.opt.clear()
        for i in range(len(self.mem)-2):  # ADD
            l = self.mem[i] + self.mem[i+1] + self.mem[i+2]
            if len(l) != 7 or l[0] != 'inc' or l[2] != 'dec' or l[4] != 'jnz':
                continue
            d, c, cc, offset = (l[j] for j in (1, 3, 5, 6))
            if d == c or c != cc or self.read(offset) != -2:
                continue
            if offset == d or offset == c:
                continue
            self.opt[i] = f'add {c} {d}'.split()

        for i in range(len(self.mem)-5):
            if i+1 not in self.opt:
                continue
            if self.mem[i][0] != 'cpy' or self.mem[i+4][0] != 'dec' or self.mem[i+5][0] != 'jnz':
                continue
            args = list(chain.from_iterable(
                self.mem[j][1:] for j in range(i, i+6)))
            n, d, a, dd, _, _, c, cc, offset = args
            if n == a or n == dd or n == c:
                continue
            if d == dd and c == cc and d != c and a != c and offset == '-5':
                self.opt[i] = f'incmul {a} {n} {c} {d}'.split()

    def incmul(self, a, n, c, d):
        if all(k in self.registers for k in (a, c, d)):
            self[a] += self.read(n)*self.read(c)
            self[c] = 0
            self[d] = 0
            self.idx += 5

    def add(self, c, d):
        if d in self.registers and c in self.registers:
            self[d] += self.read(c)
            self[c] = 0
            self.idx += 2

    def cpy(self, x, y):
        if y in self.registers:
            self[y] = self.read(x)

    def inc(self, x):
        if x in self.registers:
            self[x] += 1

    def dec(self, x):
        if x in self.registers:
            self[x] -= 1

    def jnz(self, x, y):
        if self.read(x):
            self.idx += self.read(y) - 1

    def run(self):
        while self.idx < len(self.mem):
            self.process()


def parse(input_text):
    for line in input_text.splitlines():
        l = line.split()
        # if l[0] not in ('cpy', 'inc', 'dec', 'jnz', 'tgl'):
        #     raise ValueError('Input data contains invalid instruction')
        yield l


def main():
    puzzle_input = advent.get_input(2016, 12)
    program = tuple(parse(puzzle_input))
    c = Assembunny(program)
    c.run()
    print(c['a'])
    c.__init__(program)
    c['c'] = 1
    c.run()
    print(c['a'])
    # print(c.incmul_calls)


if __name__ == '__main__':
    main()
