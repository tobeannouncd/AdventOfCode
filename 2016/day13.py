import advent


def is_wall(x, y, fav_num):
    '''
    >>> is_wall(0,0,10)
    False
    >>> is_wall(5,4,10)
    True
    '''
    a = x*x + 3*x + 2*x*y + y + y*y
    a += fav_num
    b = bin(a)[2:]
    return bool(b.count('1') % 2)


def main():
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
