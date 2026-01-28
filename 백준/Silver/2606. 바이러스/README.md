# [Silver III] 바이러스 - 2606 

[문제 링크](https://www.acmicpc.net/problem/2606) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

### 제출 일자

2026년 1월 29일 00:08:08

### 문제 설명

<p>신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.</p>

<p>예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.</p>

<p><img alt="" src="https://www.acmicpc.net/upload/images/zmMEZZ8ioN6rhCdHmcIT4a7.png" style="width: 239px; height: 157px; "></p>

<p>어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하인 양의 정수이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.</p>

### 출력 

 <p>1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.</p>

## Input 반례 (해결 과정)

```python
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False] * n

def virus(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            virus(graph, i, visited)

virus(graph, 1, visited)
print(visited.count(True)) 
```

해당 코드에 예제 입력1을 실행하면 정답인 4가 아니라 5가 출력되었다. 문제에서 요구사하는 정답은 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 것이었다. 따라서  `print(visited.count(True))`에서 -1을 빼서 1번 컴퓨터를 제외시켜주는 것이다. (1번 컴퓨터도 당연히 True이기 때문)    

`visited = [False] * n`에서 index error가 발생하였다. `graph`에서 0번 인덱스는 포함하지 않아 range를 n+1로 잡은 것처럼, visited도 0번 인덱스를 포함한 n+1의 공간이 필요하다.    

수정한 최종 코드는 아래와 같다.    

## 최종 코드
```python
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
```
