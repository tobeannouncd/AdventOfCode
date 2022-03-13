import re
from collections import defaultdict
from itertools import product

import advent


def main():
    data = advent.get_input(2020, 14).strip().splitlines()

    part_one(data)

    part_two(data)


def part_two(data):
    mem = defaultdict(int)
    for line in data:
        if line.startswith('mask'):
            mask = line.split(' = ')[-1]
            continue
        idx, val = digits(line)
        floating_addr = bitmask(mask, idx, ver=2)
        for addr in address_iter(floating_addr):
            mem[addr] = val
    print(sum(mem.values()))


def part_one(data):
    mem = defaultdict(int)
    for line in data:
        if line.startswith('mask'):
            mask = line.split(' = ')[-1]
            continue
        idx, val = digits(line)
        mem[idx] = bitmask(mask, val)
    print(sum(mem.values()))


def digits(s: str):
    return (int(n) for n in re.findall(r'\d+', s))


def bitmask(mask: str, n: int, ver=1) -> int | str:
    n_bin = bin(n)[2:].rjust(36, '0')
    out = ''
    for m, b in zip(mask, n_bin):
        if m == 'X' and ver == 1:
            out += b
        elif m == '0' and ver == 2:
            out += b
        else:
            out += m
    if ver == 1:
        return int(out, 2)
    if ver == 2:
        return out


def address_iter(addr: str):
    float_locs = [i for i, val in enumerate(addr) if val == 'X']
    for p in product('01', repeat=len(float_locs)):
        new_addr = list(addr)
        for i, n in zip(float_locs, p):
            new_addr[i] = n
        yield int(''.join(new_addr), 2)


if __name__ == '__main__':
    main()
