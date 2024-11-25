import sys
from collections import deque
input=sys.stdin.readline
q=deque()
for _ in range(int(input())):
    l=input().split()
    c=l[0]
    if c=='push':
        q.appendleft(l[1])
    elif c=='pop':
        print(q.pop() if q else -1)
    elif c=='size':
        print(len(q))
    elif c=='empty':
        print(0 if q else 1)
    elif c=='front':
        print(q[-1] if q else -1)
    elif c=='back':
        print(q[0] if q else -1)