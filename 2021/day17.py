_filename = 'input/day17.txt'


def proberange(vx, vy, xr, yr):
    pos = [0, 0]
    while pos[0] <= xr[1] and pos[1] >= yr[0]:
        yield(pos)
        pos[0] += vx
        vx = max(0, vx-1)
        pos[1] += vy
        vy -= 1


def inrange(pos, xr, yr):
    return (pos[0] in range(xr[0], 1+xr[1]) and pos[1] in range(yr[0], yr[1]+1))


with open(_filename) as f:
    data = f.read().strip().split('\n')

_, a, b = data[0].split('=')
xr = tuple(map(int, a.split(',')[0].split('..')))
yr = tuple(map(int, b.split('..')))


vy_max = max(-yr[0]-1, yr[1])
print(vy_max*(vy_max+1)//2)
vy_min = yr[0]
vx_min = min(1, xr[0])
vx_max = xr[1]
n_vel = 0
for vy in range(vy_min, vy_max+1):
    for vx in range(vx_min, vx_max+1):
        if any(inrange(pos, xr, yr) for pos in proberange(vx, vy, xr, yr)):
            n_vel += 1

print(n_vel)
