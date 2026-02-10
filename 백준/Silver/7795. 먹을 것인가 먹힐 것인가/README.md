# [Silver III] 먹을 것인가 먹힐 것인가 - 7795 

[문제 링크](https://www.acmicpc.net/problem/7795) 

### 성능 요약

메모리: 35668 KB, 시간: 248 ms

### 분류

정렬, 이분 탐색, 두 포인터

### 제출 일자

2026년 2월 11일 00:39:36

### 문제 설명

<p>심해에는 두 종류의 생명체 A와 B가 존재한다. A는 B를 먹는다. A는 자기보다 크기가 작은 먹이만 먹을 수 있다. 예를 들어, A의 크기가 {8, 1, 7, 3, 1}이고, B의 크기가 {3, 6, 1}인 경우에 A가 B를 먹을 수 있는 쌍의 개수는 7가지가 있다. 8-3, 8-6, 8-1, 7-3, 7-6, 7-1, 3-1.</p>

<p><img alt="" src="https://www.acmicpc.net/upload/images/ee(1).png" style="height:164px; width:209px"></p>

<p>두 생명체 A와 B의 크기가 주어졌을 때, A의 크기가 B보다 큰 쌍이 몇 개나 있는지 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 A의 수 N과 B의 수 M이 주어진다. 둘째 줄에는 A의 크기가 모두 주어지며, 셋째 줄에는 B의 크기가 모두 주어진다. 크기는 양의 정수이다. (1 ≤ N, M ≤ 20,000) </p>

### 출력 

 <p>각 테스트 케이스마다, A가 B보다 큰 쌍의 개수를 출력한다.</p>

## 문제 해결 아이디어

A의 개수는 N개 (1이상), B의 개수는 M개(20,000)이하로, A 크기 하나당 최대 20,000개의 크기를 검사해야하므로, 최대 N*20,000번이 반복되게 된다.

B를 정렬하고, A의 원소들을 target으로 한 후, B를 이분탐색하여 target과 같은 크기의 인덱스를 구한다.

만약 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12의 인덱스를 B가 가졌는데, target과 같은 수의 인덱스가 10이라면, len(B)-1-index가 그 개수이다.  

⇒ target보다 작은 것들 개수를 세야 하기 때문에 target과 같은 인덱스를 찾아서 해당 인덱스부터 끝 인덱스까지의 개수가 A1이 먹을 수 있는 B들의 개수이다.

## Input 반례 (해결 과정)

```python
import sys
n = int(sys.stdin.readline())

def comparison(start, end, target, bs):
    while start <= end:
        mid = (start + end) // 2 # a랑 똑같은 b가 있는 경우
        if bs[mid] == target:
            return mid # mid의 인덱스 값 반환. (mid 이전의 값들은 다 target보다 작음)
        elif bs[mid] < target:
            start = mid + 1
        else: 
            end = mid - 1
    if bs[mid] < target: # 같은 값이 없는 경우, target보다 작은 값들 중 가장 큰 값의 인덱스 반환
        return mid + 1
    else: 
        return 0

for _ in range(n):
    count = 0
    a, b = sys.stdin.readline().split()
    a_sizes = list(map(int, sys.stdin.readline().split()))
    b_sizes = list(map(int, sys.stdin.readline().split()))
    b_sizes.sort()
    for a_size in a_sizes:
        if a_size > b_sizes[-1]:
            count += len(b_sizes)
        elif a_size <= b_sizes[0]:
            continue
        else: count += comparison(0, len(b_sizes)-1, a_size, b_sizes)
    print(count)
```

이렇게 코드를 작성하여 예제 출력을 돌려보니 제대로 출력이 되었지만 25%에서 틀렸다고 나왔다. 그래서 질문 게시판에 있는 반례(나와 같이 25%에서 막힌) 입력을 넣어보아도 제대로 정답이 출력되었다.

```
1
5 5
2 3 4 5 6 
1 2 3 4 5

# 정답 15
```

이유가 뭔지 생각해보다가, target과 같은 bs[mid]가 가장 앞쪽 인덱스가 아닐 수 있다는 점이었다. (B들 중엔 중복이 존재하니까..!)   

따라서 개수를 세는 부분에서 Idx로 가장 앞쪽 인덱스를 세어, 그 인덱스를 기준으로 개수를 세도록 변경해보겠다.    

```python
import sys
n = int(sys.stdin.readline())

def comparison(start, end, target, bs):
    while start <= end:
        mid = (start + end) // 2 # a랑 똑같은 b가 있는 경우
        if bs[mid] == target:
            return bs.index(bs[mid]) # 같은 값이 있는 경우, 그 값의 인덱스 반환(index가 0부터 시작이라 자신 빼고 그대로 반환)
        elif bs[mid] < target:
            start = mid + 1
        else: 
            end = mid - 1
    if bs[mid] < target: # 같은 값이 없는 경우, target보다 작은 값들 중 가장 큰 값의 인덱스 반환 (index가 0부터 시작이라 +1하여 반환)
        return bs.index(bs[mid]) + 1
    else: 
        return 0

for _ in range(n):
    count = 0
    a, b = sys.stdin.readline().split()
    a_sizes = list(map(int, sys.stdin.readline().split()))
    b_sizes = list(map(int, sys.stdin.readline().split()))
    b_sizes.sort()
    for a_size in a_sizes:
        if a_size > b_sizes[-1]:
            count += len(b_sizes)
        elif a_size <= b_sizes[0]:
            continue
        else: count += comparison(0, len(b_sizes)-1, a_size, b_sizes)
    print(count)
```

같은 값이 없는 경우, target보다 작은 값들 중 가장 큰 값의 인덱스 반환 (index가 0부터 시작이라 +1하여 반환)   

위 경우에서 중복된 수가 몇개인지 모르니까 가장 처음 인덱스 + 해당 수 개수를 더해줘야 한다.   

`return bs.index(bs[mid]) + 1`대신 `return bs.index(bs[mid]) + bs.count(bs[mid])`

위 경우 답은 또 맞는데 제출하면 여전히 25%에 틀린다..   

근데 생각해보면, 이렇게 count랑 index를 넣으면 for문 안에 O(N)이 다시 들어가게 돼서 이분탐색을 사용한 의미가 사라지게 된다. (그리고 아마 target==bs[mid]도 target보다 작은 개수를 정확하게 보장하지 않을 것...?)   

<aside>
💡

comparison이 뭘 반환해야 하나.  

while이 끝난 뒤에 뭘 활용할지   

`==` 인 경우는 그냥 **안 세도 된다.** target보다 작은 원소의 개수 세기.   

</aside>

따라서 최종코드는 아래와 같다.   

### `bs[mid] < target`인 경우

mid 위치의 값이 target보다 작다. mid 포함해서 왼쪽은 전부 target보다 작음.   

⇒ 작은 값의 개수는 최소 mid+1개 이상이고, 더 오른쪽에 작은 값이 또 있는지 확인하러 탐색해봐야 함. (`start = mid + 1`)   

mid보다 작은 인덱스 부분은 무조건 target보다 작음.   

### `bs[mid] >= target`인 경우

mid 위치의 값이 target보다 같거나 크다. mid 위치의 값을 포함해서 오른쪽은 전부 더 크거나 같음.   

⇒ `end = mid-1`하여 왼쪽 부분을 탐색해봐야함. target과 같은 b_sizes의 값은 어차피 못 세니까, ≥로 처리한다.   

mid 보다 큰 인덱스 부분은 무조건 target보다 크거나 같음.    

### while이 끝나는 순간

start > end인 상태이다. target이 들어갈 수 있는 가장 왼쪽 위치이다.    

start 앞에 원소들은 모두 < target   

start부터 ≥ target이다.   

```python
[ < target ][   ][ >= target ]
	            ↑
	          start
	          end
```

start와 end가 같으면, 탐색이 한 번 남은 상태이다. stard와 end 기준으로 상태는 위와 같고, 여기서 mid도 start와 end와 같아진다. 이때 start=mid+1이 되거나 end=mid-1이 되면 해당 start가 target이 들어갈 수 있는 가장 왼쪽 자리가 된다.   

## 최종 코드

```python
import sys
n = int(sys.stdin.readline())

def comparison(start, end, target, bs):
    while start <= end:
        mid = (start + end) // 2
        if bs[mid] < target:
            start = mid + 1
        else: # bs[mid] == target인 경우엔 어차피 개수를 안 세기 때문에 같은 처리
            end = mid - 1
    return start

for _ in range(n):
    count = 0
    a, b = sys.stdin.readline().split()
    a_sizes = list(map(int, sys.stdin.readline().split()))
    b_sizes = list(map(int, sys.stdin.readline().split()))
    b_sizes.sort()
    for a_size in a_sizes:
        if a_size > b_sizes[-1]:
            count += len(b_sizes)
        elif a_size <= b_sizes[0]:
            continue
        else: count += comparison(0, len(b_sizes)-1, a_size, b_sizes)
    print(count)

```
