import operator as op
from functools import reduce

filename = 'input/day16.txt'


def getInput(filename):
    with open(filename) as i:
        ret = i.read()
    return ret.strip().split('\n')


def peek(data, n, bits=False):
    ret = data[0][:n]
    if not bits:
        ret = int(ret, 2)
    data[0] = data[0][n:]
    return ret


def processVal(vals, typeID):
    opers = {0: op.add, 1: op.mul, 5: op.gt, 6: op.lt, 7: op.eq}
    if typeID == 2:
        return min(vals)
    elif typeID == 3:
        return max(vals)
    else:
        return reduce(opers[typeID], vals)


def parse(data, sumVer=[0]):
    ver = peek(data, 3)
    sumVer[0] += ver

    typeID = peek(data, 3)
    if typeID == 4:
        binNum = ''
        while True:
            flag = peek(data, 1)
            binNum += peek(data, 4, bits=True)
            if not flag:
                break
        retVal = int(binNum, 2)
    else:
        lenID = peek(data, 1)
        subVals = []
        if lenID:
            numSubpackets = peek(data, 11)
            for _ in range(numSubpackets):
                data, _, subVal = parse(data, sumVer)
                subVals.append(subVal)
        else:
            lenSubpackets = peek(data, 15)
            subpackets = [peek(data, lenSubpackets, bits=True)]
            while subpackets[0]:
                subpackets, _, subVal = parse(subpackets, sumVer)
                subVals.append(subVal)
        retVal = processVal(subVals, typeID)

    return data, sumVer[0], retVal


def solve(data):
    for line in data:
        l = 4*len(line)
        line = bin(int(line, 16))[2:].zfill(l)
        _, part1, part2 = parse([line])
        print(f'Part 1: {part1}')
        print(f'Part 2: {part2}')


if __name__ == '__main__':
    data = getInput(filename)
    solve(data)
