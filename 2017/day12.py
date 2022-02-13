from dataclasses import dataclass, field
import advent


@dataclass
class Door:
    name: int
    neighbors: list = field(default_factory=list)


def get_door(name: int, door_dict: dict[int, Door]) -> Door:
    if name not in door_dict:
        door_dict[name] = Door(name)
    return door_dict[name]


def solve(inp: str):
    doors = {}
    for line in inp.splitlines():
        door, connections = line.split(' <-> ')
        d = get_door(int(door), doors)
        neighbors = list(map(int, connections.split(', ')))
        for neighbor in neighbors:
            d.neighbors.append(get_door(neighbor, doors))
    group = []
    q = [doors[0]]
    while q:
        d = q.pop()
        del doors[d.name]
        group.append(d)
        for n in d.neighbors:
            if n not in group:
                q.append(n)
    print(len(group))
    num_groups = 1
    while doors:
        group = []
        _,d = doors.popitem()
        q = [d]
        num_groups += 1
        while q:
            d = q.pop()
            if d.name in doors:
                del doors[d.name]
            group.append(d)
            for n in d.neighbors:
                if n not in group:
                    q.append(n)
    print(num_groups)


def main():
    foo = advent.get_input(2017, 12)
    solve(foo)


if __name__ == '__main__':
    main()
