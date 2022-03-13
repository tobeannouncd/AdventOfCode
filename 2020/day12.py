import advent


class Ferry:
    def __init__(self) -> None:
        self.pos = 0
        self.facing = 1

    def step(self, action: str, val: int):
        if action == 'N':
            self.pos += 1j * val
        if action == 'S':
            self.pos += -1j * val
        if action == 'E':
            self.pos += 1 * val
        if action == 'W':
            self.pos += -1 * val
        if action == 'L':
            self.facing *= pow(1j, val//90)
        if action == 'R':
            self.facing *= pow(-1j, val//90)
        if action == 'F':
            self.pos += self.facing * val

    @property
    def dist(self):
        return int(abs(self.pos.real) + abs(self.pos.imag))


class FerryTwo(Ferry):
    def __init__(self) -> None:
        super().__init__()
        self.waypoint = 10+1j

    def step(self, action: str, val: int):
        if action == 'N':
            self.waypoint += 1j * val
        if action == 'S':
            self.waypoint += -1j * val
        if action == 'E':
            self.waypoint += 1 * val
        if action == 'W':
            self.waypoint += -1 * val
        if action == 'L':
            self.waypoint *= pow(1j, val//90)
        if action == 'R':
            self.waypoint *= pow(-1j, val//90)
        if action == 'F':
            self.pos += self.waypoint * val


def main():
    data = advent.get_input(2020, 12).strip().splitlines()

    ferry_one = Ferry()
    ferry_two = FerryTwo()
    for direction in data:
        action, val = direction[0], int(direction[1:])
        ferry_one.step(action, val)
        ferry_two.step(action, val)
    print(ferry_one.dist)
    print(ferry_two.dist)


if __name__ == '__main__':
    main()
