from collections import deque

import advent


def main():
    data = tuple(map(int, advent.get_input(2020, 9).strip().splitlines()))
    preamble = deque(data[:25], 25)
    for n in data[26:]:
        if can_sum(n, preamble):
            preamble.append(n)
        else:
            first_invalid = n
            break
    print(first_invalid)

    contig = deque()
    data_iter = iter(data)
    while sum(contig) != first_invalid:
        if sum(contig) < first_invalid:
            contig.append(next(data_iter))
        else:
            contig.popleft()
    print(min(contig) + max(contig))


def can_sum(s, nums):
    for i, a in enumerate(nums):
        b = s-a
        if b in list(nums)[i+1:]:
            return True
    return False


if __name__ == '__main__':
    main()
