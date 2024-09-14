# [level 2] 올바른 괄호 - 12909 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12909?language=python3) 

### 성능 요약

메모리: 11.2 MB, 시간: 13.71 ms

### 구분

코딩테스트 연습 > 스택／큐

### 채점결과

정확성: 69.5<br/>효율성: 30.5<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 15일 02:40:05

### 문제 설명

<p>괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어</p>

<ul>
<li>"()()" 또는 "(())()" 는 올바른 괄호입니다.</li>
<li>")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.</li>
</ul>

<p>'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.</p>

<h5>제한사항</h5>

<ul>
<li>문자열 s의 길이 : 100,000 이하의 자연수</li>
<li>문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>s</th>
<th>answer</th>
</tr>
</thead>
        <tbody><tr>
<td>"()()"</td>
<td>true</td>
</tr>
<tr>
<td>"(())()"</td>
<td>true</td>
</tr>
<tr>
<td>")()("</td>
<td>false</td>
</tr>
<tr>
<td>"(()("</td>
<td>false</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1,2,3,4<br>
문제의 예시와 같습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges


## 문제 해결 아이디어
파이썬의 list를 활용하여 문자열의 괄호를 하나하나 분리하여 list로 저장한다.   
스택을 활용하여 ‘(’가 나오면 push, ‘)’가 나오면 pop을 진행한다.    
반복은 list의 길이만큼 반복한다.   
스택이 비어있는데 ‘)’가 나오면 바로 False를 반환하고, 반복이 끝났음에도 스택에 ‘(’가 남아있다면 False를 반환한다. 반복이 끝난 후 스택이 비어있는 경우 True를 반환한다.   
</br>

## 최종 코드
```python
# s= "()()"

def solution(s):
    parent_list = list(s)
    stack=[]
    for i in range(0, len(parent_list)):
        if parent_list[i]=='(':
            stack.append('('). 
        elif parent_list[i]==')':
            if len(stack)!=0:
                stack.pop(). 
            else:
                return False
    if len(stack) != 0:
        return False
        
    return True

# answer=solution(s)
# print(answer)

```
