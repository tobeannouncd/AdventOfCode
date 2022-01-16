def main():
    fn = 'input/day2.txt'
    with open(fn) as f:
        box_dims = f.read().strip().split('\n')
    tot_paper = 0
    tot_ribbon = 0
    for box in box_dims:
        l,w,h = sorted(map(int,box.split('x')))
        tot_paper += 2*(l*w+l*h+w*h) + l*w
        tot_ribbon += 2*(l+w)+l*w*h
    print(tot_paper)
    print(tot_ribbon)


if __name__ == '__main__':
    main()
