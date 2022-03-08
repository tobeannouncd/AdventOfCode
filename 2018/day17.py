from collections import defaultdict, deque
import advent

SAMPLE_DATA = '''x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504'''


def peek(position, direction, map):
    x, y = position

    if direction == 'left':
        new_position = x-1, y
    elif direction == 'right':
        new_position = x+1, y
    elif direction == 'up':
        new_position = x, y-1
    elif direction == 'down':
        new_position = x, y+1

    if new_position in map:
        return map[new_position]
    return '.'


def is_bordered(soil_map, pos):
    x, y = pos
    left_x = x
    while True:
        if soil_map[left_x-1, y] == '#':
            break
        left_x -= 1
        if soil_map[left_x, y+1] not in '#~':
            return False
    right_x = x
    while True:
        if soil_map[right_x+1, y] == '#':
            break
        right_x += 1
        if soil_map[right_x, y+1] not in '#~':
            return False
    return True


def simulate(data: str):
    soil_map = parse(data)
    ymin = min(y for x, y in soil_map if soil_map[x, y] == '#')
    ymax = max(y for x, y in soil_map if soil_map[x, y] == '#')

    pos = 500, 0
    soil_map[pos] = '|'

    q = []
    q.append(pos)
    while q:
        pos = q.pop()
        x, y = pos

        if soil_map[pos] == '|':
            if y == ymax:
                continue
            # down
            down = x, y+1
            down_val = soil_map[down]
            if down_val == '.':
                soil_map[down] = '|'
                q.append(down)
                continue
            if down_val == '|':
                continue
            # check if layer can fill
            if is_bordered(soil_map, pos):
                soil_map[pos] = '~'
                q.append(pos)
                continue
            # left
            left = x-1, y
            left_val = soil_map[left]
            if left_val == '.':
                soil_map[left] = "|"
                q.append(left)
            # right
            right = x+1, y
            right_val = soil_map[right]
            if right_val == '.':
                soil_map[right] = '|'
                q.append(right)
        elif soil_map[pos] == '~':
            # left
            left = x-1, y
            if soil_map[left] in '|.':
                soil_map[left] = '~'
                q.append(left)
            # right
            right = x+1, y
            if soil_map[right] in '|.':
                soil_map[right] = '~'
                q.append(right)
            # up
            up = x, y-1
            if soil_map[up] == '|':
                q.append(up)

    ans = 0
    ans2 = 0
    for x, y in soil_map:
        if y not in range(ymin, ymax+1):
            continue
        if soil_map[x, y] in '|~':
            ans += 1
            if soil_map[x,y] == '~':
                ans2+=1
    
    with open('day17_output.txt', 'w') as o:
        o.write(soil_string(soil_map))
    print(ans)
    print(ans2)


def soil_string(soil_map):
    xmin = min(x for x, y in soil_map if soil_map[x, y] in '#|~')
    xmax = max(x for x, y in soil_map if soil_map[x, y] in '#|~')
    ymin = min(y for x, y in soil_map if soil_map[x, y] == '#')
    ymax = max(y for x, y in soil_map if soil_map[x, y] == '#')

    out = []
    for y in range(ymin, ymax+1):
        line = ''
        for x in range(xmin, xmax+1):
            line += soil_map[x, y]
        out.append(line)
    return '\n'.join(out)


def parse(data: str):
    soil_map = defaultdict(lambda: '.')
    for line in data.splitlines():
        parts = line.split(', ')
        d = {}
        for part in parts:
            xy, rng = part.split('=')
            if '..' in rng:
                beg, end = map(int, rng.split('..'))
            else:
                beg = end = int(rng)
            d[xy] = range(beg, end+1)
        for x in d['x']:
            for y in d['y']:
                soil_map[x, y] = '#'
    return soil_map


def main():
    data = advent.get_input(2018, 17)
    # data = SAMPLE_DATA
    simulate(data)


if __name__ == '__main__':
    main()
