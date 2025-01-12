n = int(input())
origin = []
for i in range(n):
    temp = tuple(map(int, input().split()))
    origin.append(temp)

origin.sort(key=lambda x:(x[0], x[1]))

for i in origin:
    print(*i)