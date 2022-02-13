'''Collection of useful functions for solving Advent of Code problems.'''

import pickle
from collections.abc import Callable
from os.path import exists
from typing import Iterable
from PIL import Image

import requests

COOKIE_FILE = './input/cookie.pickle'
BASE_URL = 'https://adventofcode.com/'


def set_cookie():
    d = {}
    while True:
        k = input('key (enter -1 if done):')
        if k == '-1':
            break
        v = input('value:')
        d[k] = v
    with open(COOKIE_FILE, 'wb') as f:
        pickle.dump(d, f)


def read_cookie(file: str = COOKIE_FILE):
    with open(file, 'rb') as f:
        print(pickle.load(f))


def get_input(year: int, day: int, fname_only: bool = False) -> str:
    file_path = f'./input/day{day}.txt'
    if not exists(file_path):
        url = f'{BASE_URL}{year}/day/{day}/input'
        with open(COOKIE_FILE, 'rb') as f:
            r = requests.get(url, cookies=pickle.load(f))
        with open(file_path, 'w') as f:
            f.write(r.text.strip())
    if fname_only:
        return file_path
    with open(file_path) as f:
        data = f.read().strip()
    return data


def test(main_func: Callable[[str], Iterable], tests: dict[str, tuple[str, Iterable]]):
    header = 'Part,Result,Expected,Actual'.split(',')
    for name, (data, answers) in tests.items():
        results = []
        padding = '  '
        solution = main_func(data)
        justify = 'ljust,center,rjust,rjust'.split(',')
        for i, answer in enumerate(answers, start=1):
            val = next(solution)
            results.append((i,
                            {True: 'Pass', False: 'Fail'}[val == answer],
                            answer,
                            val))
        widths = 4, 6, *(max((len(header[i]),
                             *(len(str(result[i]))
                               for result in results)))
                         for i in (2, 3))
        title = f'Dataset: {name}'
        tot_width = max(sum(widths)+(len(widths)-1)*len(padding), len(title))
        print(title.center(tot_width, '='))
        print(padding.join((eval(f'"{a}".{j}({b})')
              for a, b, j in zip(header, widths, justify))))
        print(*(padding.join((eval(f'"{a}".{j}({b})')
                             for a, b, j in zip(result, widths, justify)))
                for result in results), sep='\n')


def run(func: Callable, *args):
    answers = func(*args)
    if answers is None:
        return
    if not isinstance(answers, Iterable):
        print(answers)
    for i, answer in enumerate(answers, start=1):
        print(f'Part {i}: {answer}')


def print_img(fname: str, pixels: Iterable[tuple[int, int]], width, height, scale=10):
    img = Image.new('1', (width, height))
    for pixel in pixels:
        img.putpixel(pixel, 1)
    img.resize((scale*width, scale*height)).save(fname)


def main():
    if not exists(COOKIE_FILE):
        set_cookie()
    read_cookie()
    pass


if __name__ == '__main__':
    main()
