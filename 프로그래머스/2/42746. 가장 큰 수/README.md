# [level 2] 가장 큰 수 - 42746 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42746) 

### 성능 요약

메모리: 27.2 MB, 시간: 1285.43 ms

### 구분

코딩테스트 연습 > 정렬

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 22일 16:44:20

### 문제 설명

<p>0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.</p>

<p>예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.</p>

<p>0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.</p>

<h5>제한 사항</h5>

<ul>
<li>numbers의 길이는 1 이상 100,000 이하입니다.</li>
<li>numbers의 원소는 0 이상 1,000 이하입니다.</li>
<li>정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>numbers</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>[6, 10, 2]</td>
<td>"6210"</td>
</tr>
<tr>
<td>[3, 30, 34, 5, 9]</td>
<td>"9534330"</td>
</tr>
</tbody>
      </table>
<hr>

<p>※ 공지 - 2021년 10월 20일 테스트케이스가 추가되었습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges


## 문제 해결 아이디어
numbers의 요소를 배치할 수 있는 순서의 개수는 len(numbers)!이다. len(numbers)를 n이라고 할 때, n!만큼 반복하면서, nPn을 하게 되면 각 배치를 모두 알 수 있다.     
이때의 배치 조합들을 모두 candidate 리스트에 넣고 max()함수를 이용해 가장 큰 값을 찾는다.    

## Input 반례 (해결 과정)

```python
import math
from itertools import permutations
def solution(numbers):
    numbers = list(map(str, numbers))
    n = len(numbers)
    candidate = []

    m = list(permutations(numbers, n))
    for i in range(math.factorial(n)):
        candidate.append(''.join(m[i]))
    candidate = list(map(int, candidate))
    answer = str(max(candidate))
    return answer
```

문제 정의의 예시 입출력은 통과하였는데, 제출해보니 테스트케이스1~11까지 시간초과가 발생하였다.     
numbers의 길이는 1이상 100,000으로 숫자의 개수가 최대 10만개라는 것이다. for문을 보면 n!번을 반복하기 때문에 최대 100,000!번 반복하게 된다. 매우 큰 숫자로 여기서 시간초과가 발생하는 것으로 보인다.     
위 방법이 아니라 각 numbers 요소에서 가장 높은 자릿수와 numbers의 요소를 key와 value로 딕셔너리를 만든다. 그 후에 key값을 기준으로 정렬한 후에, 다중 value인 key값만 알아내어, 순열로 재배치를 시도한 후 최대값을 구해보는 식으로 변경하려 한다.    

```python
from itertools import permutations
def solution(numbers):
    n = len(numbers)
    first = []
    d = {}

    for i in range(n): # 가장 높은 자리수 추출 및 딕셔너리 생성
        if numbers[i] < 1000: 
            if numbers[i] // 100 == 0: 
                if numbers[i] // 10 == 0: # n
                    first.append(numbers[i])
                else: # nn
                    first.append(numbers[i] // 10)
            else:  # nnn
                first.append(numbers[i] // 100)
        elif numbers[i] == 1000: # 1000
            first.append(1)
        d.setdefault(first[-1], []).append(numbers[i])

    sorted_d = dict(sorted(d.items(), reverse=True))  # 큰 수가 먼저 오도록 한 딕셔너리
    sorted_n = list(sorted_d.values())  # 리스트로 변환

    answer = []
    # value값이 여러개인 것들만 순서 조합
    for i in range(len(sorted_n)):
        candidate = []
        k_answer = sorted_n[i]
        if len(sorted_n[i]) > 1:  # value값이 여러개일 때
            m = list(permutations(sorted_n[i], len(sorted_n[i]))) # value값이 여러개인 것들 순서 조합 저장
            for i in range(len(m)):
                candidate.append(''.join(map(str, m[i])))  # 정수형을 문자열로 변환하여 결합
            candidate = list(map(int, candidate))
            k_answer = str(max(candidate))  # 가장 큰 조합을 문자열로 변환
        else:
            k_answer = ''.join(map(str, k_answer))  # 리스트에 하나의 숫자만 있을 때 처리
        answer.append(k_answer)

    # 최종적으로 리스트의 모든 문자열을 결합하여 반환
    return ''.join(answer)
```

처음엔 테스트케이스1~11까지 시간초과였는데 이번엔 줄긴 했다. 테스트케이스 1~6, 11만 시간초과이다.     
permutations에서 시간초과가 나는 것은 확실한 것 같은데 줄일 방법을 모르겠다.     
검색을 해보니 lambda를 활용하는 방법이 있었다.    

### lambda (람다)
함수를 한 줄로 표현 가능.    
```python
lambda 매개변수 : 표현식
```
```python
# 예시
def add(x, y):
    return x + y

# 위 함수를 아래와 같이 람다로 표현 가능.
add = lambda x, y: x + y
```

### 문자열 sort()
위 코드에서 문자열의 sort()기능을 이용하고 있지 않다. max()를 활용하기 위해 str에서 int로 변경하기도 했었다. 이 방법 대신 문자열의 sort()기능을 활용하여 문제를 풀고자 한다.       

`문자열의 sort()기능은 사전식으로 정렬`이 된다. 하지만 ‘가장 큰 수’문제의 리스트는 숫자를 표현한 문자열이다. 따라서 숫자도 사전식으로 정렬이 되기 때문에 자릿수가 다르면 “123”과 “45”가 있을 때 “45”가 더 큰 것으로 처리된다. 즉, 자리수가 다르면 크기 비교가 어려워진다.     
이에 각 문자열을 3번 반복하여 최대 12자리(최소공배수 : 4자리 숫자를 이어붙였을 때 최대 길이)의 문자열을 만든다. 입력 숫자는 최대 1000이므로 최대 4자리 숫자(1000)이기 때문에, 비교대상 문자열들의 길이가 같아져 문자열 비교를 통한 숫자의 조합 크기 비교를 정확하게 할 수 있다. (비교에 필요한 길이만큼의 문자열 확보가 가능해진다. 만약 입력 숫자가 더 큰 자리수까지 있다면, 문자열 반복 횟수를 그에 맞게 늘려야 한다.)    

예를 들어, “30”, “3”, “34”라면 사전식 정렬을 했을 때 “3”, ”30”, ”34”으로 정렬이 되고, 이를 오름차순으로 연결하면 “34303”이 되는데 실제론 34330이 더 크다. 그렇기에 3번 반복하여 “303030”, “333”, “343434”로 만든 후 sort()하면, “343434”, “333”, “303030”으로 정렬이 되고, 이 순서대로 원래 요소를 연결하면 “34330”으로 올바른 값이 나온다. 문자열은 한글자 한글자 아스키코드로 비교하기 때문에 각 요소의 맨 앞인 3을 비교하고, 그다음을 비교해야 하는데 “3”은 그다음 수가 없고, “34”와 “30”중에 하나가 올 수 있기 때문에 “3”*3을 해서 두번째에 3이 와도 무방하다. “30”과 “34”의 두번째 글자를 비교하여 정렬을 할 수 있고, “3”*3의 두번째 글자도 함께 비교하여 정렬할 수 있는 것이다.  **(맨 앞 수가 같은 두 숫자를 이어붙였을 때의 크기를 비교하는 것과 유사한 효과)**     

`⇒ 맨 앞 수가 같을 때, 그 숫자들끼리의 조합 중 가장 큰 것을 알 수 있음. (반복 필요 없음)`     

### 새로운 풀이 접근

numbers를 문자열 변경한 후, 위처럼 key값을 람다함수를 이용해 x*3으로 설정하여 내림차순으로 정렬한 후 join으로 이어준다.     
최종 반환 값은 문자열이어야 하는데, 예를 들어 “000”같이 모든 숫자가 0인 경우 “000”이 반환되면 안 되기 때문에, int로 한 번 변환해준 후 다시 문자열로 변환하여 반환한다.   

정답인 최종 코드는 아래에 첨부한다.    

## 최종 코드

```python
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)
    answer = ''.join(numbers)

    # 모든 숫자가 0인 경우 처리
    return str(int(answer))
```
