import hashlib

def get_hash_prefix(s:str, n:int):
    return hashlib.md5(s).hexdigest()[:n]


def main():
    fn = 'input/day4.txt'
    with open(fn) as f:
        secret_key = f.read().strip()
    num=0
    while int(get_hash_prefix((secret_key+str(num)).encode(), 5),16):
        num += 1
    print(num)
    while int(get_hash_prefix((secret_key+str(num)).encode(), 6),16):
        num += 1
    print(num)

if __name__ == '__main__':
    main()
