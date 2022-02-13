from copy import deepcopy
from dataclasses import dataclass, field
from itertools import combinations
from math import lcm
import re
import advent


@dataclass
class Moon:
    pos: list
    vel: list = field(default_factory=lambda: [0, 0, 0])
    init_vals: tuple = field(init=False)
    period: list[int] = field(default_factory=lambda: [None, None, None])
    stp: int = 0
    # mem: tuple[list] = field(default_factory=lambda: ([],[],[]))

    def __post_init__(self):
        # init_vals = ((x0, vx0), (y0, vy0), (z0, vz0))
        self.init_vals = tuple((p, v) for p, v in zip(self.pos, self.vel))

    def step(self):
        self.stp += 1
        for i, v in enumerate(self.vel):
            self.pos[i] += v
            if self.period[i] is None and (self.pos[i], v) == self.init_vals[i]:
                self.period[i] = self.stp

    def potential(self):
        return sum(map(abs, self.pos))

    def kinetic(self):
        return sum(map(abs, self.vel))

    def energy(self):
        return self.potential()*self.kinetic()


def apply_gravity(moons: list[Moon]):
    for a, b in combinations(moons, 2):
        for i, (pa, pb) in enumerate(zip(a.pos, b.pos)):
            if pa < pb:
                a.vel[i] += 1
                b.vel[i] -= 1
            elif pa > pb:
                a.vel[i] -= 1
                b.vel[i] += 1
    for moon in moons:
        moon.step()


def solve(inp: str, n_steps=1000):
    moons = []
    init_pos = []
    for line in inp.splitlines():
        xyz = list(map(int, re.findall(r'-?\d+', line)))
        moons.append(Moon(xyz))
        init_pos.append(list(xyz))
    for _ in range(n_steps):
        apply_gravity(moons)
    # print(moons)
    yield sum(moon.energy() for moon in moons)
    xyz_lists = tuple(list(c) for c in zip(*init_pos))
    periods = []
    for c in xyz_lists:
        c_init = c.copy()
        v = [0]*len(c)
        stp = 0
        while True:
            stp += 1
            for i, cc in enumerate(c):
                for dd in c:
                    if cc < dd:
                        v[i] += 1
                    elif cc > dd:
                        v[i] -= 1
            for i, vv in enumerate(v):
                c[i] += vv
            if c == c_init and all(vv==0 for vv in v):
                break
        periods.append(stp)
    yield lcm(*periods)

def main():
    year, day = 2019, 12
    inp = advent.get_input(year, day)
    samp = '''<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>'''
    samp2 = '''<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>'''
    advent.run(solve, inp)


if __name__ == '__main__':
    main()
