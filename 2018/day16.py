from enum import Enum, auto
from itertools import combinations
import operator
import re
from collections import defaultdict, namedtuple

import advent

INSTRUCTIONS = 'addi,addr,muli,mulr,bani,banr,bori,borr,seti,setr,gtir,gtri,gtrr,eqrr,eqri,eqir'.split(
    ',')


def execute(inst: str, a: int, b: int, c: int, regs: list[int]):
    if inst.startswith('add'):
        func = operator.add
        val_a = regs[a]
        val_b = b if inst.endswith('i') else regs[b]
    if inst.startswith('mul'):
        func = operator.mul
        val_a = regs[a]
        val_b = b if inst.endswith('i') else regs[b]
    if inst.startswith('ban'):
        func = operator.and_
        val_a = regs[a]
        val_b = b if inst.endswith('i') else regs[b]
    if inst.startswith('bor'):
        func = operator.or_
        val_a = regs[a]
        val_b = b if inst.endswith('i') else regs[b]
    if inst.startswith('set'):
        func = (lambda x, _: x)
        val_a = regs[a] if inst.endswith('r') else a
        val_b = b
    if inst.startswith('gt'):
        func = (lambda x,y: int(x>y))
        val_a = a if inst[2] == 'i' else regs[a]
        val_b = b if inst[3] == 'i' else regs[b]
    if inst.startswith('eq'):
        func = (lambda x,y: int(x==y))
        val_a = a if inst[2] == 'i' else regs[a]
        val_b = b if inst[3] == 'i' else regs[b]

    regs[c] = func(val_a, val_b)


def part_one(data: str):
    samples, test_program = data.split('\n\n\n\n')

    possibilities = defaultdict(set)
    ans = 0
    for sample in samples.split('\n\n'):
        bef, code, aft = (tuple(map(int, re.findall(r'\d+', x)))
                          for x in sample.splitlines())
        opcode, a, b, c = code
        for instr in INSTRUCTIONS:
            result = list(bef)
            execute(instr, a, b, c, result)
            if tuple(result) == aft:
                possibilities[opcode].add(instr)
        if len(possibilities[opcode]) >= 3:
            ans += 1
    print(ans)

    opcode_map = {}
    while possibilities:
        for n, s in tuple(possibilities.items()):
            if len(s) == 1:
                inst = s.pop()
                opcode_map[n] = inst
                del possibilities[n]
        for n, s in possibilities.items():
            for inst in opcode_map.values():
                s.discard(inst)

    registers = [0, 0, 0, 0]
    for line in test_program.splitlines():
        opcode, a, b, c = map(int, line.split())
        execute(opcode_map[opcode], a, b, c, registers)
        
    print(registers[0])


def main():
    data = advent.get_input(2018, 16)
    part_one(data)


if __name__ == '__main__':
    main()
