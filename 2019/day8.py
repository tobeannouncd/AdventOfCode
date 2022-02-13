from collections import Counter

import advent


def solve(inp: str, width: int, height: int):
    layers = []
    i = 0
    layer_len = width*height
    while i < len(inp):
        layers.append(inp[i:i+layer_len])
        i += layer_len
    # counters = []
    min_zero = None, None
    for layer in layers:
        c = Counter(layer)
        if min_zero[0] is None or min_zero[0] > c['0']:
            min_zero = c['0'], c
    _, c = min_zero
    yield c['1']*c['2']
    img = [None]*layer_len
    for layer in layers:
        for i, (ch, pixel) in enumerate(zip(layer, img)):
            if pixel is not None or ch == '2':
                continue
            img[i] = ch
    fn = './output/day8.png'
    render(fn, img, width, height)
    yield fn


def render(fn: str, img: list[str], width: int, height: int):
    pixels = []
    for i, ch in enumerate(img):
        if ch == '0':
            continue
        x, y = i % width, i//width
        pixels.append((x, y))

    advent.print_img(fn, pixels, width, height)


def main():
    inp = advent.get_input(2019, 8)
    width = 25
    height = 6
    advent.run(solve, inp, width, height)


if __name__ == '__main__':
    main()
