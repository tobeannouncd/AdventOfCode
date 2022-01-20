from itertools import permutations

import advent


def main():
    ss = [list(map(int, line.split()))
          for line in advent.get_input(2017, 2).splitlines()]
    print(sum(max(line) - min(line) for line in ss))
    sum2 = 0
    for line in ss:
        for a, b in permutations(line, 2):
            if a % b:
                continue
            sum2 += a//b
            break
    print(sum2)


if __name__ == '__main__':
    main()
