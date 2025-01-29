import sys
from collections import deque

nm = list(map(int, sys.stdin.readline().split()))  # map 객체를 list로 변환
maze = []
for i in range(nm[0]):  # nm[0]: n (row, 행)
    maze.append(list(map(int, sys.stdin.readline().strip())))  # list 변환 추가

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < nm[0] and 0 <= yy < nm[1] and maze[xx][yy] == 1:
                queue.append((xx, yy))
                maze[xx][yy] = maze[x][y]+1
    return maze[nm[0]-1][nm[1]-1]
print(bfs(0,0))