from math import ceil, lcm

import advent


def main():
    data = advent.get_input(2020, 13).splitlines()

    print(part_one(data))

    print(part_two(data))


def parse(data):
    first_departure = int(data[0])
    buses = {}
    for i, x in enumerate(data[1].split(',')):
        if x.isnumeric():
            buses[i] = int(x)
    return first_departure, buses


def part_one(data):
    first_departure, buses = parse(data)
    departures = {}
    for id in buses.values():
        departures[id] = ceil(first_departure/id) * id

    bus = min(departures, key=departures.get)
    return bus*(departures[bus] - first_departure)


def part_two(data):
    _, buses = parse(data)
    l = list(buses.items())
    i, id = l[0]
    mult = id
    offset = (id-i) % mult
    for i, id in l[1:]:
        while offset % id != (id-i) % id:
            offset += mult
        mult = lcm(mult, id)
    return offset


if __name__ == '__main__':
    main()
