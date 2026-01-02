# [Silver IV] 균형잡힌 세상 - 4949 

[문제 링크](https://www.acmicpc.net/problem/4949) 

### 성능 요약

메모리: 33432 KB, 시간: 144 ms

### 분류

자료 구조, 문자열, 스택

### 제출 일자

2026년 1월 2일 15:12:13

### 문제 설명

<p>세계는 균형이 잘 잡혀있어야 한다. 양과 음, 빛과 어둠 그리고 왼쪽 괄호와 오른쪽 괄호처럼 말이다.</p>

<p>정민이의 임무는 어떤 문자열이 주어졌을 때, 괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램을 짜는 것이다.</p>

<p>문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고, 문자열이 균형을 이루는 조건은 아래와 같다.</p>

<ul>
	<li>모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.</li>
	<li>모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.</li>
	<li>모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.</li>
	<li>모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.</li>
	<li>짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.</li>
</ul>

<p>정민이를 도와 문자열이 주어졌을 때 균형잡힌 문자열인지 아닌지를 판단해보자.</p>

### 입력 

 <p>각 문자열은 마지막 글자를 제외하고 영문 알파벳, 공백, 소괄호("( )"), 대괄호("[ ]")로 이루어져 있으며, 온점(".")으로 끝나고, 길이는 100글자보다 작거나 같다.</p>

<div>입력의 종료조건으로 맨 마지막에 온점 하나(".")가 들어온다.</div>

### 출력 

 <p>각 줄마다 해당 문자열이 균형을 이루고 있으면 "yes"를, 아니면 "no"를 출력한다.</p>


### 문제 해결 아이디어
괄호를 여는 (나 [가 들어오면 스택에 push한다. 그리고 닫는 괄호가 들어왔을 때, 같은 종류의 여는 괄호일 때만 pop한다.

### Input 반례 (해결 과정)

```python
import sys

lines = []
while True:
    s = input().strip()
    lines.append(s)
    if s == ".":
        break   

s = []
for x in lines:
    for y in x:
        if y == "(" or y == "[":
            s.append(y)
        if y == ")":
            if len(s) > 0 and s[-1] == "(":
                s.pop()
        if y == "]":
            if len(s) > 0 and s[-1] == "[":
                s.pop()
    
    print("yes" if len(s) == 0 else "no")
    s.clear()
```

해당 코드는 예제에선 잘 동작했지만, [))))]과 같은 경우에 no가 아닌 yes를 출력하는 반례를 만들어냈다.    

이 경우에 )를 만났을 때 그냥 push 해버리면 될 것 같다. 어차피 false문자열인 경우이니까.    

그리고 “.”인 경우만 입력을 종료하는 조건이라서 입력 로직도 수정하였다.    

```python
import sys

lines = []
while True:
    s = input()
    if s == ".":
        break 
    lines.append(s)

for x in lines:
    for y in x:
        if y == "(" or y == "[":
            s.append(y)
        if y == ")":
            if len(s) > 0 and s[-1] == "(":
                s.pop()
            elif len(s) > 0 and s[-1] != "(":
                s.append(y)
        if y == "]":
            if len(s) > 0 and s[-1] == "[":
                s.pop()
            elif len(s) > 0 and s[-1] != "[]":
                s.append(y)
    print("yes" if len(s) == 0 else "no")
    s.clear()
```

이것도 10% 대에서 틀린다….   

]]]처럼 닫는 괄호인데 스택이 비어있는 경우는 처리가 안 되고, 이미 틀린 상태도 계속 검사하는 비효율성이 있다.   

 해당 사항을 고친 최종 정답 코드는 아래와 같다.   

### 최종 코드
```python
import sys

lines = []
while True:
    s = input()
    if s == ".":
        break 
    lines.append(s)
s = []

for x in lines:
    for y in x:
        if y == "(" or y == "[":
            s.append(y)
        if y == ")":
            if len(s) == 0: 
                s.append(y)
                break
            elif s[-1] == "(":
                s.pop()
            elif s[-1] != "(":
                s.append(y)
                break
        if y == "]":
            if len(s) == 0:
                s.append(y)
                break
            elif s[-1] == "[":
                s.pop()
            elif s[-1] != "[":
                s.append(y)
                break
    print("yes" if len(s) == 0 else "no")
    s.clear()
```
