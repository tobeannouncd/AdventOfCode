from functools import reduce
from operator import xor
from typing import Tuple
import advent

SUFFIX = bytes((17, 31, 73, 47, 23))
LOOP_LENGTH = 256
NUM_LOOPS = 64


class Twister:

    def __init__(self, lengths, debug, part=1) -> None:
        self.lengths = lengths
        self.loop_length = LOOP_LENGTH
        if debug and part == 1:
            self.loop_length = 5
        self.loop = list(range(self.loop_length))
        self.skipsize = 0
        self.pos = 0

    def twist(self, seg_length):
        loop_tmp = rotate_left(self.loop, self.pos)
        left, right = loop_tmp[:seg_length], loop_tmp[seg_length:]
        loop_tmp = left[::-1]+right
        return rotate_right(loop_tmp, self.pos)

    def run1(self):
        for length in self.lengths:
            self.step(length)

    def step(self, length):
        self.loop = self.twist(length)
        self.pos = (self.pos + length +
                    self.skipsize) % self.loop_length
        self.skipsize = (self.skipsize + 1) % self.loop_length

    def run2(self):
        for _ in range(NUM_LOOPS):
            self.run1()


def rotate_left(l: list, n: int):
    left, right = l[:n], l[n:]
    return right+left


def rotate_right(l: list, n: int):
    left, right = l[:-n], l[-n:]
    return right+left


def main(debug=False):
    input_string = advent.get_input(2017, 10)

    print(f'Part 1: {part1(input_string, debug)}')
    print(f'Part 2: {part2(input_string, debug)}')


def part1(input_string: str, debug: bool):
    if debug:
        input_string = '3,4,1,5'
    lengths = tuple(map(int, input_string.split(',')))
    t = Twister(lengths, debug)
    t.run1()
    if debug:
        print(f'{t.loop=}')
    a, b = t.loop[:2]
    return a*b


def dense_hash(sparse_hash):
    for i in range(16):
        yield reduce(xor, sparse_hash[16*i:16*i+16])


def part2(input_string: str, debug: bool):
    byte_str = input_string.encode('ascii') + SUFFIX
    t = Twister(byte_str, debug, 2)
    if debug:
        print(f'{list(byte_str)=}')
    t.run2()
    sparse_hash = t.loop
    if debug:
        sparse_hash = [65, 27, 9, 1, 4, 3, 40,
                       50, 91, 7, 6, 0, 2, 5, 68, 22]*16
        print(f'{sparse_hash=}')
    d = dense_hash(sparse_hash)
    if debug:
        print(f'{d=}')
    return ''.join(hex(ch)[2:] for ch in d)


if __name__ == '__main__':
    main()
