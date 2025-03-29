# [Gold V] AC - 5430 

[문제 링크](https://www.acmicpc.net/problem/5430) 

### 성능 요약

메모리: 52000 KB, 시간: 312 ms

### 분류

덱, 파싱, 구현, 문자열, 자료 구조

### 제출 일자

2025년 3월 29일 22:47:17

### 문제 설명

<p>선영이는 주말에 할 일이 없어서 새로운 언어 AC를 만들었다. AC는 정수 배열에 연산을 하기 위해 만든 언어이다. 이 언어에는 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.</p>

<p>함수 R은 배열에 있는 수의 순서를 뒤집는 함수이고, D는 첫 번째 수를 버리는 함수이다. 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.</p>

<p>함수는 조합해서 한 번에 사용할 수 있다. 예를 들어, "AB"는 A를 수행한 다음에 바로 이어서 B를 수행하는 함수이다. 예를 들어, "RDD"는 배열을 뒤집은 다음 처음 두 수를 버리는 함수이다.</p>

<p>배열의 초기값과 수행할 함수가 주어졌을 때, 최종 결과를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 테스트 케이스의 개수 T가 주어진다. T는 최대 100이다.</p>

<p>각 테스트 케이스의 첫째 줄에는 수행할 함수 p가 주어진다. p의 길이는 1보다 크거나 같고, 100,000보다 작거나 같다.</p>

<p>다음 줄에는 배열에 들어있는 수의 개수 n이 주어진다. (0 ≤ n ≤ 100,000)</p>

<p>다음 줄에는 [x<sub>1</sub>,...,x<sub>n</sub>]과 같은 형태로 배열에 들어있는 정수가 주어진다. (1 ≤ x<sub>i</sub> ≤ 100)</p>

<p>전체 테스트 케이스에 주어지는 p의 길이의 합과 n의 합은 70만을 넘지 않는다.</p>

### 출력 

 <p>각 테스트 케이스에 대해서, 입력으로 주어진 정수 배열에 함수를 수행한 결과를 출력한다. 만약, 에러가 발생한 경우에는 error를 출력한다.</p>


## 문제 해결 아이디어

테스트 케이스 개수는 최대 10만개이기 때문에, read로 입력을 처리한다.   

R일때 뒤집고 D일 때 삭제하자!   

단순 pop으로 앞에 걸 제거하면 시간복잡도가 O(n)이기 때문에 deque로 popleft()를 사용할 것이다.   

## Input 반례 (해결 과정)

```python
import sys
import json
from collections import deque

input_data = sys.stdin.read().split()
n = int(input_data[0])  # 테스트 케이스 개수
op = []
numberOfInt = []
integer = []

for i in range(n):
    op.append(list(input_data[1 + (i * 3)]))  # 문자열을 리스트로 변환
    numberOfInt.append(int(input_data[2 + (i * 3)]))  # 정수 변환
    integer.append(deque(json.loads(input_data[3 + (i * 3)])))  # 문자열을 리스트로 변환 후 deque로 저장

    for j in op[i]:
        if j == "R":
            integer[i].reverse()
        else: # "D"
            if len(integer[i]) == 0:
                integer[i] = "error"
                break
            integer[i].popleft()
    print(list(integer[i])) 
```

예제는 정답이지만 시간 초과가 발생한다…    

1. 테스트 케이스의 최대 개수는 100개
2. 테스트 케이스 당 계산의 최대 개수는 100,000개
3. 테스트 케이스 당 수의 최대 개수 100,000개

reverse()의 시간복잡도가 O(n)이기 때문에 최대로 발생하는 시간복잡도는 100(1: 테스트 케이스 개수) * 100,000(2: 계산 개수) * 100,000(R일 때 수를 뒤집어야 함.)    

시간 제한은 1초인데, 1억번의 연산을 초과하게 된다.    

reverse를 최대한 줄여야 하는데…    

isReverse를 하여 가상으로 뒤집고, 뒤집혔을 때 D를 실행해야 하면 오른쪽을 삭제하고, 뒤집히지 않았을 때 D를 실행해야 하면 왼쪽을 삭제하도록 했다.    

```python
import sys
import json
from collections import deque

input_data = sys.stdin.read().split()
n = int(input_data[0])  # 테스트 케이스 개수
op = []  # 계산 개수
numberOfInt = []
integer = []
result = []

for i in range(n):
    op.append(list(input_data[1 + (i * 3)]))  # 문자열을 리스트로 변환
    numberOfInt.append(int(input_data[2 + (i * 3)]))  # 정수 변환
    integer.append(deque(json.loads(input_data[3 + (i * 3)])))  # 문자열을 리스트로 변환 후 deque로 저장
    isReverse = False
    for j in op[i]:
        if j == "R":
            isReverse = not isReverse
        else: # "D"
            if len(integer[i]) == 0:
                result.append("error")
                break
            if isReverse: 
                integer[i].pop()
            else:
                integer[i].popleft()
    if isReverse == True:
        integer[i] = deque(reversed(integer[i]))
    result.append(list(integer[i]))

for i in result:
    if len(i) > 0:
        print(i)
```

근데 왜 자꾸 16%에서 오류가 발생하는 것일까….   

게시판 글을 살펴보다가 아래 글을 보았다.    

[](https://www.acmicpc.net/board/view/157954)

출력 결과에 공백이 들어가고, 파이썬 특성으로 인해 그렇다는데, 이 이유로 이 분도 안 됐다고 한다…    

설마 나도 그럴까 하고, 공백을 제거하니 정답이었다…    

너무 허무… join 관련해서도 한 번 정리하면 좋을 것 같고… 요소들의 타입을 변환하는 방법도 다시 정리해야겠다…     

## 최종 코드

```python
import sys
import json
from collections import deque

input_data = sys.stdin.read().split()
n = int(input_data[0])  # 테스트 케이스 개수
op = []  # 계산 개수
numberOfInt = []
integer = []
result = []

for i in range(n):
    op.append(list(input_data[1 + (i * 3)]))  # 문자열을 리스트로 변환
    numberOfInt.append(int(input_data[2 + (i * 3)]))  # 정수 변환
    integer.append(deque(json.loads(input_data[3 + (i * 3)])))  # 문자열을 리스트로 변환 후 deque로 저장
    isReverse = False
    isError = False
    for j in op[i]:
        if j == "R":
            isReverse = not isReverse
        else: # "D"
            if len(integer[i]) == 0:
                result.append("error")
                isError = True
                break
            if isReverse:
                integer[i].pop()
            else:
                integer[i].popleft()
    if isError == True:
        continue
    if isReverse:
        integer[i].reverse() 
        
    # deque를 리스트로 변환한 후, 각 요소를 문자열로 변환하여 출력
    strlist = [str(i) for i in integer[i]]  # deque의 요소를 문자열로 변환
    result.append("[" + ",".join(strlist) + "]")  # 문자열을 합쳐서 출력 포맷에 맞춤

# 결과 출력
for res in result:
    print(res)
```
