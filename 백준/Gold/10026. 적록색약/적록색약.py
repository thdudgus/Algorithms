import sys
sys.setrecursionlimit(10000)

# DFS 함수 정의
def dfs(x, y, color): # (행, 열, 색깔)
    if x < 0 or x >= N or y < 0 or y >= N:  # 범위를 벗어나거나 
        return
    if visited[x][y] or grid[x][y] != color:  # 이미 방문했거나 다른 색이면 종료
        return

    # 현재 위치 방문 처리
    visited[x][y] = True

    # 상하좌우 탐색
    dfs(x-1, y, color)
    dfs(x+1, y, color)
    dfs(x, y-1, color)
    dfs(x, y+1, color)

# 입력 받기
N = int(input())  
grid = [list(input().strip()) for _ in range(N)]

# 방문 여부를 저장할 2차원 리스트 생성
visited = [[False] * N for _ in range(N)]

# 각 색깔의 구역 수 세기
region_count = 0
# 적록색맹 X
for i in range(N):
    for j in range(N):
        if not visited[i][j]:  # 방문하지 않았다면 새로운 구역 발견
            dfs(i, j, grid[i][j])  # 해당 색깔로 DFS 탐색
            region_count += 1  # 구역 수 증가
print(region_count, end=" ")

# 적록색맹 O
region_count = 0
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if grid[i][j] == 'R':
            grid[i][j] = 'G'

for i in range(N):
    for j in range(N):
        if not visited[i][j]:  # 방문하지 않았다면 새로운 구역 발견
            dfs(i, j, grid[i][j] )  # 해당 색깔로 DFS 탐색
            region_count += 1  # 구역 수 증가
print(region_count)
