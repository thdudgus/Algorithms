from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    visited = [[False] * m for _ in range(n)]
    que = deque([(0, 0, 1)])  # (row, col, 거리) - 시작은 1칸째
    visited[0][0] = True
    
    while que:
        row, col, dist = que.popleft()
        
        # 도착점이면 바로 반환
        if row == n - 1 and col == m - 1:
            return dist
        
        for dr, dc in directions:
            nr = row + dr
            nc = col + dc
            
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            if maps[nr][nc] == 0:
                continue
            if visited[nr][nc]:
                continue
            
            visited[nr][nc] = True
            que.append((nr, nc, dist + 1))
    
    # 큐가 다 빌 때까지 도착 못 하면 -1
    return -1