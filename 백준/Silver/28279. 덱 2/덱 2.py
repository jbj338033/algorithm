import sys
from collections import deque
input=sys.stdin.readline
q=deque()
for _ in range(int(input())):
    l=list(map(int,input().split()))
    c=l[0]
    if c==1:
        q.appendleft(l[1])
    elif c==2:
        q.append(l[1])
    elif c==3:
        print(q.popleft() if q else -1)
    elif c==4:
        print(q.pop() if q else -1)
    elif c==5:
        print(len(q))
    elif c==6:
        print(0 if q else 1)
    elif c==7:
        print(q[0] if q else -1)
    elif c==8:
        print(q[-1] if q else -1)