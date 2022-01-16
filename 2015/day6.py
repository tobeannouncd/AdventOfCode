from collections import defaultdict
from itertools import product
import re


def cmd_2(s_cmd, val_init):
    if s_cmd == 'on':
        val = val_init + 1
    elif s_cmd == 'off':
        val = max(0, val_init-1)
    elif s_cmd == 'toggle':
        val = val_init + 2
    return val


def main():
    fn = 'input/day6.txt'
    cmds = []
    pat = re.compile(r'(\w+) (\d+,\d+) through (\d+,\d+)')
    with open(fn) as f:
        for line in f:
            cmd, s_start, s_end = pat.search(line).groups()
            i_start = tuple(map(int, s_start.split(',')))
            i_end = tuple(map(int, s_end.split(',')))
            cmds.append((cmd, i_start, i_end))
    lights = defaultdict(int)
    for cmd, start, end in cmds:
        a, b = start
        c, d = end
        for i, j in product(range(a, c+1), range(b, d+1)):
            pt = complex(i, j)
            if cmd == 'on':
                lights[pt] = 1
            elif cmd == 'off' and pt in lights:
                del lights[pt]
            elif cmd == 'toggle':
                if pt in lights:
                    del lights[pt]
                else:
                    lights[pt] = 1
    print(sum(lights.values()))
    lights = defaultdict(int)
    for cmd,start,end in cmds:
        a,b = start
        c,d=end
        for i,j in product(range(a,c+1),range(b,d+1)):
            pt = complex(i,j)
            lights[pt] = cmd_2(cmd,lights[pt])
    print(sum(lights.values()))


if __name__ == '__main__':
    main()
