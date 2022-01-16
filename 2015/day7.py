import operator as op
from collections import deque

OPERS = {'AND': op.and_, 'OR': op.or_, 'LSHIFT': op.lshift,
         'RSHIFT': op.rshift, 'NOT': lambda x: x ^ 0xFFFF}
FN = 'input/day7.txt'


def parseable(left: str, wire_list):
    tokens = left.split()
    for token in tokens:
        if token in OPERS or token.isnumeric():
            continue
        if token not in wire_list:
            return False
    return True


def parse(left: str, wire_list):
    tokens = left.split()
    q = []
    cmd = lambda x: x
    for token in tokens:
        if token.isnumeric():
            q.append(int(token))
        elif token in OPERS:
            cmd = OPERS[token]
        else:
            q.append(wire_list[token])
    return cmd(*q)


def main():
    with open(FN) as f:
        data = f.read().strip().split('\n')
    # print(type(data))
    wires = {}
    q = deque(data)
    # lines_done = 0
    while q:
        line = q.pop()
        left, right = line.split(' -> ')
        if parseable(left, wires):
            wires[right] = parse(left, wires)
            # lines_done += 1
        else:
            q.appendleft(line)
        # if lines_done and lines_done%10==0:
        #     print(f'{lines_done} lines complete')
    part_one = wires['a']
    print(part_one)

    q=deque()
    wires = {}
    for line in data:
        _,right = line.split(' -> ')
        if right == 'b':
            q.append(f'{part_one} -> b')
        else:
            q.append(line)
    while q:
        line = q.pop()
        left, right = line.split(' -> ')
        if parseable(left, wires):
            wires[right] = parse(left, wires)
            # lines_done += 1
        else:
            q.appendleft(line)
        # if lines_done and lines_done%10==0:
        #     print(f'{lines_done} lines complete')
    part_two = wires['a']
    print(part_two)

if __name__ == '__main__':
    main()
