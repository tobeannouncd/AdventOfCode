from xml.dom import minidom
import advent
from collections import defaultdict
from itertools import permutations



def main():
    inp = advent.get_input(2015, 9)
    routes = inp.splitlines()
    d = defaultdict(dict)
    for route in routes:
        loc_a,_,loc_b,_,dist = route.split()
        d[loc_a][loc_b] = int(dist)
        d[loc_b][loc_a] = int(dist)
    min_dist = None
    max_dist = None
    for p in permutations(d):
        tot_dist = 0
        for orig,dest in zip(p,p[1:]):
            tot_dist += d[orig][dest]
        if min_dist is None or tot_dist < min_dist[0]:
            min_dist = tot_dist, p
        if max_dist is None or tot_dist > max_dist[0]:
            max_dist = tot_dist, p
    print('Part 1:', min_dist)
    print('Part 2:', max_dist)
    

if __name__ == '__main__':
    main()
