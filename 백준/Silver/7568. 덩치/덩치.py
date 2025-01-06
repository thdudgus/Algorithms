n = int(input())
body = []
rank = []
for i in range(n):
    body.append(list(map(int, input().split())))
    rank.append(1)

for i in range(n): # 비교
    for j in range(n): # 비교 당함
        if i == j:
            continue
        if (body[i][0] < body[j][0]) and (body[i][1] < body[j][1]):
            rank[i] = rank[i] + 1

print(*rank)