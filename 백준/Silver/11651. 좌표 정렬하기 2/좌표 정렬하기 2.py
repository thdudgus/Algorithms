n = int(input())
origin = []
for i in range(n):
    origin.append(tuple(map(int, input().split())))

origin.sort(key=lambda x: (x[1], x[0]))

for i in origin:
    print(*i)