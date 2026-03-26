import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    T = int(input()) # 테스트 케이스의 개수
    
    for _ in range(T):
        n = int(input()) # 팀의 수
        last_year = list(map(int, input().split())) # 작년 순위
        
        # 인접 행렬(adj[a][b]가 True면 a가 b보다 순위가 높음) 및 진입 차수 배열
        adj = [[False] * (n + 1) for _ in range(n + 1)]
        indegree = [0] * (n + 1)
        
        # 1. 작년 순위를 바탕으로 초기 그래프 구성 (완전 그래프)
        for i in range(n):
            for j in range(i + 1, n):
                adj[last_year[i]][last_year[j]] = True
                indegree[last_year[j]] += 1
                
        # 2. 올해 바뀐 순위 적용 (간선 뒤집기)
        m = int(input())
        for _ in range(m):
            u, v = map(int, input().split())
            if adj[u][v]:
                adj[u][v], adj[v][u] = False, True
                indegree[v] -= 1
                indegree[u] += 1
            else:
                adj[v][u], adj[u][v] = False, True
                indegree[u] -= 1
                indegree[v] += 1
                
        # 3. 위상 정렬 로직
        result = []
        q = deque()
        certain = True # 순위가 확실한지 판별
        
        # 진입 차수가 0인 노드를 찾아 큐에 삽입
        for i in range(1, n + 1):
            if indegree[i] == 0:
                q.append(i)
                
        while q:
            # 큐에 2개 이상의 노드가 있다면 순위를 특정할 수 없음
            if len(q) > 1:
                certain = False
                
            now = q.popleft()
            result.append(now)
            
            # 현재 노드와 연결된 노드들의 진입 차수 감소
            for next_node in range(1, n + 1):
                if adj[now][next_node]:
                    indegree[next_node] -= 1
                    # 새롭게 진입 차수가 0이 되면 큐에 삽입
                    if indegree[next_node] == 0:
                        q.append(next_node)
                        
        # 4. 결과 출력
        if len(result) < n:
            # 큐가 일찍 비어서 모든 노드를 방문하지 못함 = 사이클 존재 (모순)
            print("IMPOSSIBLE")
        elif not certain:
            # 사이클은 없지만 큐에 2개 이상 들어간 적이 있음 = 순위 불분명
            print("?")
        else:
            # 정상적으로 위상 정렬 완료
            print(*result)

if __name__ == "__main__":
    solve()