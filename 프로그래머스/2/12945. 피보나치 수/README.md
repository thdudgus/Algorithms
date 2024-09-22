# [level 2] 피보나치 수 - 12945 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12945) 

### 성능 요약

메모리: 456 MB, 시간: 484.50 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 22일 20:50:38

### 문제 설명

<p>피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다. </p>

<p>예를들어 </p>

<ul>
<li>F(2) = F(0) + F(1) = 0 + 1 = 1</li>
<li>F(3) = F(1) + F(2) = 1 + 1 = 2</li>
<li>F(4) = F(2) + F(3) = 1 + 2 = 3</li>
<li>F(5) = F(3) + F(4) = 2 + 3 = 5</li>
</ul>

<p>와 같이 이어집니다.</p>

<p>2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.</p>

<h5>제한 사항</h5>

<ul>
<li>n은 2 이상 100,000 이하인 자연수입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>3</td>
<td>2</td>
</tr>
<tr>
<td>5</td>
<td>5</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>피보나치수는 0번째부터 0, 1, 1, 2, 3, 5, ... 와 같이 이어집니다.</p>

<h5>문제가 잘 안풀린다면😢</h5>

<p>힌트가 필요한가요? [코딩테스트 연습 힌트 모음집]으로 오세요! → <a href="https://school.programmers.co.kr/learn/courses/14743?itm_content=lesson12945" target="_blank" rel="noopener">클릭</a></p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

## 문제 해결 아이디어

 기존의 재귀 방법을 통해 피보나치 수를 구하는 것은 fib(n) = fib(n-1) + fib(n-2)이 반복되면서 중첩된 계산이 많이 발생하며, 시간 복잡도가 지수적으로 커지게 된다.     

따라서  fib(n) = fib(n-1) + fib(n-2)의 값을 저장하는 다른 배열을 만들어, 계산했던 피보나치 수는 저장해두고, 새로운 피보나치 수를 구할 때 이를 활용해보겠다.      

ib(n) = fib(n-1) + fib(n-2)의 값을 저장하는 배열 = f     

⇒ 바로 정답~~    

## 최종 코드

```python
def solution(n):
    f = []
    f.append(0)
    f.append(1)
    if n > 1:
        for i in range(n - 1):
            f.append(f[i] + f[i+1])
    return f.pop() % 1234567
```
