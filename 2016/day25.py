from itertools import count

import advent
from day12 import Assembunny, parse


class Antenna(Assembunny):
    def __init__(self, program, a=0) -> None:
        super().__init__(program)
        self.instructions['out'] = self.out
        self.pulse = False
        self.output = None
        self['a'] = a
        
    def out(self, x):
        self.output = self.read(x), self.state()
        self.pulse = True
    
    def state(self):
        memory = '\n'.join(' '.join(map(str, line)) for line in self.mem)
        regs = tuple(self.registers[x] for x in 'abcd')
        return memory, self.idx, regs
    
    def clock(self):
        while not self.pulse:
            self.process()
        self.pulse = False
        return self.output
            
def main():
    inp_text = advent.get_input(2016,25)
    program = tuple(tuple(line) for line in parse(inp_text))
    init_val, max_iters = find_clock_init(program)
    print(f'Part 1: {init_val}')
    print(f'If the clock works {max_iters} times, it should work forever.')

def find_clock_init(program):
    zero_states = set()
    one_states = set()
    ant = Antenna(program)
    max_iters = 0
    for init_val in count(0):
        ant.__init__(program, init_val)
        zero_states.clear()
        one_states.clear()
        bad = False
        iterations_needed = 0
        while True:
            zero, state = ant.clock()
            iterations_needed += 1
            if zero != 0:
                bad = True
                break
            if state in zero_states:
                break
            zero_states.add(state)
            one, state = ant.clock()
            iterations_needed += 1
            if one != 1:
                bad = True
                break
            if state in one_states:
                break
            one_states.add(state)
        max_iters = max(max_iters, iterations_needed)
        if not bad:
            break
    return init_val, max_iters
    

if __name__ == '__main__':
    main()
