import advent


class Scanner:
    def __init__(self, s: str) -> None:
        self.stream = s
        self.pos = 0
        self.in_garbage = False
        self.scores = [0]
        self.score_tot = 0
        self.garbage_len = 0

        self.length = len(self.stream)

    def run(self):
        while self.pos < self.length:
            self.step()

    def step(self):
        r = self.stream[self.pos]
        if self.in_garbage and r not in '!>':
            self.garbage_len += 1
        if r == '{' and not self.in_garbage:
            parent_score = self.scores[-1]
            cur_score = parent_score+1
            self.scores.append(cur_score)
            self.score_tot += cur_score
        elif r == '<':
            self.in_garbage = True
        elif r == '!' and self.in_garbage:
            self.pos += 2
            return
        elif r == '>':
            self.in_garbage = False
        elif r == '}' and not self.in_garbage:
            self.scores.pop()
        self.pos += 1


def main(debug=False):
    stream = advent.get_input(2017, 9)
    score, garbage_len = solve(stream, debug)
    print(f'Part 1: {score}')
    print(f'Part 2: {garbage_len}')


def solve(txt: str, debug: bool):
    s = Scanner(txt)
    s.run()
    return s.score_tot, s.garbage_len


if __name__ == '__main__':
    main()
