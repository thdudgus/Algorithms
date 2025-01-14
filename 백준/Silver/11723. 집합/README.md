# [Silver V] 집합 - 11723 

[문제 링크](https://www.acmicpc.net/problem/11723) 

### 성능 요약

메모리: 32412 KB, 시간: 2556 ms

### 분류

비트마스킹, 구현

### 제출 일자

2025년 1월 14일 20:42:57

### 문제 설명

<p>비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.</p>

<ul>
	<li><code>add x</code>: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.</li>
	<li><code>remove x</code>: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.</li>
	<li><code>check x</code>: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)</li>
	<li><code>toggle x</code>: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)</li>
	<li><code>all</code>: S를 {1, 2, ..., 20} 으로 바꾼다.</li>
	<li><code>empty</code>: S를 공집합으로 바꾼다.</li>
</ul>

### 입력 

 <p>첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.</p>

<p>둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.</p>

### 출력 

 <p><code>check</code> 연산이 주어질때마다, 결과를 출력한다.</p>


 ## 문제 해결 아이디어

파이썬의 Set 자료형을 활용한다.

### Set

- 중복을 허용하지 않는다.
- 순서가 없다. (unorderd) ⇒ indexting 지원 x
- 평균적인 시간복잡도 = O(1)
    - 해시테이블로 구현되어 있어, 해당 값을 해시 함수에 넣어 인덱스에 접근하기 때문.

**집합 연산**

```python
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
s1 & s2
s1.intersection(s2)
# 결과: {4, 5, 6}

# 합집합
s1 | s2
s1.union(s2)
# 결과: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# 차집합
s1 - s2
s1.difference(s2)
# 결과: {1, 2, 3}
```

**값 추가 & 삭제**

```python
# 값 1개 추가
s1.add(4)

# 값 여러 개 추가
s1.update([4, 5, 6])

# 특정 값 제거
s1.remove(2)
```

**set의 in**

```python
>>> 2 in s1
False
```

## Input 반례 (해결 과정)

```python
m = int(input())    
s = set()
result = []

def addS(n):
    s.add(n)

def removeS(n):
    s.remove(n)

def checkS(n):
    if n in s:
        result.append(1)
        return
    result.append(0)

def toggleS(n):
    if n in s:
        removeS(n)
        return
    s.add(n)

def allS():
    s.clear()
    for i in range(20):
        s.add(i+1)

for m in range(m):
    operation = input().split()
    sl = len(s)
    if operation[0] == "add":
        addS(operation[1])
    if operation[0] == "remove":
        removeS(operation[1])
    if operation[0] == "check":
        checkS(operation[1])
    if operation[0] == "toggle":
        toggleS(operation[1])
    if operation[0] == "all":
        allS()
    if operation[0] == "empty":
        s.clear

for i in result:
    print(i)
```

`def removeS(n):`로 인해 런타임 에러가 발생하였다. set에서 존재하지 않는 요소를 제거하려 해서 생긴 오류이다. remove가 요소가 없을 땐 자동으로 실행을 안 하는 줄 알았는데, 이렇게 하기 위해선 `discard()` 를 사용해야 한다. 따라서 `s.discard(n)`으로 변경하면 `KeyError`가 사라진다.    

다만 여전히 시간초과이다.   

시간 제한은 1.5초로 약 1억 5천만 번의 연산이 가능하다.   

수행해야하는 연산의 범위는 1번에서 최대 3백만번으로 O(nlogn)이하의 알고리즘으로 설계해야 한다.   

set의 연산 자체들은 모두 O(1)이므로 다른 곳에서 시간을 줄일 방법을 찾아야 한다.    

문제에서 주어진 범위는 1부터 20까지로 매우 적다. set 대신 list를 사용해도 인덱스를 통한 접근은 O(1)로, 사용해도 괜찮다.   

⇒ set 대신 크기가 20인 list를 사용하고, 집합에 있으면 1, 없으면 0으로 인덱스로 관리한다. (ex. 2가 있으면 해당 인덱스의 요소가 1로, 없으면 0으로 관리)   

```python
import sys
input = sys.stdin.read
m = int(input().split()[0])  # 첫 번째 줄에서 m을 가져옴
commands = input().splitlines()[1:]  # 나머지 명령어들을 가져옴

s = [0] * 21  # 1부터 20까지의 집합 표현
result = []

for command in commands:
    parts = command.split()
    if len(parts) == 2:
        operation, num = parts[0], int(parts[1])
    else:
        operation = parts[0]

    if operation == "add":
        s[num] = 1
    elif operation == "remove":
        s[num] = 0
    elif operation == "check":
        result.append(1 if s[num] else 0)
    elif operation == "toggle":
        s[num] = 0 if s[num] else 1
    elif operation == "all":
        s = [1] * 21
    elif operation == "empty":
        s = [0] * 21

sys.stdout.write("\n".join(map(str, result)) + "\n")
```

그런데 또 메모리 초과…   

`sys.stdin.read()`는 **한 번에 모든 입력을 읽어들여서 입력 크기가 커 메모리 초과가 발생**하였다.   

⇒ `sys.stdin.readline()`을 사용하여 **한 줄씩 읽으면서 처리하도록 수정.**   

또한 **result에 매번 check의 결과를 추가하기 때문에 불필요한 메모리 사용이 크다.**    

⇒ `sys.stdout.write()`를 즉시 호출하여 결과를 출력 (입력 중간에 출력돼도 괜찮았던 건지 몰랐다… 무조건 입력 쭉~ 출력 쭉~ 출력돼야 하는 줄….)    

```python
import sys
input = sys.stdin.readline

s = [0] * 21  # 1부터 20까지의 집합 표현

m = int(input().strip())  # 명령어 개수 입력

for _ in range(m):
    command = input().strip().split()
    
    if len(command) == 2:
        operation, num = command[0], int(command[1])
    else:
        operation = command[0]

    if operation == "add":
        s[num] = 1
    elif operation == "remove":
        s[num] = 0
    elif operation == "check":
        sys.stdout.write("1\n" if s[num] else "0\n")
    elif operation == "toggle":
        s[num] = 0 if s[num] else 1
    elif operation == "all":
        s = [1] * 21
    elif operation == "empty":
        s = [0] * 21
```

- `sys.stdout.write()`는 `print()`보다 빠른 출력 방식

### 두 코드 비교

**📌 `sys.stdin.read` 사용 코드**

- **`sys.stdin.read()`**:
    - `input = sys.stdin.read`를 사용하면, 표준 입력의 전체를 한 번에 읽어온다**.**
    - **`input().split()`을 호출하여 첫 번째 줄에서 명령어 개수(m)를 추출. 이후 `splitlines()`를 이용해 나머지 명령어들을 리스트로 처리.**
    - `splitlines()`는 줄 단위로 나누어 리스트로 반환. 따라서 첫 번째 줄을 제외하고 나머지 명령어들을 **`commands` 리스트에 저장**.
    

**📌 `sys.stdin.readline` 사용**

- **`sys.stdin.readline()`**:
    - `input = sys.stdin.readline`을 사용하면, 각 줄을 한 번에 하나씩 읽어온다.
    - **`input().strip()`으로 각 줄의 앞뒤 공백을 제거한 후, `split()`을 통해 명령어와 숫자를 나눈다.**
    - 명령어가 두 개이면 두 번째 값(`num`)도 읽어서 처리하고, 하나일 경우 `operation`만 처리합니다.
- 입력 처리 방식:
    - 한 번에 한 줄씩 읽기 때문에 입력이 매우 많을 경우에는 여러 번의 입력/출력 작업이 일어나게 된다.
    - 이 방식은 입력을 한 번에 모두 읽지 않고, 반복문 안에서 하나씩 읽으며 처리하므로, 작은 입력에서는 큰 차이가 없지만 대량 입력에서는 조금 더 느릴 수 있다.

## 최종 코드

```python
import sys
input = sys.stdin.readline

s = [0] * 21  # 1부터 20까지의 집합 표현

m = int(input().strip())  # 명령어 개수 입력

for _ in range(m):
    command = input().strip().split()
    
    if len(command) == 2:
        operation, num = command[0], int(command[1])
    else:
        operation = command[0]

    if operation == "add":
        s[num] = 1
    elif operation == "remove":
        s[num] = 0
    elif operation == "check":
        sys.stdout.write("1\n" if s[num] else "0\n")
    elif operation == "toggle":
        s[num] = 0 if s[num] else 1
    elif operation == "all":
        s = [1] * 21
    elif operation == "empty":
        s = [0] * 21
```

