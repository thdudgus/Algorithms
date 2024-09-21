# [level 2] 최댓값과 최솟값 - 12939 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12939?language=python3) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.05 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 12일 18:14:38

### 문제 설명

<p>문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.<br>
예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.</p>

<h5>제한 조건</h5>

<ul>
<li>s에는 둘 이상의 정수가 공백으로 구분되어 있습니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>s</th>
<th style="text-align: center">return</th>
</tr>
</thead>
        <tbody><tr>
<td>"1 2 3 4"</td>
<td style="text-align: center">"1 4"</td>
</tr>
<tr>
<td>"-1 -2 -3 -4"</td>
<td style="text-align: center">"-4 -1"</td>
</tr>
<tr>
<td>"-1 -1"</td>
<td style="text-align: center">"-1 -1"</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
</br>

## 문제 해결 아이디어
파이썬을 처음 활용해보는 것이라 list의 내장 함수에 대해 알아보니, 최댓값을 구하는 max, 최솟값을 구하는 min이 있었다. 
   
또한 format() 함수를 사용하였다.   
format()함수는 문자열 중간 중간에 특정 변수의 값을 넣어주기 위해 사용하는 것이라고 한다.   
`‘{인덱스0}, {인덱스1}’.format(값0, 값1)`과 같이 사용하며, 값0과 값1이 각각 인덱스0, 인덱스1 자리에 들어가게 된다.   
⇒ `‘값0, 값1’`     
</br>

## Input 반례 (해결 과정)
```python
def solution(s):
s = list(map(int, input().split()))
answer = '{} {}'.format(min(s), max(s))
return answer 
```
위와 같이 작성했지만 EOF ERROR가 발생하였다.    
`EOFError`는 일반적으로 입력을 받을 때 더 이상 입력이 없을 경우 발생한다.    
위 코드에서 발생한 이유는 `input()` 함수를 사용할 때, 입력이 주어지지 않거나 코드가 실행되는 환경에서 입력을 받을 수 없는 상황일 때 생긴 것으로 보인다.      
코드를 보면 함수의 매개변수로 `s`를 받고 있음에도 불구하고, 함수 내부에서 `input()`을 호출하고 있다. 따라서 함수가 호출될 때 입력으로 받은 `s`를 사용하지 않고 다시 입력을 받으려 하면서 EOFError가 발생한 것이다.    
⇒ 프로그래머스를 처음 이용해보았는데, 입력에 이미 s로 주어져있는 상태였기 때문에 다시 입력을 받을 필요 없이 그걸 활용만 하면 된다.     
</br>

## 최종 코드

```python
def solution(s):
    s = list(map(int, s.split()))  # s를 직접 사용
    answer = '{} {}'.format(min(s), max(s))  # 문자열 포맷팅 수정
    return answer
```
