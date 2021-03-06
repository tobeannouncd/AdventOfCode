import operator as op
from functools import reduce

_filename = 'input/day16.txt'
OPERS = {0: op.add, 1: op.mul, 2: (lambda x, y: min(x, y)),
         3: (lambda x, y: max(x, y)), 5: op.gt, 6: op.lt, 7: op.eq}


def peek(data, n, bits=False):
    ret = data[0][:n]
    if not bits:
        ret = int(ret, 2)
    data[0] = data[0][n:]
    return ret


def parse(data, sum_ver=[0]):
    ver = peek(data, 3)
    sum_ver[0] += ver

    type_id = peek(data, 3)
    if type_id == 4:
        ret_val = 0
        while True:
            flag = peek(data, 1)
            ret_val = (ret_val << 4) + peek(data, 4)
            if not flag:
                break
    else:
        len_id = peek(data, 1)
        subvals = []
        if len_id:
            n_subpackets = peek(data, 11)
            for _ in range(n_subpackets):
                data, _, sub_val = parse(data, sum_ver)
                subvals.append(sub_val)
        else:
            lenSubpackets = peek(data, 15)
            subpackets = [peek(data, lenSubpackets, bits=True)]
            while subpackets[0]:
                subpackets, _, sub_val = parse(subpackets, sum_ver)
                subvals.append(sub_val)
        ret_val = reduce(OPERS[type_id], subvals)

    return data, sum_ver[0], ret_val


if __name__ == '__main__':
    with open(_filename) as i:
        data = i.read().strip().split('\n')
    for line in data:
        l = 4*len(line)
        line = bin(int(line, 16))[2:].zfill(l)
        print('Part 1: {1}\nPart 2: {2}'.format(*parse([line])))
