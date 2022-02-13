from itertools import product

import advent
from intcode import Intcode


def solve(inp: str, noun1:int=12, verb1:int=2):
    program = list(map(int, inp.split(',')))
    computer = Intcode(program)
    computer[1:3] = noun1, verb1
    computer.run()
    yield computer[0]
    for noun, verb in product(range(100), repeat=2):
        computer = Intcode(program)
        computer[1:3] = noun, verb
        computer.run()
        if computer[0] == 19690720:
            yield 100*noun + verb
            break


def main():
    day = 2
    inp = advent.get_input(2019, day)
    advent.run(solve, inp)
    # advent.run(solve,'1,9,10,3,2,3,11,0,99,30,40,50',9,10)


if __name__ == '__main__':
    main()
