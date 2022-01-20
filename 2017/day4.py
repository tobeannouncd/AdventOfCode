from collections import Counter
from itertools import combinations
import advent


def are_anagrams(word1, word2):
    c1 = Counter(word1)
    c2 = Counter(word2)
    if (not c1-c2) and (not c2-c1):
        return True
    return False


def main():
    phrase_list = advent.get_input(2017, 4).splitlines()
    print(f'Part 1: {part_one(phrase_list)}')
    cnt = 0
    for phrase in phrase_list:
        word_list = phrase.split()
        if any(are_anagrams(a,b) for a,b in combinations(word_list,2)):
            continue
        cnt += 1
    print(f'Part 2: {cnt}')


def part_one(phrase_list):
    cnt = 0
    for phrase in phrase_list:
        word_list = phrase.split()
        word_set = set(word_list)
        if len(word_list) == len(word_set):
            cnt += 1
    return cnt


if __name__ == '__main__':
    main()
