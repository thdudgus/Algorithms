import heapq
import sys
input = sys.stdin.readline  
INF = 1000000000 

# 노드 개수, 간선 개수
n, m = map(int, input().split())
# 시작 노드
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기.
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력 받기
for _ in range(m):
	a, b, c = map(int, input().split())
	# a번 노드에서 b번 노드로 가는 비용이 c
	graph[a].append((b, c))
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
dijkstra(start)

for i in range(1, n + 1):
	if distance[i] == INF:
		print("INF")
	else: print(distance[i])