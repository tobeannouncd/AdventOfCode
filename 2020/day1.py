import advent


def main():
    data = list(map(int, advent.get_input(2020, 1).strip().splitlines()))
    part_one(data)
    part_two(data)


def part_two(data):
    for i, a in enumerate(data):
        for j, b in enumerate(data[i+1:], start=i+1):
            c = 2020 - a - b
            if c in data[j+1:]:
                print(a*b*c)
                break


def part_one(data):
    for i, a in enumerate(data):
        b = 2020 - a
        if b in data[i+1:]:
            print(a*b)
            break


if __name__ == '__main__':
    main()
