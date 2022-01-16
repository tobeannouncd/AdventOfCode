from collections import defaultdict
import re
import advent

RE_PAT = re.compile(r'[A-Z][a-z]?')


def tokenize(s: str):
    return RE_PAT.findall(s)


def main():
    lst_in = advent.get_input(2015, 19).splitlines()
    repl_map = defaultdict(set)
    for line in lst_in[:-2]:
        a, b = line.split(' => ')
        repl_map[a].add(b)
    mol = lst_in[-1]

    mods = single_repl(repl_map, mol)

    print('Part 1:', len(mods))

    reverse_map = defaultdict(set)
    for a, s in repl_map.items():
        if a == 'e':
            continue
        for b in s:
            reverse_map[b].add(a)
    # print(repl_map['e'])
    print(sorted(reverse_map))
    print(mol)


def single_repl(repl_map, mol):
    mods = set()
    for aa in repl_map:
        for bb in repl_map[aa]:
            for m in re.finditer(aa, mol):
                mods.add(mol[:m.start()] + bb + mol[m.start()+len(aa):])
    return mods


if __name__ == '__main__':
    main()
