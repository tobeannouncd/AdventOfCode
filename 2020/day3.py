import operator
from functools import reduce

import advent


def main():
    data = advent.get_input(2020, 3).strip()
    tree_map = [list(l) for l in data.splitlines()]
    down = 1
    right = 3
    part_one_ans = check_slope(tree_map, down, right)
    print(part_one_ans)

    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]
    trees = [check_slope(tree_map, d, r) for r, d in slopes]
    print(reduce(operator.mul, trees))


def check_slope(tree_map, down, right):
    j = 0
    cols = len(tree_map[0])
    ans = 0
    for i in range(0, len(tree_map), down):
        j = (i*right) % cols
        if tree_map[i][j] == '#':
            ans += 1
    return ans


if __name__ == '__main__':
    main()
