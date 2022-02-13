from typing import Iterable
import advent


def fuel_required(mass: int) -> int:
    return mass//3 - 2


def solve(inp) -> Iterable:
    masses = list(map(int, inp.splitlines()))
    yield sum(fuel_required(m) for m in masses)
    new_fuel = 0
    for mass in masses:
        fuel = [fuel_required(mass)]
        fuel2 = fuel_required(fuel[-1])
        while fuel2 > 0:
            fuel.append(fuel2)
            fuel2 = fuel_required(fuel[-1])
        new_fuel += sum(fuel)
    yield new_fuel


def main():
    day = 1
    inp = advent.get_input(2019, day)
    advent.run(solve, inp)


if __name__ == '__main__':
    main()
