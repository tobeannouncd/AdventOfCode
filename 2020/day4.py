import re

import advent

RULES = {
    'byr': r'19[2-9]\d|200[0-2]',
    'iyr': r'201\d|2020',
    'eyr': r'202\d|2030',
    'hgt': r'1[5-8]\dcm|19[0-3]cm|59in|6\din|7[0-6]in',
    'hcl': r'#[0-9a-f]{6}',
    'ecl': r'amb|blu|brn|gry|grn|hzl|oth',
    'pid': r'\d{9}'
}


def main():
    data = advent.get_input(2020, 4).strip().split('\n\n')

    valid_passports = part_one(data)
    print(len(valid_passports))

    more_valid = part_two(valid_passports)
    print(len(more_valid))


def part_two(valid_passports):
    more_valid = []
    for p in valid_passports:
        if all(re.fullmatch(v, p[k]) for k, v in RULES.items()):
            more_valid.append(p)
    return more_valid


def part_one(data):
    passports = []
    for p in data:
        d = {}
        for itm in p.split():
            k, v = itm.split(':')
            d[k] = v
        passports.append(d)

    valid_passports = []
    for p in passports:
        if all(f in p for f in RULES):
            valid_passports.append(p)
    return valid_passports


if __name__ == '__main__':
    main()
