import advent


def main():
    data = advent.get_input(2020, 7).strip().splitlines()
    bag_rules = {}
    for bag in data:
        bag_color, contents = bag.split(' bags contain ')
        d = {}
        if contents.startswith('no'):
            bag_rules[bag_color] = d
            continue
        for part in contents.split(', '):
            n = int(part.split()[0])
            color = part.split(' ', 1)[1].rsplit(' ', 1)[0]
            d[color] = n
        bag_rules[bag_color] = d

    print(part_one(bag_rules))

    print(bag_count('shiny gold', bag_rules)-1)


def part_one(bag_rules):
    q = ['shiny gold']
    contained_by = set()
    while q:
        current = q.pop()
        for color, s in bag_rules.items():
            if current in s:
                contained_by.add(color)
                q.append(color)
    return len(contained_by)


def bag_count(color, rules):
    ans = 1
    for c, n in rules[color].items():
        ans += n*bag_count(c, rules)
    return ans


if __name__ == '__main__':
    main()
