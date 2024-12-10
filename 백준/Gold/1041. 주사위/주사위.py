n=int(input())
d=list(map(int,input().split()))
if n==1:print(sum(d)-max(d))
else:
    p=[(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,5),(2,4),(2,5),(3,4),(3,5),(4,5)]
    t=[(0,1,2),(0,1,3),(0,2,4),(0,3,4),(1,2,5),(1,3,5),(2,4,5),(3,4,5)]
    min1=min(d)
    min2=min(d[i]+d[j] for i,j in p)
    min3=min(d[i]+d[j]+d[k] for i,j,k in t)
    c1=(n-2)*(n-2)*5+(n-2)*4;c2=(n-2)*8+4;c3=4
    print(c1*min1+c2*min2+c3*min3)