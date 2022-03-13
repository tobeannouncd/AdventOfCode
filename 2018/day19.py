'''
The program described in my input file consists of two portions:

1) Generate a large number and store in register 2
2) store the sum of all divisors of this number in register 0

without knowing the structure of how 
'''

import advent
from day16 import execute


def part_one(data: str):
    print(run(data))


def run(data, *, part=1):
    ip, *program = data.splitlines()
    registers = [0]*6
    if part == 2:
        registers[0] = 1
    idx_pointer = int(ip.split()[-1])
    program_rng = range(len(program))

    while registers[idx_pointer] in program_rng:
        i = registers[idx_pointer]
        if i == 1:
            break
        line = program[i]
        inst, *args = line.split()
        a, b, c = map(int, args)
        execute(inst, a, b, c, registers)
        registers[idx_pointer] += 1
    n = registers[2]
    ans = 0
    for i in range(1, int(n**.5)+1):
        if n % i == 0:
            ans += i + n//i
            if i*i == n:
                ans -= i
    return ans


def part_two(data):
    print(run(data, part=2))


def main():
    data = advent.get_input(2018, 19)
    part_one(data)
    part_two(data)


if __name__ == '__main__':
    main()
