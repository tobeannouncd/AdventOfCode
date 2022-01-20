import advent

def main():
    input_str = advent.get_input(2017,1)
    q = []
    s1 = input_str
    s2 = s1*2
    for a,b in zip(s1,s2[1:]):
        if a==b:
            q.append(int(a))
    print(sum(q))
    l=len(s1)
    q=[]
    for a,b in zip(s1,s2[l//2:]):
        if a==b:
            q.append(int(a))
    print(sum(q))

if __name__ == '__main__':
    main()
