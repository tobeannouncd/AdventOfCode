import re
import advent

HEX_PAT = re.compile(r'\\x[a-f0-9]{2}')


def parse_string(s: str) -> str:
    s = s[1:-1].replace('\\\\', '\\').replace('\\"', '"')
    hex_list = HEX_PAT.findall(s)
    for h in hex_list:
        s = s.replace(h, chr(int(h[-2:], 16)))
    return s


def encode_string(s: str) -> str:
    s=s.replace('\\','\\\\').replace('"','\\"')
    return f'"{s}"'


def main():
    t = advent.get_input(2015, 8).split('\n')
    print('Part 1:', sum(len(line) - len(parse_string(line)) for line in t))
    print('Part 2:', sum(len(encode_string(line)) - len(line) for line in t))


if __name__ == '__main__':
    main()
