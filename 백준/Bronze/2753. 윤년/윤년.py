y=int(input())
print(1 if y%4==0 and y%100!=0 or y%400==0 else 0)