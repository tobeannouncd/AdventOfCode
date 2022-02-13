from itertools import cycle, permutations

import advent
from intcode import Intcode


def solve(inp: str):
    program = tuple(map(int, inp.split(',')))
    outputs = []
    for setting_combo in permutations(range(5), 5):
        signal = 0
        amps = gen_amps(program, setting_combo)
        for amp in amps:
            amp.run(signal)
            signal = amp.outputs[0]
        outputs.append(signal)
    yield max(outputs)
    outputs = []
    for setting_combo in permutations(range(5, 10), 5):
        signal = 0
        amps = gen_amps(program, setting_combo)
        amp_cycle = cycle(amps)
        while True:
            amp = next(amp_cycle)
            if amp.done:
                break
            amp.run(signal)
            signal = amp.outputs[-1]
        outputs.append(signal)
    yield max(outputs)


def gen_amps(program, setting_combo):
    amps = []
    for setting in setting_combo:
        amps.append(Intcode(program, setting))
    return amps


def main():
    inp = advent.get_input(2019, 7)
    samp = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'
    advent.run(solve, inp)


if __name__ == '__main__':
    main()
