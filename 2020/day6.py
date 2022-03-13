from collections import Counter

import advent


def main():
    data = advent.get_input(2020, 6).strip().split('\n\n')
    part_one_ans = 0
    part_two_ans = 0
    for group in data:
        c = Counter()
        responses = group.splitlines()
        n_people = len(responses)
        for r in responses:
            c += Counter(r)
        part_one_ans += len(c)
        part_two_ans += len(set(k for k, v in c.items() if v == n_people))
    print(part_one_ans)
    print(part_two_ans)


if __name__ == '__main__':
    main()
