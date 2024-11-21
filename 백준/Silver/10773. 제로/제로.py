s=[]
for _ in range(int(input())):
    n=int(input())
    if n==0:s.pop()
    else:s.append(n)
print(sum(s))