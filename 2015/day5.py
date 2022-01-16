from collections import Counter


def is_nice(st: str):
    c = Counter(st)
    c_vowels = sum(c[v] for v in 'aeiou')
    if c_vowels < 3:
        return False
    if all(a != b for a, b in zip(st, st[1:])):
        return False
    if any(ss in st for ss in ('ab','cd','pq','xy')):
        return False
    return True

def is_really_nice(st: str):
    if all(st.count(a+b) == 1 for a,b in zip(st, st[1:])):
        return False
    if all(a != c for a,b,c in zip(st,st[1:],st[2:])):
        return False
    return True

def main():
    fn = 'day5.txt'
    with open(fn) as f:
        data = f.read().strip().split('\n')
    print(sum(is_nice(s) for s in data))
    print(sum(is_really_nice(s) for s in data))


if __name__ == '__main__':
    main()
