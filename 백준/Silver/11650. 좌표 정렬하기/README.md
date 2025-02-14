# [Silver V] 좌표 정렬하기 - 11650 

[문제 링크](https://www.acmicpc.net/problem/11650) 

### 성능 요약

메모리: 54216 KB, 시간: 2860 ms

### 분류

정렬

### 제출 일자

2025년 1월 12일 14:33:56

### 문제 설명

<p>2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 x<sub>i</sub>와 y<sub>i</sub>가 주어진다. (-100,000 ≤ x<sub>i</sub>, y<sub>i</sub> ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.</p>

### 출력 

 <p>첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.</p>


## 문제 해결 아이디어   

#### 튜플    

튜플은 변경이 불가능한 자료형이다.    

각 좌표의 값이 변할 필요가 없기 때문에 튜플을 사용하였다.      

#### 튜플 정렬

```python
t = [(3, 4), (1, 1), (1, -1), (2, 2), (3, 3)]

t.sort(key=lambda x:x[0]) // 첫 번째 원소로 오름차순 정렬
t.sort(key=lambda x:x[1]) // 두번째 원소로 오름차순 정렬

t.sort(key=lambda x:-x[0]) // 첫 번째 원소로 내림차순 정렬
t.sort(key=lambda x:-x[1]) // 두 번째 원소로 내림차순 정렬

t.sort(key=lambda x:(x[0], x[1])) // 첫 번째 원소로 오름차순 정렬, 첫 번째 원소가 같은 경우 두 번째 원소로 오름차순 정렬
```

- 모든 `sort()` 메서드는 **Timsort** 기반이며, 시간복잡도는 O(n log n)으로 동일하다.    
- **공간복잡도:** `O(n)` (정렬 과정에서 추가 메모리 사용)     
- **안정 정렬:** `t.sort(key=lambda x:(x[0], x[1]))`와 같은 다중 조건 정렬에서도 첫 번째 기준이 동일한 경우 두 번째 기준으로 안정적으로 정렬된다.    

## 최종 코드
```python
n = int(input())
origin = []
for i in range(n):
    origin.append(tuple(map(int, input().split())))

origin.sort(key=lambda x:(x[0], x[1]))

for i in origin:
    print(*i)
```
