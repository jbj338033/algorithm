while 1:
    a=input()
    if a=='.':break
    s=[]
    for i in a:
        if i=='(':s.append(1)
        elif i==')':
            if s and s[-1]==1:s.pop()
            else:s.append(3)
        elif i=='[':s.append(2)
        elif i==']':
            if s and s[-1]==2:s.pop()
            else:s.append(4)
    print('no' if s else 'yes')