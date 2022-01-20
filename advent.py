import pickle
import requests
from os.path import exists

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


def read_cookie():
    with open(COOKIE_FILE, 'rb') as f:
        print(pickle.load(f))


def get_input(year: int, day: int, ext: str = 'txt') -> str:
    file_path = f'./input/day{day}.{ext}'
    if exists(file_path):
        with open(file_path) as f:
            data = f.read().strip()
        return data
    else:
        url = f'{BASE_URL}{year}/day/{day}/input'
        with open(COOKIE_FILE, 'rb') as f:
            r = requests.get(url, cookies=pickle.load(f))
        with open(file_path, 'w') as f:
            f.write(r.text.strip())
        return r.text.strip()


def main():
    if not exists(COOKIE_FILE):
        set_cookie()
    read_cookie()
    # set_cookie()
    # read_cookie()
    pass


if __name__ == '__main__':
    main()
