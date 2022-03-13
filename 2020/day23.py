from dataclasses import dataclass
from typing_extensions import Self
import advent


@dataclass
class Cup:
    id: int
    next: Self = None


def main():
    data = tuple(map(int, advent.get_input(2020, 23).strip()))
    part_two = True
    prev = None
    cups = {}
    for n in data:
        cups[n] = Cup(n)
        if prev is None:
            current = cups[n]
        else:
            prev.next = cups[n]
        prev = cups[n]
    if part_two:
        for n in range(10, 1_000_001):
            cups[n] = Cup(n)
            prev.next = cups[n]
            prev = cups[n]
    cups[n].next = current

    n_turns = 100
    if part_two:
        n_turns = 10_000_000

    for _ in range(n_turns):
        pick_up = current.next
        pick_up_end = pick_up.next.next
        current.next = pick_up_end.next

        pickup_vals = []
        n = pick_up
        for _ in range(3):
            pickup_vals.append(n.id)
            n = n.next
        dest_val = current.id - 1
        while dest_val < 1 or dest_val in pickup_vals:
            while dest_val in pickup_vals:
                dest_val -= 1
            if dest_val < 1:
                dest_val = max(cups)
        dest_cup = cups[dest_val]

        dest_cup.next, pick_up_end.next = pick_up, dest_cup.next

        current = current.next
        
    if not part_two:
        ans = ''
        n = cups[1]
        while True:
            n = n.next
            if n.id == 1:
                break
            ans += str(n.id)
        print(ans)
    else:
        ans = cups[1].next.id * cups[1].next.next.id
        print(ans)
        


if __name__ == '__main__':
    main()
