# [level 2] 다음 큰 숫자 - 12911 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12911) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.02 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

정확성: 70.0<br/>효율성: 30.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 06일 15:15:49

### 문제 설명

<p>자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.</p>

<ul>
<li>조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.</li>
<li>조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.</li>
<li>조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.</li>
</ul>

<p>예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.</p>

<p>자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수를 완성해주세요.</p>

<h5>제한 사항</h5>

<ul>
<li>n은 1,000,000 이하의 자연수 입니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>78</td>
<td>83</td>
</tr>
<tr>
<td>15</td>
<td>23</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예#1<br>
문제 예시와 같습니다.<br>
입출력 예#2<br>
15(1111)의 다음 큰 숫자는 23(10111)입니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges


## 문제 해결 아이디어

n을 이진수로 반환한 후 1의 개수 세기   
n에서 1을 증가시키면서 bin()을 이용하여 이진수로 반환하여 1의 개수를 세고 n의 이진수 1 개수와 같으면 return.   

## Input 반례 (해결 과정)

### split()
split()함수는 문자열을 일정한 규칙으로 잘라서 리스트로 만들어주는 함수이다.    
`문자열.split(sep, maxsplit)`함수는 문자열을 maxsplit 번 만큼 sep의 구분자를 기준으로 문자열을 구분하여 잘라서 리스트를 만들어준다.    
sep 파라미터는 기본값이 none이고, 이때엔 공백을 기준으로 문자열을 자른다. 다른 기준으로 자르고 싶다면 ‘,’와 같이 쉼표를 기준으로 자를 수 있다.   
**예시**
`s : a b c d e f g      
s.split() : ['a', 'b', 'c', 'd', 'e', 'f', 'g']`

## 최종 코드

```python
def solution(n):
    b = list(bin(n)[2:])
    count = b.count('1')

    while 1:
        n += 1
        next = list(bin(n)[2:])
        if count == next.count('1'):
            break
    answer = n
    return answer
```
