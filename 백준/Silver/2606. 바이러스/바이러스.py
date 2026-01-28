n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False] * (n+1)

def virus(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            virus(graph, i, visited)

virus(graph, 1, visited)
print(visited.count(True)-1) 