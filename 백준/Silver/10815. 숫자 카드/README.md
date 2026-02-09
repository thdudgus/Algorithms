# [Silver V] 숫자 카드 - 10815 

[문제 링크](https://www.acmicpc.net/problem/10815) 

### 성능 요약

메모리: 111124 KB, 시간: 1992 ms

### 분류

자료 구조, 정렬, 이분 탐색, 집합과 맵, 해시를 사용한 집합과 맵

### 제출 일자

2026년 2월 9일 18:31:57

### 문제 설명

<p>숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다. 두 숫자 카드에 같은 수가 적혀있는 경우는 없다.</p>

<p>셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다</p>

### 출력 

 <p>첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 가지고 있으면 1을, 아니면 0을 공백으로 구분해 출력한다.</p>

## 문제 해결 아이디어

숫자의 범위가 -1천만부터 +1천만까지로 크고, 이 수들 사이에서 M이 있는지 없는지 찾아야하기 때문에 이분 탐색을 이용한다.    

또한, 입력도 input() 대신 readline()을 통해 수를 정리한다.    

## Input 반례 (해결 과정)

```python
import sys
n = int(sys.stdin.readline())
n_cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_cards = list(map(int, sys.stdin.readline().split()))
n_cards.sort()

def bi_search(start, end, target, cards):
    while start <= end:
        mid = (start + end) // 2
        if target == cards[mid]:
            return 1
        elif target > cards[mid]:
            start = mid + 1
        else: 
            end = mid - 1
    return 0

# n에 m이 있는지 탐색, target이 m
for m_card in m_cards: 
    print(**bi_search(0, len(n_cards), m_card, n_cards)**, end=' ')
```

예제는 정답인데 제출했더니 런타임에러가 발생하길래 왜인가 했더니, 함수를 호출하는 부분에서 `end` 인덱스 부분을 `len(n_cards)`로 넘겨주고 있기 때문이었다. ⇒ index 에러였던 것.    
 
이 부분을  `len(n_cards)-1`로 변경하니 정답이었다 !
