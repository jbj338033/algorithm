import sys
input=lambda:sys.stdin.readline().rstrip()
n,m=map(int,input().split())
l=set([input() for _ in range(n)])
r=set([input() for _ in range(m)])
i=l & r
print(len(i))
print(*sorted(i),sep='\n')