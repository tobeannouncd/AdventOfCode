import advent
from collections import defaultdict
from itertools import permutations


def main():
    inp = advent.get_input(2015, 13).splitlines()
    # print(*inp, sep='\n')
    d = defaultdict(dict)
    for line in inp:
        sp = line.rstrip('.').split()
        name_a, gain_lose, val, name_b = (sp[i] for i in (0, 2, 3, -1))
        val = {'gain': 1, 'lose': -1}[gain_lose] * int(val)
        d[name_a][name_b] = val
    # print(d['Mallory'])
    max_happiness = 0
    for p in permutations(d):
        h = 0
        p_ring = (p[-1], *p, p[0])
        for left, name, right in zip(p_ring, p_ring[1:], p_ring[2:]):
            h += d[name][left] + d[name][right]
        max_happiness = max(max_happiness, h)
    print(max_happiness)
    for name in d:
        d[name]['TBA'] = 0
    for name in d.copy():
        d['TBA'][name] = 0
    # print(d)
    max_happiness = 0
    for p in permutations(d):
        h = 0
        p_ring = (p[-1], *p, p[0])
        for left, name, right in zip(p_ring, p_ring[1:], p_ring[2:]):
            h += d[name][left] + d[name][right]
        max_happiness = max(max_happiness, h)
    print(max_happiness)

if __name__ == '__main__':
    main()
