from collections import deque
def solution(n, vertex):
    graph = [[] for _ in range(n+1)]
    # 인접리스트 만들기
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)

    # 각 노드까지의 거리
    dist = [-1] * (n + 1)   # -1이면 미방문
    dist[1] = 0 # index 0은 더미노드
    queue = deque([1])
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if dist[i] == -1:
                dist[i] = dist[v] + 1
                queue.append(i)
                
    return dist.count(max(dist))