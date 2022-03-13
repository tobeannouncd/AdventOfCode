import advent


def main():
    data = tuple(map(int, advent.get_input(2020, 10).strip().splitlines()))

    print(part_one(data))

    print(part_two(data))


def part_two(data):
    ways = [0]*(max(data)+4)
    ways[1:4] = 1, 1, 1
    for n in sorted(data):
        for i in range(n+1, n+4):
            ways[i] += ways[n]
    return ways[-1]


def part_one(data):
    s = sorted(data)
    s = [0] + s + [s[-1]+3]
    one_jolt, three_jolt = 0, 0
    for a, b in zip(s, s[1:]):
        if b-a == 1:
            one_jolt += 1
        elif b-a == 3:
            three_jolt += 1
    return one_jolt*three_jolt


if __name__ == '__main__':
    main()
