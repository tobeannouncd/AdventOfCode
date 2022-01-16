import advent
import re


def string_increment(s: str) -> str:
    if s[-1] == 'z':
        return string_increment(s[:-1]) + 'a'
    return s[:-1] + chr(1+ord(s[-1]))

def is_valid(s: str) -> bool:
    if any(ch in s for ch in 'iol'):
        return False
    if len(set(re.findall(r'(\w)\1',s))) < 2:
        return False
    flag_a = False
    for a,b,c in zip(s,s[1:],s[2:]):
        aa,bb,cc = map(ord,(a,b,c))
        if bb-aa == 1 and cc-bb==1:
            flag_a = True
            break
    if not flag_a:
        return False
    return True

    


def main():
    inp = advent.get_input(2015, 11)
    inp_a = inp
    while not is_valid(inp_a):
        inp_a = string_increment(inp_a)
    print(inp_a)
    inp_a = string_increment(inp_a)
    while not is_valid(inp_a):
        inp_a = string_increment(inp_a)
    print(inp_a)


if __name__ == '__main__':
    main()
