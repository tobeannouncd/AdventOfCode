from collections import defaultdict
from itertools import product
import advent


def main():
    square_id = int(advent.get_input(2017, 3))
    part_one(square_id)
    part_two(square_id)


def part_one(square_id):
    i = 1
    perim = 0
    down = 0
    right = 0
    side_len = 1
    while i < square_id:
        perim += 8
        i += perim
        down += 1
        right += 1
        side_len += 2
    # print(i, perim)
    # print(i - square_id)
    side1 = side_len-1
    side2 = side1
    side3 = side2
    side4 = side3-1
    while i > square_id:
        i -= 1
        if side1:
            side1 -= 1
            right -= 1
        elif side2:
            side2 -= 1
            down -= 1
        elif side3:
            side3 -= 1
            right += 1
        elif side4:
            side4 -= 1
            down += 1
    print(abs(down)+abs(right))


def neighbor_vals(pt, spiral):
    for p in product(range(-1, 2), repeat=2):
        if all(pp == 0 for pp in p):
            continue
        yield spiral[tuple(a+da for a, da in zip(pt, p))]


def part_two(tgt):
    spiral = defaultdict(int)
    x, y = 0, 0
    val = 1
    dx, dy = 1, 0
    direction_steps = 1
    steps_made = 0
    while val < tgt:
        spiral[(x, y)] = val
        x, y = x+dx, y+dy
        steps_made += 1
        if steps_made == direction_steps:
            # rotate ccw
            dx, dy = -dy, dx
            steps_made = 0
        # if left or right, increment direction_steps
            if dy == 0:
                direction_steps += 1
        val = sum(neighbor_vals((x, y), spiral))
    print(val)


if __name__ == '__main__':
    main()
