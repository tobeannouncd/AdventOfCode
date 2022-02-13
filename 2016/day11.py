'''
credit for this implementation goes to https://eddmann.com/posts/advent-of-code-2016-day-11-radioisotope-thermoelectric-generators/
'''

from collections import Counter, deque
import re
from itertools import chain, combinations

import advent


def parse_input(state: str) -> list:
    return [set(re.findall(r'(\w+)(?:-compatible)? (microchip|generator)', line)) for line in state.splitlines()]


def is_valid_floor(floor):
    return len(set(typ for _, typ in floor)) < 2 or \
        all((obj, 'generator') in floor for (
            obj, typ) in floor if typ == 'microchip')


def next_states(state: tuple[int, int, list[set]]):
    moves, elevator, floors = state

    possible_moves = chain(combinations(
        floors[elevator], 2), combinations(floors[elevator], 1))

    for move in possible_moves:
        for direction in [-1, 1]:
            next_elevator = elevator + direction
            if next_elevator not in range(len(floors)):
                continue

            next_floors = floors.copy()
            next_floors[elevator] = next_floors[elevator].difference(move)
            next_floors[next_elevator] = next_floors[next_elevator].union(move)

            if is_valid_floor(next_floors[elevator]) and is_valid_floor(next_floors[next_elevator]):
                yield moves+1, next_elevator, next_floors


def is_all_top_level(floors):
    return all(not floor
               for number, floor in enumerate(floors)
               if number < len(floors) - 1)


def count_floor_objects(state):
    _, elevator, floors = state
    return elevator, tuple(tuple(Counter(typ for _, typ in floor).most_common()) for floor in floors)


def min_to_top(floors):
    seen = set()
    q = deque([(0, 0, floors)])

    while q:
        state = q.popleft()
        moves, _, floors = state

        if is_all_top_level(floors):
            return moves

        for next_state in next_states(state):
            if (key := count_floor_objects(next_state)) not in seen:
                seen.add(key)
                q.append(next_state)


def main():
    starting_state = advent.get_input(2016, 11)
    board = parse_input(starting_state)
    print(min_to_top(board))
    extra_items = {('elerium','generator'),('elerium','microchip'),('dilithium','generator'),('dilithium','microchip')}
    board[0] |= extra_items
    print(min_to_top(board))

if __name__ == '__main__':
    main()
