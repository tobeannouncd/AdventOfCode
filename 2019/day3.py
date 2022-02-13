from typing import Iterable
import advent


def solve(inp: str):
    wire_a, wire_b = (line.split(',') for line in inp.splitlines())
    dirs = {'R': 1+0j, 'L': -1+0j, 'U': 1j, 'D': -1j}
    path_a, path_b = (make_path(wire, dirs) for wire in [wire_a, wire_b])
    intersections = set(path_a) & set(path_b)
    yield min(map(manhattan, intersections))
    d = {}
    for point in intersections:
        times = []
        times.append(1+path_a.index(point))
        times.append(1+path_b.index(point))
        d[point] = times
    yield min(sum(v) for v in d.values())


def manhattan(pt_a: complex, pt_b: complex = 0j) -> int:
    for pt in (pt_a, pt_b):
        assert pt.imag.is_integer()
        assert pt.real.is_integer()
    d = pt_a - pt_b
    return int(abs(d.real) + abs(d.imag))


def make_path(wire1: Iterable[str], dirs: dict[str, complex]) -> list[complex]:
    path1 = []
    pos1 = 0j
    for step in wire1:
        direction = dirs[step[0]]
        dist = int(step[1:])
        for _ in range(dist):
            pos1 += direction
            path1.append(pos1)
    return path1


def main():
    year, day = 2019, 3
    inp = advent.get_input(2019, 3)
    advent.run(solve, inp)


if __name__ == '__main__':
    main()
