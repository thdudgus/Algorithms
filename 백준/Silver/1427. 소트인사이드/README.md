# [Silver V] 소트인사이드 - 1427 

[문제 링크](https://www.acmicpc.net/problem/1427) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

문자열, 정렬

### 제출 일자

2026년 2월 4일 11:31:55

### 문제 설명

<p>배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.</p>

### 입력 

 <p>첫째 줄에 정렬하려고 하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.</p>

### 출력 

 <p>첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.</p>

## 문제 해결 아이디어

람다 식을 통해 정렬

key

1. 길이 순.
2. int끼리 더함.
3. 사전순

## Input 반례 (해결 과정)

```python
n = int(input()) 
words = [] 
for i in range(n): 
	words.append(list(input())) 
serial = [] for word in words: # str형인 숫자들을 int로 변환. 
serial.append([int(v) if v.isdigit() else v for v in word]) 

def int_sum(words): 
	return sum(int(c) for c in words if c.isdigit()) 
words.sort(key=lambda x: (len(x), int_sum(words))) 
print(words)
```

예제들이 계속 틀린다… 뭐가 문제일까 살펴보니,   

words를 리스트로 바꿔서 숫자들을 더하려고 했었다. 왜냐면 words에 있는 단어들 안에서 문자 하나씩 살펴봐야하기 때문에 리스트로 변환 했던 건데..    

굳이 그럴 필요 없이 정렬할 때 조건 `x`를 볼 때 어차피 단어가 하나씩 `int_sum`으로 넘어가면, 그 안에서 문자 하나씩 보면 되기 때문에, 그냥 `words = [input() for _ in range(n)]`이렇게 입력 받아서 int_sum에서 활용하면 된다.   

그리고 2번째 조건까지 같을 땐, 사전 순으로 정렬해줘야 하기 때문에 세번째 조건도 추가해주었다.   

```python
n = int(input())
words = [input() for _ in range(n)]

def int_sum(words):
    return sum(int(c) for c in words if c.isdigit())

words.sort(key=lambda x: (len(x), int_sum(words), x))
for w in words:
    print(w)
```

이렇게 해도 틀렸다.. 왜 그럴까 봤더니 람다식에서 int_sum으로 넘겨줄 때 x가 아니라 words를 넘겨주니까 조건이 제대로 작동하지 않았다… x로 변경해주니 정답…!

최종 코드는 아래와 같아.

## 최종 코드

```python
n = int(input())
words = [input() for _ in range(n)]

def int_sum(words):
    return sum(int(c) for c in words if c.isdigit())

words.sort(key=lambda x: (len(x), int_sum(x), x))
for w in words:
    print(w)
```
