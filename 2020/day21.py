import advent


def main():
    data = advent.get_input(2020, 21)
    lines = []
    for line in data.strip().splitlines():
        left, right = line.split('(contains ')
        ingredients = left.split()
        allergens = [l[:-1] for l in right.split()]
        lines.append((ingredients, allergens))

    allergen_dict, ans = part_one(lines)
    print(ans)

    a = part_two(allergen_dict)
    print(','.join(a))


def part_one(lines):
    allergens = set()
    ingredients = set()
    for i, a in lines:
        allergens.update(a)
        ingredients.update(i)
    allergen_dict = {}
    for i, a in lines:
        for allergen in a:
            if allergen not in allergen_dict:
                allergen_dict[allergen] = set(i)
            else:
                allergen_dict[allergen].intersection_update(i)
    not_allergens = set()
    for i in ingredients:
        if all(i not in s for s in allergen_dict.values()):
            not_allergens.add(i)
    ans = 0
    for i, _ in lines:
        for ing in i:
            if ing in not_allergens:
                ans += 1
    return allergen_dict, ans


def part_two(allergen_dict):
    while any(len(s) > 1 for s in allergen_dict.values()):
        for a, s in allergen_dict.items():
            if len(s) == 1:
                for aa, ss in allergen_dict.items():
                    if a != aa:
                        ss -= s
    a = [v.pop() for k, v in sorted(allergen_dict.items())]
    return a


if __name__ == '__main__':
    main()
