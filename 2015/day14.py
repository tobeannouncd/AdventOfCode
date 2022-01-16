from collections import Counter
import advent
import re

RE_PAT = re.compile(
    r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+)')
RACE_TIME = 2503

class Reindeer:
    def __init__(self, in_str: str):
        g = RE_PAT.match(in_str).groups()
        self.name = g[0]
        self.speed, self.dur, self.rest = map(int, g[1:])
        self.pos = 0
        self.fly_time = 0
        self.rest_time = 0
        self.resting = False

    def __repr__(self) -> str:
        return f'{self.name}: {self.speed} km/s for {self.dur} sec, rest for {self.rest} sec'

    def race(self, time: int) -> int:
        for _ in range(time):
            self.step()
        return self.pos

    def step(self):
        if not self.resting:
            self.pos += self.speed
            self.fly_time += 1
            if self.fly_time == self.dur:
                self.resting = True
                self.rest_time = 0
            return
        if self.resting:
            self.rest_time += 1
            if self.rest_time == self.rest:
                self.resting = False
                self.fly_time = 0
            return


def main():
    inp = advent.get_input(2015, 14).splitlines()
    racers = set()
    racers_b = set()
    for line in inp:
        racers.add(Reindeer(line))
        racers_b.add(Reindeer(line))
    # print(*racers, sep='\n')
    print(max(racer.race(RACE_TIME) for racer in racers))

    scores = Counter()
    for _ in range(RACE_TIME):
        cur_pos = []
        for racer in racers_b:
            cur_pos.append(racer.race(1))
        top_pos = max(cur_pos)
        for racer in racers_b:
            if racer.pos == top_pos:
                scores[racer.name] += 1
    # d = {racer.name:racer.pos for racer in racers_b}
    print(scores.most_common(1))
    # print(d)


if __name__ == '__main__':
    main()
