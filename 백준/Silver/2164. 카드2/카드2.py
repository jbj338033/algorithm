import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
q=deque(range(1,n+1))
while len(q)>1:
    q.popleft()
    q.append(q.popleft())
print(q[0])