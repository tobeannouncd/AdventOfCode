import advent
from intcode import Intcode


def solve(inp: str):
    pgm = tuple(map(int, inp.split(',')))
    computer = Intcode(pgm,1)
    computer.run()
    assert not any(computer.outputs[:-1])
    yield computer.outputs[-1]
    computer = Intcode(pgm,5)
    computer.run()
    assert len(computer.outputs) == 1
    yield computer.outputs[0]
    


def main():
    year, day = 2019, 5
    inp = advent.get_input(year, day)
    advent.run(solve, inp)
    # advent.run(solve,'3,0,4,0,99')


if __name__ == '__main__':
    main()
