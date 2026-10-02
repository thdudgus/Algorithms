from collections import deque

def bfs(start, graph, n):
    visited = [False for _ in range(n+1)]
    visited[start] = True
    queue = deque([start])
    count = 0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                count += 1
    return count

def solution(n, results):
    win = [[] for _ in range(n+1)]
    lose = [[] for _ in range(n+1)]
    for a, b in results:
        win[a].append(b)
        lose[b].append(a)
    
    answer = 0
    for i in range(1, n + 1):
        if bfs(i, win, n) + bfs(i, lose, n) == n - 1:
            answer += 1
        
    return answer