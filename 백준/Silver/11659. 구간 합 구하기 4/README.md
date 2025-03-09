# [Silver III] 구간 합 구하기 4 - 11659 

[문제 링크](https://www.acmicpc.net/problem/11659) 

### 성능 요약

메모리: 64536 KB, 시간: 204 ms

### 분류

누적 합

### 제출 일자

2025년 3월 9일 20:04:16

### 문제 설명

<p>수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.</p>

### 출력 

 <p>총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.</p>



## 문제 해결 아이디어

시간 제한은 1초로 약 1억번의 연산이 가능하다.   

n과 m이 10만이기 때문에 O(nlogn)이 되어야 한다.   

수를 저장하는 배열 number를 만들고 인덱스 0은 비워둔다. 인덱스 1부터 첫번째 숫자이다.   

입력을 모두 받은 후 구간 합을 진행한다.   

## Input 반례 (해결 과정)

```python
temp = list(map(int, input().split()))
n = temp[0]
m = temp[1]
number = list(map(int, input().split()))
number.insert(0, 0)
op = []
for i in range(m):
    op.append(list(map(int, input().split())))
for i in range(m):
    total = 0
    temp = op[i][1] - op[i][0] + 1
    for j in range(temp):
        total += number[op[i][0] + j]
    print(total)
```

for문이 두 번 중첩되어 시간초과가 발생하였다.   

```python
temp = list(map(int, input().split()))
n = temp[0]
m = temp[1]
number = list(map(int, input().split()))
number.insert(0, 0)
for i in range(m):
    op = list(map(int, input().split()))
    total = sum(number[op[0]:op[1]+1])
    print(total)
```

위 처럼 for문의 중첩을 해제해보았지만, 반복의 횟수는 같아 여전히 시간초과가 발생하였다.    

<aside>
💡

누적합을 이용하자! 

</aside>

**누적합**   

배열이나 리스트의 각 위치까지의 합을 미리 계산해놓은 결과.   

예를 들어, `리스트가 [1, 2, 3, 4, 5]`라면 누적합은 다음과 같이 계산된다.    

- 첫 번째 요소: 1
- 두 번째 요소까지의 합: 1 + 2 = 3
- 세 번째 요소까지의 합: 1 + 2 + 3 = 6
- 네 번째 요소까지의 합: 1 + 2 + 3 + 4 = 10
- 다섯 번째 요소까지의 합: 1 + 2 + 3 + 4 + 5 = 15

따라서 누적합 배열은 [1, 3, 6, 10, 15]가 된다.   

이렇게 누적합을 미리 구해두면, 이후에 특정 구간의 합을 빠르게 계산할 수 있다.    

예를 들어 `리스트의 인덱스 i부터 j까지의 합`을 구하고 싶다면, 누적합 배열을 이용하여 `구간합 = 누적합[j] - 누적합 [i-1]`와 같이 계산할 수 있다. (단, i가 0일 경우 누적합[j]가 해당 구간의 합이 된다.   

위 개념을 이용하여 누적합을 미리 구한 후, 구간합을 구해보겠다.    

```python
temp = list(map(int, input().split()))
n = temp[0]
m = temp[1]
number = list(map(int, input().split()))
number.insert(0, 0)
addSum =  [0] * (n + 1)
for i in range(1, n + 1):
    addSum[i] = addSum[i - 1] + number[i]
for _ in range(m):
    temp = list(map(int, input().split()))
    i = temp[0]
    j = temp[1]
    
    print(addSum[j] - addSum[i - 1])
```

시간초과이다… 왜일까..?   

~~일단 insert는 O(N)이 걸리므로, 인덱스를 조정하여 삭제해보도록 하겠다.~~ ~~(인덱스 0인 경우를 생각하기 번거로워서 insert를 사용했던 거였는데…)~~     

그리고 n과 m이 늘어날 수록 input이 너무 많이 이루어져서 그런 걸로 예상이 된다.    

아래는 정답 코드이다.    

read 사용법이 아직 익숙치 않은데 이를 잘 익혀야겠다….     

## 최종 코드

```python
import sys

# 한 번에 입력을 받아 리스트로 변환
input_data = sys.stdin.read().split()

# 첫 번째 줄에서 n, m 가져오기
n = int(input_data[0])
m = int(input_data[1])

# 두 번째 줄에서 숫자 리스트 가져오기
number = list(map(int, input_data[2:n+2]))

# 누적합 배열 생성 (0번 인덱스를 추가하여 초기값 0으로 설정)
addSum = [0] * (n + 1)
for i in range(1, n + 1):
    addSum[i] = addSum[i - 1] + number[i - 1]

# m개의 쿼리 처리
index = n + 2 # 첫 번째 줄(N, M)과 두 번째 줄(N개의 수)을 제외한 인덱스, 세번째 부터 (M개의 쿼리)
result = []
for _ in range(m):
    i = int(input_data[index])
    j = int(input_data[index + 1])
    index += 2

    # 구간 합 계산
    result.append(str(addSum[j] - addSum[i - 1]))

# 결과 출력 (sys.stdout.write 사용)
sys.stdout.write("\n".join(result) + "\n")

```
