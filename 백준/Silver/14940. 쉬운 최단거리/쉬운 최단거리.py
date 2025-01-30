import sys
from collections import deque

nm = list(map(int, sys.stdin.readline().split()))
mapInfo = []
for i in range(nm[0]): # row 만큼 반복
    temp = list(map(int, sys.stdin.readline().split()))
    mapInfo.append(temp)
    if 2 in temp:
        sx, sy = i, temp.index(2)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            xx = dx[i] + x
            yy = dy[i] + y

            if 0 <= xx < nm[0] and 0<= yy < nm[1] and mapInfo[xx][yy] == 1:
                queue.append((xx, yy))
                mapInfo[xx][yy] += mapInfo[x][y]

bfs(sx, sy)
for i in range(nm[0]):
    for j in range(nm[1]):
        if mapInfo[i][j] == 1:
            mapInfo[i][j] = -1
        if mapInfo[i][j] == 0:
            continue
        if mapInfo[i][j] != -1:
            mapInfo[i][j] -= 2

for i in mapInfo:
    print(*i)
