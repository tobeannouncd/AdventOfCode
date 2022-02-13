import advent


class Node:
    def __init__(self, name) -> None:
        self.name = name
        self.parent = None
        self.num_orbs = None

    def n_orbits(self):
        
        if self.num_orbs is None:
            if self.parent is None:
                self.num_orbs = 0
            else:
                self.num_orbs = 1 + self.parent.n_orbits()
        return self.num_orbs

    def path(self):
        p = []
        n = self
        while n.parent is not None:
            p.append(n)
            n = n.parent
        return p


def get_node(name: str, s: dict):
    if name not in s:
        s[name] = Node(name)
    return s[name]


def solve(inp: str):
    node_set = {}
    for line in inp.splitlines():
        par, child = line.split(')')
        n_par = get_node(par, node_set)
        n_child = get_node(child, node_set)
        n_child.parent = n_par
    yield sum(n.n_orbits() for n in node_set.values())
    path_you = node_set['YOU'].path()
    path_san = node_set['SAN'].path()
    a,b = None, None
    while a is b:
        a,b = path_you.pop(), path_san.pop()
    yield len(path_you)+len(path_san)

def main():
    year, day = 2019, 6
    inp = advent.get_input(year, day)
    advent.run(solve, inp)
    sample = '''COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN'''
    advent.run(solve, sample)


if __name__ == '__main__':
    main()
