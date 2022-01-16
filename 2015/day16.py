import advent
import re

RE_PAT = re.compile(r'\w+: \d+')

TAPE = {'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1}


def main():
    sue_list = advent.get_input(2015, 16).splitlines()
    sue_dict = {}
    for i, line in enumerate(sue_list, start=1):
        items = RE_PAT.findall(line)
        d = {}
        for item in items:
            k, v = item.split(': ')
            d[k] = int(v)
        sue_dict[i] = d
    matches = []
    for sue, inv in sue_dict.items():
        if all(TAPE[itm] == inv[itm] for itm in inv):
            matches.append(sue)
    print(*matches)
    matches = []
    for sue, inv in sue_dict.items():
        candidate = True
        for itm, qty in inv.items():
            if itm in ('cats', 'trees'):
                if qty <= TAPE[itm]:
                    candidate = False
                    break
            elif itm in ('pomeranians', 'goldfish'):
                if qty >= TAPE[itm]:
                    candidate = False
                    break
            elif qty != TAPE[itm]:
                candidate = False
                break
        if candidate:
            matches.append(sue)
    print(*matches)


if __name__ == '__main__':
    main()
