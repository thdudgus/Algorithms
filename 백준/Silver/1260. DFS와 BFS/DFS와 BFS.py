def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    # v에 연결된 모든 노드 순회
    for i in graph[v]:
        if not visited[i]: #방문하지 않았으면 해당 노드를 시작 노드로 다시 dfs
            dfs(graph, i, visited)

from collections import deque
def bfs(graph, start, visited):
    # 현재 노드를 방문 처리
    visited[start] = True
    queue = deque([start])

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')

        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 쿠에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n = list(map(int,input().split()))
graph = []
for i in range(n[0]+1):
    graph.append([])

for i in range(n[1]):
    temp = list(map(int, input().split()))
    graph[temp[0]].append(temp[1])
    graph[temp[1]].append(temp[0])

for i in range(len(graph)):
    graph[i].sort()

visited = [False]*(n[0]+1)
dfs(graph, n[2], visited)
print()
visited = [False]*(n[0]+1)
bfs(graph, n[2], visited)