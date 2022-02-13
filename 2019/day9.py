import advent
from intcode import Intcode

def solve(inp: str):
    program = tuple(map(int, inp.split(',')))
    computer = Intcode(program,1)
    yield computer.outputs[-1]
    computer = Intcode(program,2)
    yield computer.outputs[-1]

def main():
    inp = advent.get_input(2019,9)
    sample = '''109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'''
    advent.run(solve, inp)

if __name__ == '__main__':
    main()
