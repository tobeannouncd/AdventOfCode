from collections import deque
import advent


class Deck:
    def __init__(self, cards) -> None:
        self.cards = deque(cards)


def main():
    data = advent.get_input(2020, 22).strip()
    decks = []
    for deck in data.split('\n\n'):
        decks.append(deque(map(int, deck.split('\n', 1)[1].splitlines())))
    player_one = decks[0].copy()
    player_two = decks[1].copy()

    ans = part_one(player_one, player_two)
    print(ans)

    player_one = decks[0].copy()
    player_two = decks[1].copy()
    winner = game(player_one, player_two)
    if winner == 1:
        print(score_hand(player_one))
    elif winner == 2:
        print(score_hand(player_two))


def game(deck_one: deque, deck_two: deque):
    history = set()
    while deck_one and deck_two:
        if (tuple(deck_one), tuple(deck_two)) in history:
            return 1
        history.add((tuple(deck_one), tuple(deck_two)))
        a, b = deck_one.popleft(), deck_two.popleft()
        if a <= len(deck_one) and b <= len(deck_two):
            winner = game(deque(list(deck_one)[:a]), deque(list(deck_two)[:b]))
        elif a > b:
            winner = 1
        else:
            winner = 2
        if winner == 1:
            deck_one.extend((a, b))
        elif winner == 2:
            deck_two.extend((b, a))
    if deck_one:
        return 1
    elif deck_two:
        return 2


def part_one(player_one, player_two):
    while player_one and player_two:
        a, b = player_one.popleft(), player_two.popleft()
        if a > b:
            player_one.extend((a, b))
        else:
            player_two.extend((b, a))
    return score(player_one, player_two)


def score(player_one, player_two):
    if player_one:
        winner = player_one
    else:
        winner = player_two

    return score_hand(winner)


def score_hand(winning_hand):
    ans = 0
    for i, card in enumerate(reversed(winning_hand), start=1):
        ans += i*card
    return ans


if __name__ == '__main__':
    main()
