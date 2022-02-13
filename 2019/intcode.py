from collections import defaultdict
import operator
from typing import Iterable


class Intcode:
    def __init__(self, mem: Iterable[int], *inputs) -> None:
        # self.mem = list(mem)
        self.mem = defaultdict(int)
        self.mem.update(enumerate(list(mem)))
        self.pos = 0
        self.done = False
        self.inputs = []
        for inp in inputs:
            self.inputs.append(inp)
        self.pause = False
        self.outputs = []
        self.rel_base = 0
        if self.inputs:
            self.run()

    def __getitem__(self, key) -> int:
        if isinstance(key, slice):
            out = []
            for itm in range(key.start, key.stop, key.step):
                if itm < 0:
                    raise KeyError('Cannot access memory at negative address')
                out.append(itm)
            return out
        return self.mem[key]

    def __setitem__(self, key, value):
        if isinstance(key, slice):
            if key.step is not None and key.step != 1:
                raise KeyError('slice step can only be 1')
            assert (key.stop-key.start) == len(value)
            assert key.start >= 0
            for i, v in zip(range(key.start, key.stop), value):
                self.mem[i] = v
        else:
            self.mem[key] = value

    def run(self, *inputs):
        self.pause = False
        for inp in inputs:
            self.inputs.append(inp)
        while not self.done and not self.pause:
            self.process()

    def scan(self, mode) -> int:
        idx = self.interpret_mode(mode)
        return self[idx]

    def interpret_mode(self, mode):
        if mode == 0:
            idx = self[self.pos]
        elif mode == 1:
            idx = self.pos
        elif mode == 2:
            idx = self[self.pos] + self.rel_base
        self.pos += 1
        return idx

    def process(self):
        modes_opcode = str(self[self.pos]).rjust(5, '0')
        self.pos += 1
        modes = list(map(int, modes_opcode[:3]))
        opcode = int(modes_opcode[3:])
        if opcode == 1:
            self.arith(modes, operator.add)
        elif opcode == 2:
            self.arith(modes, operator.mul)
        elif opcode == 3:
            self.input(modes)
        elif opcode == 4:
            self.output(modes)
        elif opcode == 5:
            self.jump(modes, True)
        elif opcode == 6:
            self.jump(modes, False)
        elif opcode == 7:
            self.arith(modes, operator.lt)
        elif opcode == 8:
            self.arith(modes, operator.eq)
        elif opcode == 9:
            self.set_relbase(modes)
        elif opcode == 99:
            self.done = True

    def set_relbase(self, modes):
        param = self.scan(modes.pop())
        self.rel_base += param

    def arith(self, modes, func):
        params = (self.scan(modes.pop()) for _ in range(2))
        val = func(*params)
        self.write(int(val), modes.pop())

    def write(self, val, mode):
        idx = self.interpret_mode(mode)
        self[idx] = val

    def input(self, modes):
        if not self.inputs:
            self.pause = True
            self.pos -= 1
            return
        val = self.inputs.pop()
        self.write(val, modes.pop())

    def output(self, modes):
        val = self.scan(modes.pop())
        self.outputs.append(val)

    def jump(self, modes, compare):
        val = self.scan(modes.pop())
        dest = self.scan(modes.pop())
        if bool(val) == compare:
            self.pos = dest


def main():
    pass


if __name__ == '__main__':
    main()
