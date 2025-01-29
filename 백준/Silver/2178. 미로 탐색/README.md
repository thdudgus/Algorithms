# [Silver I] 미로 탐색 - 2178 

[문제 링크](https://www.acmicpc.net/problem/2178) 

### 성능 요약

메모리: 34944 KB, 시간: 68 ms

### 분류

너비 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2025년 1월 30일 03:32:33

### 문제 설명

<p>N×M크기의 배열로 표현되는 미로가 있다.</p>

<table class="table table-bordered" style="width:18%">
	<tbody>
		<tr>
			<td style="width:3%">1</td>
			<td style="width:3%">0</td>
			<td style="width:3%">1</td>
			<td style="width:3%">1</td>
			<td style="width:3%">1</td>
			<td style="width:3%">1</td>
		</tr>
		<tr>
			<td>1</td>
			<td>0</td>
			<td>1</td>
			<td>0</td>
			<td>1</td>
			<td>0</td>
		</tr>
		<tr>
			<td>1</td>
			<td>0</td>
			<td>1</td>
			<td>0</td>
			<td>1</td>
			<td>1</td>
		</tr>
		<tr>
			<td>1</td>
			<td>1</td>
			<td>1</td>
			<td>0</td>
			<td>1</td>
			<td>1</td>
		</tr>
	</tbody>
</table>

<p>미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.</p>

<p>위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.</p>

### 입력 

 <p>첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 <strong>붙어서</strong> 입력으로 주어진다.</p>

### 출력 

 <p>첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.</p>

## 문제 해결 아이디어

제한시간은 1초로 약 1억번의 연산이 가능하다.   

N, M의 크기가 2이상 100이하의 정수이기 때문에 시간복잡도는 크게 신경쓰지 않아도 될 듯 하다.   
</br>

입력을 연결 정보로 저장해서 인접 구역을 미리 설정하는 게 아니라, 노드에 대해 상하좌우를 그때그때 탐색할 수 있도록 해야 한다.   

(범위를 벗어나거나 0이면 return하도록)   

- BFS 사용: 상하좌우 인접한 1을 탐색
- visited 배열로 중복 탐색 방지
- 연결 구역 세기: 방문하지 않은 새로운 1을 발견할 때마다 count 1 증가. 연결이 끊어진다면 count 1 감소

## Input 반례 (해결 과정)

`nm = map(int, sys.stdin.readline().split())`에서 오류가 발생하였다.    

⇒ **`map` 객체는 iterable**이지만, 리스트처럼 인덱스로 접근할 수 없다. nm[0]처럼 사용 불가.   
⇒ 따라서 list()로 변환하여 사용해야 한다. `nm = list(map(int, sys.stdin.readline().split()))`   
</br> 

**입력값을 한글자씩 분리하려면?**    

`sys.stdin.readline().split()`대신에 아래 코드 사용.   

**공백이 아니라 한 글자씩 숫자로 변환하려면 strip()만 사용해야 함.**   

```python
line = "1111"  # 예제 입력
numbers = list(map(int, line.strip()))  # '1111' -> [1, 1, 1, 1]
print(numbers)  # [1, 1, 1, 1]
```
</br>

직접 코드를 작성하면서 위와 같은 문제점들을 겪었지만, 코드를 어떻게 구성해야 할지 갈피를 잡지 못 해 다른 사람의 글을 참고하였다.   

dfs를 사용해보려 하였으나, dfs는 모든 정점을 탐색한다. 미로를 탈출하는 최소한의 거리였기 때문에 bfs를 사용하여야 한다.   

dx와 dy를 상하좌우 이동이 가능하도록 설정하고, bfs의 인수 x와 y에 더하여 좌표가 옮겨진 xx와 yy를 얻을 수 있다. 옮겨진 좌표가 범위를 넘지 않고, 값이 1일 때만 queue에 넣고, maze의 값을 1 올려주면 이동한 거리가 된다.   

queue가 빌 때까지 위 과정을 반복하고, 도착 지점 좌표의 maze 값을 반환하면 최종적으로 이동한 거리가 된다.  
  

아래는 최종 코드이다.   

## 최종 코드

```python
import sys
from collections import deque

nm = list(map(int, sys.stdin.readline().split()))  # map 객체를 list로 변환
maze = []
for i in range(nm[0]):  # nm[0]: n (row, 행)
    maze.append(list(map(int, sys.stdin.readline().strip())))  # list 변환 추가

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < nm[0] and 0 <= yy < nm[1] and maze[xx][yy] == 1:
                queue.append((xx, yy))
                maze[xx][yy] = maze[x][y]+1
    return maze[nm[0]-1][nm[1]-1]
print(bfs(0,0))
```
