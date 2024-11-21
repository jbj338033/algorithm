for _ in range(int(input())):
    a=input()
    s=[]
    for i in a:
        if i=='(':s.append('(')
        elif i==')':
            if s and s[-1]=='(':s.pop()
            else:s.append(')')
    print('NO' if s else 'YES')