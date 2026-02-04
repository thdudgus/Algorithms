# [Silver V] 수 정렬하기 2 - 2751 

[문제 링크](https://www.acmicpc.net/problem/2751) 

### 성능 요약

메모리: 142080 KB, 시간: 908 ms

### 분류

정렬

### 제출 일자

2026년 2월 4일 11:15:06

### 문제 설명

<p>N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.</p>

### 출력 

 <p>첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.</p>

## 문제 해결 아이디어

그냥 sort 쓰면 되지 않나..?

## Input 반례 (해결 과정)

```python
n = int(input())
num = []
for _ in range(n):
    num.append(int(input()))

num.sort()
for i in num:
    print(i)
```

음… 시간 초과이다. 왜일까?
일단 수의 개수는 100만 개이고, 정렬은 nlogn이라서 이게 이유는 아닐 것이다. 

for문이 문제인가 싶어서 리스트 컴프리헨션으로 바꿔봤는데 시간 초과다…

파이썬의 `input`, `print`는 시간복잡도가 어떻게 될까?

**1. `input()` vs `sys.stdin.readline()`** 

• **`input()`**: 입력을 받을 때마다 프롬프트 메시지를 처리하고 줄바꿈 문자를 제거하는 등 부가적인 작업을 수행하여 대량 입력 시 O(N)시간 내에 성능 저하가 발생할 수 있다.
• **`sys.stdin.readline()`**: 훨씬 빠른 입력을 제공하며, 반복문 내에서 수십만 개 이상의 데이터를 받을 때 유리.
• **팁**: `import sys; input = sys.stdin.readline`을 사용하여 `input()`을 대체하면 편리. 

**2. `print()` 시간 복잡도 및 최적화** 

• `print()` 함수는 호출될 때마다 개별적으로 화면에 출력하므로 비용이 든다.
• **속도 개선**: 대량 출력 시 `print()`를 반복 호출하는 대신, 결과를 리스트에 저장한 후 `' '.join()`으로 한 번에 출력하거나 `sys.stdout.write()`를 사용하면 시간 복잡도 내의 상수 요소를 줄여 더 빠르게 동작. 

**3. 시간 복잡도 요약** 

• 데이터 개수 N에 대해, 개별 입출력은 O(1)로 보일 수 있으나 대량 데이터를 처리할 때는 데이터의 길이 혹은 개수에 비례하는 O(N의 시간을 소요. 

## 최종 코드

```python
import sys
n = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for _ in range(n)]
num.sort()
for i in num:
    print(i)
```

`input`만 `stdin.readline`으로 바꾼 것보다 아래처럼 `print`까지 `stdout.write`으로 바꾼 게 약 1000ms나 시간이 줄어든다.

```sql
import sys
n = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for _ in range(n)]
num.sort()
sys.stdout.write('\n'.join(map(str, num)))
```
