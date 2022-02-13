from collections import Counter
import advent
from intcode import Intcode


def solve(inp: str):
    program = tuple(map(int, inp.split(',')))
    arcade = Intcode(program)
    arcade.run()
    screen = draw(arcade.outputs)
    c = Counter(screen.values())
    yield c[2]
    arcade = Intcode(program)
    game_mode = 2 # 1: quarters, 2: free play
    screen = play_game(arcade, game_mode)
    for pt, val in screen.items():
        if pt[0]==-1:
            yield val
            break

def play_game(arcade, game_mode):
    arcade[0] = game_mode
    arcade.run()
    while True:
        screen = draw(arcade.outputs)
        c=Counter(screen.values())
        if c[2] == 0:
            break
        # render(screen)
        # joystick = int(input('Left (-1), Stay (0), or Right (1):'))
        ball_x, paddle_x = None, None
        for pos, val in screen.items():
            if val == 4:
                ball_x = pos[0]
            elif val == 3:
                paddle_x = pos[0]
            if ball_x is not None and paddle_x is not None:
                break
        joystick = 0
        if ball_x<paddle_x:
            joystick = -1
        elif ball_x>paddle_x:
            joystick = 1
        # input()
        arcade.run(joystick)
    return screen


def render(screen: dict[tuple[int, int], int]):
    points = {}
    score = None
    for pt, val in screen.items():
        x, _ = pt
        if x == -1:
            score = val
        elif x >= 0:
            if val == 0:
                continue
            elif val == 1:
                points[pt] = '#'
            elif val == 2:
                points[pt] = 'O'
            elif val == 3:
                points[pt] = 'T'
            elif val == 4:
                points[pt] = '*'
    print(f'Score: {score}')
    # find screen dimensions
    xmax = max(points, key=lambda x: x[0])[0]
    ymax = max(points, key=lambda x: x[1])[1]
    grid = [[' ']*(xmax+1) for _ in range(ymax+1)]
    for (x, y), val in points.items():
        grid[y][x] = val
    for line in grid:
        print(''.join(line))


def draw(instructions: list[int]):
    stack = list(reversed(instructions))
    objects = {}
    while stack:
        xpos = stack.pop()
        ypos = stack.pop()
        tile_id = stack.pop()
        objects[(xpos, ypos)] = tile_id
    return objects


def main():
    inp = advent.get_input(2019, 13)
    advent.run(solve, inp)


if __name__ == '__main__':
    main()
