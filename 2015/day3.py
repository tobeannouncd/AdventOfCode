def main():
    fn = 'input/day3.txt'
    with open(fn) as f:
        in_file = f.read().strip()
    pos = 0+0j
    visited = set()
    visited.add(pos)
    d_dir = {'^': 1j, 'v': -1j, '<': -1, '>': 1}
    for ch in in_file:
        pos += d_dir[ch]
        visited.add(pos)
    print(len(visited))
    pos_a, pos_b = 0, 0
    vis = set()
    vis.add(pos_a)
    for i, ch in enumerate(in_file):
        if i % 2 == 0:
            pos_a += d_dir[ch]
            vis.add(pos_a)
            continue
        if i % 2 == 1:
            pos_b += d_dir[ch]
            vis.add(pos_b)
            continue
    print(len(vis))


if __name__ == '__main__':
    main()
