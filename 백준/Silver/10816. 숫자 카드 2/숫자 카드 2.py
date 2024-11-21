import sys
input=sys.stdin.readline
input()
d={}
for i in input().split():
    d[i] = d.get(i, 0)+1
input()
r=[]
for i in input().split():
    r.append(d.get(i, 0))
print(*r)