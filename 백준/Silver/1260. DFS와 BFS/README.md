# [Silver II] DFS와 BFS - 1260 

[문제 링크](https://www.acmicpc.net/problem/1260) 

### 성능 요약

메모리: 35712 KB, 시간: 328 ms

### 분류

그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

### 제출 일자

2025년 1월 29일 19:28:47

### 문제 설명

<p>그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.</p>

### 입력 

 <p>첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.</p>

### 출력 

 <p>첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.</p>

## 문제 해결 아이디어

재귀를 이용해 dfs와 bfs를 구현한다.   

dfs (스택 사용)     

1. 탐색 시작 노드를 스택에 삽임하고 방문 처리
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있다면 그 노드를 스택에 넣고 방문 처리
    1. 방문하지 않은 인접 노드가 없다면 스택에서 최상단 노드 꺼내기
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

(방문 처리는 스택에 한 번 삽입되어 처리된 노드가 다시 삽입되지 않게 체크하는 것. 방문처리를 함으로써 각 노드를 한 번씩만 처리할 수 있다.)    

bfs (큐 사용)    

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
3. 2번의 과정을 더이상 수행할 수 없을 때까지 반복한다.

## Input 반례 (해결 과정)

첫 예제에서 결과가 두 탐색 모두 1 2 3 4로 나왔다.    

DFS에 대한 이해가 부족하여 DFS의 결과가 1 2 3 4로 생각했지만 1 2 4 3이 옳은 결과였다.     

1. 시작 정점 1에서 출발
2. 1번과 연결된 정점들 중 작은 정점을 방문(2)
3. 2번과 연결된 정점들 중 작은 정점을 방문(4)
4. 4번에 연결된 정점들 중 작은 정점을 방문(3)
5. 더이상 방문할 정점이 없으므로 종료. (1로 돌아갔지만 1과 연결된 정점들 2, 3, 4는 모두 방문 처리 완료)
</br>

그리고 그래프를 입력받고 parsing하는 방법이 잘못되었었다.    

원래는 단순히 그래프를 그대로 입력받았는데, 작성한 dfs와 bfs 코드는 인덱스 번호가 정점 번호로, 해당 정점에 연결된 정점들 번호가 인덱스의 값으로 들어가 있었다.     

따라서, 아래 코드처럼 입력된 정점 정보를 인덱스로 하여 연결된 정점들을 graph에 새롭게 parsing하였다.    

예제 입력은 정점 1에 [1, 2], [1, 3], [1, 4]로 연결을 표시했지만 탐색에 사용할 graph는 graph[1]의 값을 [2, 3, 4]로 되도록 코드를 작성하였다. 또한 작은 정점부터 방문해야 하기 때문에, 입력 값 parsing 후 그래프를 인덱스마다 정렬하였다.   

(graph[0]은 정점 번호가 없으므로 빈 칸이다.)    

```python
graph = []
for i in range(n[0]+1):
    graph.append([])

for i in range(n[1]):
    temp = list(map(int, input().split()))
    graph[temp[0]].append(temp[1])
    graph[temp[1]].append(temp[0])

for i in range(len(graph)):
    graph[i].sort()
```

위처럼 graph를 제대로 설정하니 정답이 되었다.    

## 최종 코드

```python
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
```
