import itertools
import advent


class Crypto:
    def __init__(self, loop_size: int) -> None:
        self.loop_size = loop_size
        self.public_key = self.transform(7)

    def transform(self, n):
        return pow(n, self.loop_size, 20201227)


def main():
    data = advent.get_input(2020, 25).strip()
    public_card, public_door = map(int, data.splitlines())

    for loop_size in itertools.count(1):
        a = Crypto(loop_size)
        if a.public_key in (public_card, public_door):
            break
    if a.public_key == public_card:
        print(a.transform(public_door))
    else:
        print(a.transform(public_card))


if __name__ == '__main__':
    main()
