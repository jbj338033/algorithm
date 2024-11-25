import sys
input=sys.stdin.readline
s=[]
for _ in range(int(input())):
    l=list(map(int,input().split()))
    c=l[0]
    if c==1:
        s.append(l[1])
    elif c==2:
        print(s.pop() if s else -1)
    elif c==3:
        print(len(s))
    elif c==4:
        print(0 if s else 1)
    elif c==5:
        print(s[-1] if s else -1)