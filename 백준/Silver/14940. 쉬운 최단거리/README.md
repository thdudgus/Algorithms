# [Silver I] 쉬운 최단거리 - 14940 

[문제 링크](https://www.acmicpc.net/problem/14940) 

### 성능 요약

메모리: 39948 KB, 시간: 444 ms

### 분류

너비 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2025년 1월 30일 23:58:01

### 문제 설명

<p>지도가 주어지면 모든 지점에 대해서 목표지점까지의 거리를 구하여라.</p>

<p>문제를 쉽게 만들기 위해 오직 가로와 세로로만 움직일 수 있다고 하자.</p>

### 입력 

 <p>지도의 크기 n과 m이 주어진다. n은 세로의 크기, m은 가로의 크기다.(2 ≤ n ≤ 1000, 2 ≤ m ≤ 1000)</p>

<p>다음 n개의 줄에 m개의 숫자가 주어진다. 0은 갈 수 없는 땅이고 1은 갈 수 있는 땅, 2는 목표지점이다. 입력에서 2는 단 한개이다.</p>

### 출력 

 <p>각 지점에서 목표지점까지의 거리를 출력한다. 원래 갈 수 없는 땅인 위치는 0을 출력하고, 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1을 출력한다.</p>

## 문제 해결 아이디어

이전에 풀었던 문제와 마찬가지로 dx와 dy를 설정하여 상하좌우를 탐색할 수 있도록 한다.  

입력 중 2가 나오면 해당 인덱스를 저장해둔다.   

해당 인덱스는 모든 점에서의 목표 지점이지만, 해당 인덱스까지의 거리를 알아야하기 때문에, 해당 인덱스를 시작점으로 삼아 너비우선탐색을 진행한다.   

> 시작 노드를 큐에 삽입한다.    
x와 y를 큐에서 꺼내와 dx와 dy를 더한 좌표가 지도의 범위를 넘지 않고, 값이 1일 때만 큐에 삽입한다.(방문하지 않은 노드이기 때문에 1) 그리고 이동한 거리를 세기 위해 mapInfo[xx][yy]의 값에 mapInfo[x][y]를 더해준다.   
큐가 빌 때 까지 위 과정을 반복한다.   
> 

만약 mapInfop[i][j]의 값이 1인 곳은 -1로 변경해준다.   
위 bfs 과정은 갈 수 있는 길이 1로 표시된 mapInfo에 직접 거리를 더하는 것이기 때문에 반복 후, (-1이나 0인 경우 제외)-1을 해준다. 그리고 탐색의 시작점이자 지도의 목표지점인 2를 저장한 인덱스 부분은 0으로 변경해준다.    

## Input 반례 (해결 과정)

```python
import sys
from collections import deque

nm = list(map(int, sys.stdin.readline().split()))
mapInfo = []
for i in range(nm[0]): # row 만큼 반복
    temp = list(map(int, sys.stdin.readline().split()))
    mapInfo.append(temp)
    if 2 in temp:
        sx, sy = i, temp.index(2)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            xx = dx[i] + x
            yy = dy[i] + y

            if 0 <= xx < nm[0] and 0<= yy < nm[1] and mapInfo[xx][yy] == 1:
                queue.append((xx, yy))
                mapInfo[xx][yy] += mapInfo[x][y]

bfs(sx, sy)
for i in range(nm[0]):
    for j in range(nm[1]):
        if mapInfo[i][j] == 1:
            mapInfo[i][j] = -1
            print(mapInfo)
        if mapInfo[i][j] != -1 or mapInfo[i][j] != 0:
            mapInfo[i][j] -= 1
mapInfo[sx][sy] = 0

for i in mapInfo:
    print(*i)
```

위 코드에서 목표 지점까지의 거리들을 쭉 출력해보면 예제출력보다 2씩 큰 것을 알 수 있다. 원래는 시작 지점도 1이라고 생각해 1만 빼면 된다고 생각 했는데, 시작 지점은 2이기 때문에 2를 빼주어야 한다.   

또한, `if mapInfo[i][j] != -1 or mapInfo[i][j] != 0: mapInfo[i][j] -= 1` 해당 부분에서 앞 조건이 True면 뒷 조건이 무시되기 때문에 -1이 아닌 0인 경우도 값이 빼져 답이 틀리게 도출되었었다. 따라서 뒷 조건을 따로 if로 분리하여 올바르게 결과가 도출되도록 하였다. ~~(기초적인 건데 이걸 놓쳤네…)~~   

아래는 최종 코드이다.   

## 최종 코드

```python
import sys
from collections import deque

nm = list(map(int, sys.stdin.readline().split()))
mapInfo = []
for i in range(nm[0]): # row 만큼 반복
    temp = list(map(int, sys.stdin.readline().split()))
    mapInfo.append(temp)
    if 2 in temp:
        sx, sy = i, temp.index(2)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            xx = dx[i] + x
            yy = dy[i] + y

            if 0 <= xx < nm[0] and 0<= yy < nm[1] and mapInfo[xx][yy] == 1:
                queue.append((xx, yy))
                mapInfo[xx][yy] += mapInfo[x][y]

bfs(sx, sy)
for i in range(nm[0]):
    for j in range(nm[1]):
        if mapInfo[i][j] == 1:
            mapInfo[i][j] = -1
        if mapInfo[i][j] == 0:
            continue
        if mapInfo[i][j] != -1:
            mapInfo[i][j] -= 2

for i in mapInfo:
    print(*i)

```
