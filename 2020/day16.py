import advent


def main():
    data = advent.get_input(2020, 16)

    rules, nearby_tickets, my_ticket = parse(data)

    valid, part_one = valid_tickets(rules, nearby_tickets)
    print(part_one)

    labeled_ticket, part_two = label_ticket(rules, my_ticket, valid)
    print(part_two)


def parse(data):
    rules_text, ticket_text, nearby_text = data.strip().split('\n\n')
    rules = {}
    for rule in rules_text.splitlines():
        category = rule.split(': ')[0]
        ranges_text = rule.split(': ')[1].split(' or ')
        rng = set()
        for group in ranges_text:
            start, stop = map(int, group.split('-'))
            rng.update(range(start, stop+1))
        rules[category] = rng

    nearby_tickets = [[int(n) for n in line.split(',')]
                      for line in nearby_text.splitlines()[1:]]

    my_ticket = [int(n) for n in ticket_text.splitlines()[1].split(',')]
    return rules, nearby_tickets, my_ticket


def valid_tickets(rules, nearby_tickets):
    valid_tickets = []

    error_rate = 0
    for ticket in nearby_tickets:
        invalid_values = []
        for value in ticket:
            if not any(value in rng for rng in rules.values()):
                invalid_values.append(value)
        if invalid_values:
            error_rate += sum(invalid_values)
        else:
            valid_tickets.append(ticket)
    return valid_tickets, error_rate


def label_ticket(rules, ticket, valid_tickets):
    possibilities = []
    for n in valid_tickets[0]:
        possibilities.append(possible_categories(rules, n))
    for ticket in valid_tickets[1:]:
        for p, n in zip(possibilities, ticket):
            p &= possible_categories(rules, n)
    while any(len(p) > 1 for p in possibilities):
        for i, p in enumerate(possibilities):
            if len(p) == 1:
                x = list(p)[0]
                for j, q in enumerate(possibilities):
                    if i != j:
                        q.discard(x)
    for i, p in enumerate(possibilities):
        possibilities[i] = p.pop()

    departure_product = 1
    my_ticket_dict = {}
    for category, n in zip(possibilities, ticket):
        my_ticket_dict[category] = n
        if category.startswith('departure'):
            departure_product *= n

    return my_ticket_dict, departure_product


def possible_categories(rules, n):
    s = set()
    for category, rng in rules.items():
        if n in rng:
            s.add(category)
    return s


if __name__ == '__main__':
    main()
