import sys
input=sys.stdin.readline
input()
d={}
for i in input().split():
    d[i]=1
input()
for i in input().split():
    print(d.get(i,0),end=' ')