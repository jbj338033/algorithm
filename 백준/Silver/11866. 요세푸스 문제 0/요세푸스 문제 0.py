from collections import deque
n,k=map(int,input().split())
q=deque(map(str,range(1,n+1)))
o=[]
while q:
    q.rotate(-k+1)
    o.append(q.popleft())
print(f'<{", ".join(o)}>')