import advent


class Tunnel:
    def __init__(self, lst: list, rule_map: dict) -> None:
        self.lst = lst
        self.map = rule_map
        self.i_zero = 0

    def evolve(self):
        pass

    def encode(self):
        pass

    @staticmethod
    def decode():
        pass


def bitfield(n: int) -> list[int]:
    '''Turn an integer into a list of bits starting with the least significant bit

    >>> bitfield(2)
    [0, 1]
    >>> bitfield(26)
    [0, 1, 0, 1, 1]
    '''
    lst = []
    while n:
        lst.append(n % 2)
        n >>= 1
    return lst


def fieldbit(lst: list[int]) -> int:
    '''Convert a list of bits (least significant first) to its corresponding integer value

    >>> fieldbit([0, 1])
    2
    >>> fieldbit([0, 1, 0, 1, 1])
    26
    '''
    n = 0
    while lst:
        n = (n << 1)+lst.pop()
    return n


def parse_input(inp: str) -> tuple[int, dict]:
    a = inp.splitlines()[0].split(': ')[1]
    tr = str.maketrans('#.', '10')
    a_bin = int(a.translate(tr)[::-1], 2)
    d = {}
    for line in inp.splitlines()[2:]:
        l, r = line.split(' => ')
        ll = int(l.translate(tr)[::-1], 2)
        rr = int(r == '#')
        d[ll] = rr
    return a_bin, d


def main():
    inp = advent.get_input(2018, 12)
    init_state, rules = parse_input(inp)
    
    print('stuff')
    

    pass


def _test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    # _test()
    main()
