# [Silver III] 킹 - 1063 

[문제 링크](https://www.acmicpc.net/problem/1063) 

### 성능 요약

메모리: 32412 KB, 시간: 40 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2026년 3월 12일 22:55:41

### 문제 설명

<p>8*8크기의 체스판에 왕이 하나 있다. 킹의 현재 위치가 주어진다. 체스판에서 말의 위치는 다음과 같이 주어진다. 알파벳 하나와 숫자 하나로 이루어져 있는데, 알파벳은 열을 상징하고, 숫자는 행을 상징한다. 열은 가장 왼쪽 열이 A이고, 가장 오른쪽 열이 H까지 이고, 행은 가장 아래가 1이고 가장 위가 8이다. 예를 들어, 왼쪽 아래 코너는 A1이고, 그 오른쪽 칸은 B1이다.</p>

<p>킹은 다음과 같이 움직일 수 있다.</p>

<ul>
	<li>R : 한 칸 오른쪽으로</li>
	<li>L : 한 칸 왼쪽으로</li>
	<li>B : 한 칸 아래로</li>
	<li>T : 한 칸 위로</li>
	<li>RT : 오른쪽 위 대각선으로</li>
	<li>LT : 왼쪽 위 대각선으로</li>
	<li>RB : 오른쪽 아래 대각선으로</li>
	<li>LB : 왼쪽 아래 대각선으로</li>
</ul>

<p>체스판에는 돌이 하나 있는데, 돌과 같은 곳으로 이동할 때는, 돌을 킹이 움직인 방향과 같은 방향으로 한 칸 이동시킨다. 아래 그림을 참고하자.</p>

<p style="text-align:center"><img alt="" src="https://upload.acmicpc.net/259549ad-b275-48a1-91f7-197a7ce72a23/-/preview/"></p>

<p>입력으로 킹이 어떻게 움직여야 하는지 주어진다. 입력으로 주어진 대로 움직여서 킹이나 돌이 체스판 밖으로 나갈 경우에는 그 이동은 건너 뛰고 다음 이동을 한다.</p>

<p>킹과 돌의 마지막 위치를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 킹의 위치, 돌의 위치, 움직이는 횟수 N이 주어진다. 둘째 줄부터 N개의 줄에는 킹이 어떻게 움직여야 하는지 주어진다. N은 50보다 작거나 같은 자연수이고, 움직이는 정보는 위에 쓰여 있는 8가지 중 하나이다.</p>

### 출력 

 <p>첫째 줄에 킹의 마지막 위치, 둘째 줄에 돌의 마지막 위치를 출력한다.</p>

## 문제 해결 아이디어

체스판의 위치는 좌표를 쓸 필요 없이, 단순히 2차원 리스트로 하여 1과 8 사이의 값이 있는지만 확인하면 된다.

킹을 이동시킨다.

조건

1. 킹 이동하고 나니 돌과 같은 곳이면, 돌도 같은 방향으로 옮긴다.
2. 근데 킹이든 돌이든 체스판 밖이면 해당 이동은 rollback

## Input 반례 (해결 과정)

첫번째 예제 input에 대한 결과만 맞고, 두번째 예제부턴 그냥 input에 넣은 좌표 그대로 출력이 됐다.. 출력을 확인해보니 그냥 단순히 dir 문자가 더해진 상태였다. `[1, 1]`이 입력이면 `[1, 1, ‘B’]`와 같이 되었다. 

또한, 난 `dir`을 입력받으면, 위에 선언한 리스트의 값과 자동으로 매치되는 줄 알았는데 그게 아니었다… `dir`이 `‘B’`면 자동으로 B리스트 값이 `dir`에 들어가는 줄 알았다… 

⇒ 직접 매칭시켜줘야 한다.. directions 함수로 따로 만들어줬다..

또한 `[1, 1] + [2, 4]`이 numpy처럼 `[3, 5]`가 된다고 생각했는데 `[1, 1, 2, 4]`가 된다.. `zip`을 이용해 각 원소끼리 더해지도록 하였다.

## 최종 코드

```python
import sys
king, stone, n = sys.stdin.readline().split()
king = list(king)
stone = list(stone)
n = int(n)
king_location = [ord(king[0]) - 64, int(king[1])]
stone_location = [ord(stone[0]) - 64, int(stone[1])]

def directions(dir):
    if dir == 'R': dir = [1, 0]
    elif dir == 'L': dir = [-1, 0]
    elif dir == 'B': dir = [0, -1]
    elif dir == 'T': dir = [0, 1]
    elif dir == 'RT': dir = [1, 1]
    elif dir == 'LT': dir = [-1, 1]
    elif dir == 'RB': dir = [1, -1]
    elif dir == 'LB': dir = [-1, -1]
    return dir

for _ in range(n):
    dir = sys.stdin.readline().rstrip()
    direction = directions(dir)
    flag = False

    king_location = [x+y for x, y in zip(king_location, direction)]
    if king_location == stone_location:
        stone_location = [x+y for x, y in zip(stone_location, direction)]
        flag = True
    if king_location[0] < 1 or king_location[0] > 8 or king_location[1] < 1 or king_location[1] > 8 or stone_location[0] < 1 or stone_location[0] > 8 or stone_location[1] < 1 or stone_location[1] > 8:
        king_location = [x-y for x, y in zip(king_location, direction)]
        if flag: stone_location = [x-y for x, y in zip(stone_location, direction)]

print(chr(king_location[0] + 64) + str(king_location[1]))
print(chr(stone_location[0] + 64) + str(stone_location[1]))
```
