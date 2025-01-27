n = int(input())
for i in range(n):
    v = [0]
    p = list(input())
    for j in p:
        if j == '(':
            v.append("(")
        elif j == ')':
            if v[-1]=='(': v.pop()
            elif len(v) == 1: v.append(')')
    if len(v) > 1:
        print("NO")
    elif len(v) == 1:
        print("YES")