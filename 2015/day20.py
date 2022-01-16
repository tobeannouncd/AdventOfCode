from math import sqrt
import advent


def sum_factors(n: int, limit=None) -> int:
    factors = set()
    for x in range(1, int(sqrt(n))+1):
        if n % x == 0:
            factors.add(x)
            factors.add(n//x)
    if limit is None:
        return sum(factors)
    return sum(f for f in factors if f*limit >= n)


def main():
    min_presents = int(advent.get_input(2015, 20))
    n = 1
    while 10*sum_factors(n) < min_presents:
        n += 1
    print(n)
    n = 1
    while 11*sum_factors(n,50) < min_presents:
        n += 1
    print(n)

if __name__ == '__main__':
    main()
