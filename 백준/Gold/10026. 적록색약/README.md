# [Gold V] 적록색약 - 10026 

[문제 링크](https://www.acmicpc.net/problem/10026) 

### 성능 요약

메모리: 32808 KB, 시간: 68 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2025년 1월 18일 02:39:53

### 문제 설명

<p>적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.</p>

<p>크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)</p>

<p>예를 들어, 그림이 아래와 같은 경우에</p>

<pre>RRRBB
GGBBB
BBBRR
BBRRR
RRRRR</pre>

<p>적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)</p>

<p>그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)</p>

<p>둘째 줄부터 N개 줄에는 그림이 주어진다.</p>

### 출력 

 <p>적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.</p>

 ## 문제 해결 아이디어

시간제한 1초. 약 1억번 계산 가능.   

1 ≤ N ≤ 100 이기 때문에 크게 고려하지 않아도 될 듯하다.    

문제 분류를 보니 그래프탐색으로 해결해야 할 듯 하다.    

[그래프 탐색 (DFS/BFS)](https://www.notion.so/DFS-BFS-17e5e2536d9280c3919ee1ed0a01272c?pvs=21)

---

**dfs를 활용해서 해당 문제 풀기**

1. 첫째 줄에 N이 주어지고, 둘째 줄부터 N개의 줄에 그림이 주어지면, 그걸 바탕으로 그래프 정보를 완성한다.
    
    0 노드는 빈 노드로 남겨두고, 노드 1부터 N*N까지 그래프 정보는 아래와 같다.
    
    | **n(노드)** |  n과 연결된 노드 |
    | --- | --- |
    | **1** |  n+1, n+N |
    | **2~N-1** | n-1, n+1, n+N |
    | **N** | n-1, n+N |
    | **1+N, 1+2N, … 1+(N-2)N** | n-N, n+1,n+N |
    | **2*N, … (N-1)*N** | n-N, n-1, n+N |
    | **1+N(N-1)** | n-N, n+1 |
    | **1+N(N-1)+1, … 1+N(N-1)+N-2** | n-N, n-1, n+1 |
    | **N*N** | n-N, n-1 |
    | **그 외** | n+1, n-1, n+N, n-N |
    
    (N≥3일 때 위 정보를 따른다. N=1일 땐 무조건 구역은 한 개. N=2일 땐 밑줄 친 부분으로만 그래프 정보를 구성하면 된다.)
    
2. 연결된 경로 중, 방문하지 않고 R일 때, G일 때, B일 때로 교체된 횟수를 센다. (ex. R 탐색이 끝나고 G로 변경되면 구역+1 한다.)
3. 연결된 경로 중, 적록 색약인 경우를 고려해 R or G일 때, B일 때로 교체된 횟수를 센다.
4. 결과를 출력한다.

## Input 반례 (해결 과정)

> 그래프 연결 정보를 저장하는 건 할 수 있는데 RGB를 어떻게 구분해야 할지 잘 모르겠다…
> 
- code
    
    ```
    import sys
    
    def dfs(graph, v, visited):	
    	# 현재 노드와 연결된 다르 노드를 재귀적으로 방문
    	for i in graph[v]: # v에 연결된 모든 노드 순회
    		if not visited[i]:
                   
    			dfs(graph, i, visited)
                   
    rgb = {"R":0, "G":0 ,"B":0}
    
    # 그림의 색 정보
    grid = []
    N = int(input()) 
    for i in range(N):
        row = list(input())
        grid.extend(row)
    
    # 그림의 각 점 연결 정보 저장
    graph = []
    graph.append([])
    for i in range(1, N+1): 
        if N==2:
            graph.append([2, 3])
            graph.append([1, 4])
            graph.append([2, 3])
        if N>=3:
            for j in range(1, N+1):
                n = i*j
                if i==1 and j==1: #1
                    graph.append([2, 1+N])
                elif i==1 and j!=1 and j!=N: # 2 ~ N-1
                    graph.append([n-1, n+1, n+N])
                elif i==1 and j==N: #N
                    graph.append([N-1, N+N])
    
                elif i!=1 and i!=N and j==1: # N+1, 2N+1, .. (N-1)N+1
                    graph.append([n-N, n+1, n+N])
                elif i!=1 and i!=N and j==N: # 2*N, … (N-1)*N
                    graph.append([n-N, n-1, n+N])
    
                elif i==N and j==1: #1+N(N-1)
                    graph.append([N*N-N+1-N, N*N-N+2])
                elif i==N and j!=1 and j!=N: # 1+N(N-1)+1, … 1+N(N-1)+N-2
                    graph.append([n-N, n+1, n-1])
                elif i==N and j==N: #N*N
                    graph.append([N*N-N, N*N-1])
    
                else:
                    graph.append([n+1, n-1, n+N, n-N])
    
    visited = [False]*9
    dfs(graph, 1, visited)
    ```
    

⇒ 그래프 인접 구역을 미리 설정하는 게 아니라 노드에 대해 상하좌우를 그때그때 탐색할 수 있도록 해야 한다. (범위를 벗어나거나 색깔이 다르면 return 하도록)    

- **DFS 사용:** 상하좌우 인접한 같은 색을 연결된 하나의 구역으로 간주.
- **재귀 사용:** `dfs`를 통해 같은 색의 모든 영역을 방문.
- **방문 체크:** `visited` 배열로 중복 탐색 방지.
- **연결 구역 세기:** 방문하지 않은 새로운 좌표를 발견할 때마다 `region_count` 증가.

```python
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
```

그림의 색을 나타내는 grid가 아래 사진처럼 2차원 리스트로 저장되기 때문에 (예제 입력)    

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/0f18c247-6d18-4d5e-9eab-6f66bdc404b1/bbafb531-00d8-41ff-9f9a-4204375adb53/image.png)

2차원 리스트의 인덱스 하나하나 순회하면서 방문하지 않았다면, dfs를 호출하여 구한다.     

dfs를 호출하고 난 후에 재귀적으로 grid를 탐색하게 된다. 갈 곳이 없거나 같은 색이 아니라면 return 되기 때문에 이 때 region_count를 +1 해준다.     

## 최종 코드
위 코드와 같다.
