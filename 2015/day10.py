import advent
from itertools import groupby


def lookandsay(n: str):
    return ''.join(str(len(list(g))) + k for k, g in groupby(n))


def main():
    n = advent.get_input(2015, 10)
    for _ in range(40):
        n = lookandsay(n)
    print(len(n))
    for _ in range(10):
        n = lookandsay(n)
    print(len(n))

if __name__ == '__main__':
    main()
