# [Silver V] 좌표 정렬하기 2 - 11651 

[문제 링크](https://www.acmicpc.net/problem/11651) 

### 성능 요약

메모리: 54216 KB, 시간: 2836 ms

### 분류

정렬

### 제출 일자

2025년 1월 18일 04:35:26

### 문제 설명

<p>2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 x<sub>i</sub>와 y<sub>i</sub>가 주어진다. (-100,000 ≤ x<sub>i</sub>, y<sub>i</sub> ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.</p>

### 출력 

 <p>첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.</p>

## 문제 해결 아이디어

[lambda](https://www.notion.so/lambda-17e5e2536d928020adbbdb195d11eb45?pvs=21)

lambda를 이용하여 y좌표를 기준으로 정렬하고, y 좌표가 같다면 x  좌표를 기준으로 정렬한다.

## 최종 코드

```python
n = int(input())
origin = []
for i in range(n):
    origin.append(tuple(map(int, input().split())))

origin.sort(key=lambda x: (x[1], x[0]))

for i in origin:
    print(*i)
```
