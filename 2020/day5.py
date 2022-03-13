import advent


def main():
    data = advent.get_input(2020, 5).strip().splitlines()

    seats = get_seat_ids(data)
    print(max(seats))

    s = sorted(seats)
    for a, b in zip(s, s[1:]):
        if b-a == 2:
            print(a+1)
            break


def get_seat_ids(data):
    seats = []
    seat_map = str.maketrans('FBLR', '0101')
    for line in data:
        seats.append(int(line.translate(seat_map), 2))
    return seats


if __name__ == '__main__':
    main()
