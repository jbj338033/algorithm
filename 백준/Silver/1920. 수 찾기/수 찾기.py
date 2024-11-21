import sys
input=sys.stdin.readline
input()
l=set(input().split())
input()
for i in input().split():
    print(1 if i in l else 0)