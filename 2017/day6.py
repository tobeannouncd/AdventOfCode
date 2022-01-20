import advent


def main(debug=False):
    block_counts = tuple(map(int, advent.get_input(2017, 6).split()))

    part_one(block_counts)
    part_two(block_counts)


def part_one(block_counts):
    configs = set()
    new_config = block_counts
    configs.add(new_config)
    while True:
        new_config = cycle(new_config)
        if new_config in configs:
            break
        configs.add(new_config)
    print(len(configs))


def part_two(block_counts):
    configs = list()
    new_config = block_counts
    configs.append(new_config)
    while True:
        new_config = cycle(new_config)
        if new_config in configs:
            break
        configs.append(new_config)
    print(len(configs)-configs.index(new_config))


def cycle(blocks: tuple):
    v = max(blocks)
    i = blocks.index(v)
    return redistribute(blocks, i)


def redistribute(blocks: tuple, i: int):
    l, ln = list(blocks), len(blocks)
    v, l[i] = l[i], 0
    while v:
        i = (i+1) % ln
        l[i] += 1
        v -= 1
    return tuple(l)


if __name__ == '__main__':
    main()
