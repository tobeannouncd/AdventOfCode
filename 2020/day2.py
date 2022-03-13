import re

import advent


def main():
    data = advent.get_input(2020, 2).strip().splitlines()
    pattern = r'(\d+)-(\d+) (.): (.+)'
    part_one = 0
    part_two = 0
    for line in data:
        low, hi, letter, pw = re.match(pattern, line).groups()
        if int(low) <= pw.count(letter) <= int(hi):
            part_one += 1
        if (pw[int(low)-1] == letter) ^ (pw[int(hi)-1] == letter):
            part_two += 1
    print(part_one)
    print(part_two)


if __name__ == '__main__':
    main()
