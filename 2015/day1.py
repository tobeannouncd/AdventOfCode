from collections import Counter

def main():
    # Part 1
    fn = 'input/day1.txt'
    with open(fn) as f:
        in_string = f.read().strip()
    c_char = Counter(in_string)
    print(c_char['(']-c_char[')'])

    # Part 2
    pos = 0
    for i,char in enumerate(in_string, start=1):
        pos += {'(':1,')':-1}[char]
        if pos == -1:
            print(i)
            break
    

if __name__ == '__main__':
    main()
