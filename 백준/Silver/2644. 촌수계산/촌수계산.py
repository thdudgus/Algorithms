import sys
from collections import deque

n = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split())) # (부모, 자식)
k = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]

for _ in range(k):
    t, tt = map(int, sys.stdin.readline().split())
    graph[t].append(tt)
    graph[tt].append(t)

visited = [0] * (n+1)

def bfs(graph, start, target_node):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        if v == target_node:
            return visited[v]
        for i in graph[v]:
            if visited[i] == 0 and i != start:
                queue.append(i)
                visited[i] = visited[v] + 1
    return -1

print(bfs(graph, target[0], target[1]))