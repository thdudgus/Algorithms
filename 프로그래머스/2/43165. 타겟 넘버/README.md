# [level 2] 타겟 넘버 - 43165 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/43165) 

### 성능 요약

메모리: 58.1 MB, 시간: 694.02 ms

### 구분

코딩테스트 연습 > 깊이／너비 우선 탐색（DFS／BFS）

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 22일 02:28:28

### 문제 설명

<p>n개의 음이 아닌 정수들이 있습니다. 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.</p>
<div class="highlight"><pre class="codehilite"><code>-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
</code></pre></div>
<p>사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.</p>

<h5>제한사항</h5>

<ul>
<li>주어지는 숫자의 개수는 2개 이상 20개 이하입니다.</li>
<li>각 숫자는 1 이상 50 이하인 자연수입니다.</li>
<li>타겟 넘버는 1 이상 1000 이하인 자연수입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>numbers</th>
<th>target</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>[1, 1, 1, 1, 1]</td>
<td>3</td>
<td>5</td>
</tr>
<tr>
<td>[4, 1, 2, 1]</td>
<td>4</td>
<td>2</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p><strong>입출력 예 #1</strong></p>

<p>문제 예시와 같습니다.</p>

<p><strong>입출력 예 #2</strong></p>
<div class="highlight"><pre class="codehilite"><code>+4+1-2+1 = 4
+4-1+2-1 = 4
</code></pre></div>
<ul>
<li>총 2가지 방법이 있으므로, 2를 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges


## 문제 해결 아이디어
‘-’의 개수를 하나씩 늘려가면서 그 계산 결과가 target과 같다면 answer += 1     
‘-’가 1개일 땐 len(numbers)의 경우     
‘-’가 2개일 땐 len(numbers)_P_2     
n= len(numbers), k = ‘-’의 개수일 때 가능한 식의 조합은 n_P_k이다.   

k가 0보다 작아지기 전까지 반복하면서, k가 n-1개부터 1개일 때까지의 조합의 계산 결과를 도출하면서 answer를 센다.     

순열을 사용하기 위해
`from itertools import permutations` 에서 
`list(permutations(numbers, k))` 를 사용한다. 이렇게 뽑힌 숫자들은 더한 후 2배 하여 전체 합에서 빼주면, 뽑힌 숫자들만 뺄셈을 한 것과 같다.     

## Input 반례 (해결 과정)
해당 코드에서는 k를 i로 표현했다.    
```python
from itertools import permutations
def solution(numbers, target):
    numbers = list(map(int, numbers))
    n = len(numbers)
    total = 0
    answer = 0
    
    for i in range(1, n): # 뺄셈의 개수
        minus = list(permutations(numbers, i))
        for j in range(len(minus)):
            total = sum(numbers) - 2*sum(minus[j])
            if total == target:
                answer+=1

    return answer
```

두번째 테스트 케이스인 [4, 1, 2, 1], 4에선 2가 answer여야 하는데 3이 나왔다.    
이 경우엔 4-1+2-1과 4+1-2+1 밖에 없는데, 위 코드에선 뺄셈을 하는 -1과 -1의 조합을 두개를 다른 경우로 보는 코드이다. 그러나 문제는 두 개를 같은 경우로 취급하기에 생긴 문제이다. 따라서 순열 대신에 조합을 사용해보겠다. (조합을 사용하기 위해 from itertools import combinations 에서 list(combinations(numbers, i)) 를 사용한다.)     
⇒ 정답 !!! :)     

## 최종 코드

```python
from itertools import combinations
def solution(numbers, target):
    numbers = list(map(int, numbers))
    answer = 0
    
    for i in range(1, len(numbers)): # 뺄셈의 개수
        minus = list(combinations(numbers, i))
        for j in range(len(minus)):
            total = sum(numbers) - 2*sum(minus[j])
            if total == target:
                answer+=1

    return answer
```
