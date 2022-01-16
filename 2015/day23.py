import advent


class Computer:
    def __init__(self, mem: list = None, reg_a: int = 0) -> None:
        self.reg = {'a': reg_a, 'b': 0}
        self.pos = 0
        if mem is None:
            self.mem = []
        else:
            self.mem = mem.copy()
        self.cmd_lookup = {'hlf': self.hlf, 'tpl': self.tpl, 'inc': self.inc,
                           'jmp': self.jmp, 'jie': self.jie, 'jio': self.jio}

    def run(self):
        try:
            line = self.mem[self.pos]
            cmd, args = line[:3], line[4:].split(', ')
            self.cmd_lookup[cmd](*args)
            return True
        except IndexError:
            print(f'Execution Finished')
            return False

    def hlf(self, r):
        self.reg[r] //= 2
        self.pos += 1

    def tpl(self, r):
        self.reg[r] *= 3
        self.pos += 1

    def inc(self, r):
        self.reg[r] += 1
        self.pos += 1

    def jmp(self, offset):
        self.pos += int(offset)

    def jie(self, r, offset):
        if self.reg[r] % 2 == 0:
            self.jmp(offset)
        else:
            self.pos += 1

    def jio(self, r, offset):
        if self.reg[r] == 1:
            self.jmp(offset)
        else:
            self.pos += 1


def main():
    mem = advent.get_input(2015, 23).splitlines()
    comp = Computer(mem)
    while True:
        a = comp.run()
        if not a:
            break
    print(comp.reg)
    comp = Computer(mem, reg_a=1)
    while True:
        a = comp.run()
        if not a:
            break
    print(comp.reg)


if __name__ == '__main__':
    main()
