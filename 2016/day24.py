from collections import defaultdict
from itertools import combinations, permutations
from operator import itemgetter
import sys
import advent


def parse(input_text: str) -> tuple[tuple[int, int], dict, set]:
    walls = set()
    targets = {}
    start = None
    for i, line in enumerate(input_text.splitlines()):
        for j, char in enumerate(line):
            if char == '.':
                continue
            elif char == '#':
                walls.add((j, i))
            elif char in '123456789':
                targets[int(char)] = (j, i)
            elif char == '0':
                start = j, i
    return start, targets, walls


def neighbors(point, walls):
    x, y = point
    for i, j in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        neighbor = x+i, y+j
        if neighbor not in walls:
            yield neighbor


def shortest_path(start, finish, walls):
    seen = set()
    prev = {}
    dist = defaultdict(lambda: sys.maxsize)
    dist[start] = 0

    while finish not in seen:
        l = (k for k in dist if k not in seen)
        cur = min(l, key=dist.get)
        seen.add(cur)
        for neighbor in neighbors(cur, walls):
            if 1 + dist[cur] < dist[neighbor]:
                dist[neighbor] = 1 + dist[cur]
                prev[neighbor] = cur

    path = [finish]
    while path[-1] in prev:
        path.append(prev[path[-1]])

    return path


def main():
    input_text = advent.get_input(2016, 24)
    start, targets, walls = parse(input_text)
    # for target in targets.values():
    #     print(f'{start} -> {target}: {len(shortest_path(start, target, walls))}')
    best_path, best_dist = find_best_path(start, targets, walls)
    print(f'{best_dist}: {best_path}')
    best_path, best_dist = find_best_path(start, targets, walls, part=2)
    print(f'{best_dist}: {best_path}')


def find_best_path(start, targets, walls, *, part=1):
    paths_betw_targets = {}
    for pair in combinations(targets.items(), 2):
        a, b = pair
        sorted_ab = tuple(sorted((a[0], b[0])))
        # print(f'{a[0]} <-> {b[0]}: {len(shortest_path(a[1], b[1], walls))}')
        dist = len(shortest_path(a[1], b[1], walls))
        paths_betw_targets[sorted_ab] = dist
    best_order, best_dist = None, sys.maxsize
    start_paths = {target: len(shortest_path(start, point, walls))
                   for target, point in targets.items()}
    for p in permutations(targets):
        dist = 0
        for i in range(len(p)-1):
            a, b = sorted(p[i:i+2])
            dist += paths_betw_targets[a, b] - 1
        dist += start_paths[p[0]] - 1
        if part == 2:
            dist += start_paths[p[-1]] - 1
        if dist < best_dist:
            best_order = [0] + list(p)
            if part == 2:
                best_order.append(0)
            best_dist = dist
    return best_order, best_dist


if __name__ == '__main__':
    main()
