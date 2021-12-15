from advent import *

leftBrackets = '([{<'
rightBrackets = ')]}>'
scores1 = {')': 3, ']': 57, '}': 1197, '>': 25137}

filename = './input/day10.txt'


def part1():
    badChars = []
    for line in getData(filename):
        q = []
        for char in line.strip():
            if char in leftBrackets:
                q.append(char)
            else:
                try:
                    char2 = q.pop()
                except IndexError:
                    badChars.append(char)
                    break
                if leftBrackets.index(char2) != rightBrackets.index(char):
                    badChars.append(char)
                    break
    return sum(map(lambda x: scores1[x], badChars))


def score2(strList):
    scores = []
    nscores = 0
    for st in strList:
        s = 0
        for ch in st:
            s = 5*s + ' ([{<'.index(ch)
        nscores += 1
        scores.append(s)
    return sorted(scores)[nscores//2]


def part2():
    compStrings = []
    for line in getData(filename):
        q = []
        isIncomplete = True
        for char in line.strip():
            if char in leftBrackets:
                q.append(char)
            elif len(q) == 0:
                isIncomplete = False
                break
            else:
                char2 = q.pop()
                if leftBrackets.index(char2) != rightBrackets.index(char):
                    isIncomplete = False
                    break
        if isIncomplete:
            compStrings.append(''.join(q[::-1]))

    return score2(compStrings)


if __name__ == '__main__':
    # print(part1())
    print(part2())
