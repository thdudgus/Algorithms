import sys

lines = []
while True:
    s = input()
    if s == ".":
        break 
    lines.append(s)
s = []

for x in lines:
    for y in x:
        if y == "(" or y == "[":
            s.append(y)
        if y == ")":
            if len(s) == 0: 
                s.append(y)
                break
            elif s[-1] == "(":
                s.pop()
            elif s[-1] != "(":
                s.append(y)
                break
        if y == "]":
            if len(s) == 0:
                s.append(y)
                break
            elif s[-1] == "[":
                s.pop()
            elif s[-1] != "[":
                s.append(y)
                break
    print("yes" if len(s) == 0 else "no")
    s.clear()