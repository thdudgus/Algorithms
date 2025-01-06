n = int(input())
addition = []
addition.append(0) #0
addition.append(1) #1
addition.append(2) #2
addition.append(4) #3
case = []
for i in range(n):
    case.append(int(input()))

if max(case) > 3:
    for i in range(4, max(case)+1):
        addition.append(addition[i-1]+addition[i-2]+addition[i-3])

for i in range(n):
    print(addition[case[i]])