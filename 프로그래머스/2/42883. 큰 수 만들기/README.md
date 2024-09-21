# [level 2] 큰 수 만들기 - 42883 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42883) 

### 성능 요약

메모리: 16.9 MB, 시간: 114.54 ms

### 구분

코딩테스트 연습 > 탐욕법（Greedy）

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 21일 17:06:59

### 문제 설명

<p>어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.</p>

<p>예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.</p>

<p>문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.</p>

<h5>제한 조건</h5>

<ul>
<li>number는 2자리 이상, 1,000,000자리 이하인 숫자입니다.</li>
<li>k는 1 이상 <code>number의 자릿수</code> 미만인 자연수입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>number</th>
<th>k</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>"1924"</td>
<td>2</td>
<td>"94"</td>
</tr>
<tr>
<td>"1231234"</td>
<td>3</td>
<td>"3234"</td>
</tr>
<tr>
<td>"4177252841"</td>
<td>4</td>
<td>"775841"</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges


## 풀이 과정
첫번째, 두번째 고찰은 너무 길어 notion 참조. 이 두 방법으론 풀리지 않고, 새로운 방법이 떠오르지 않아 다른 사람의 풀이를 참고하여 문제의 힌트를 얻었다.   


- 다른 사람의 풀이 참고   
    stack을 이용하여 푸는 방법이 있다. 계속 풀었던 방식의 “앞 인덱스 요소가 뒤 인덱스 요소보다 작으면 삭제”와 비슷한 방법이다.    
    k>0인 동안 number를 순회하면서, number의 인덱스0부터 stack에 push한다.    
    `number[i]`를 push하기 전에, `stack`의 top 값이 `push하려는 값`보다 작으면 `stack`의 top을 pop하고, k-=1로 number에서 수를 삭제했음을 표현하는 것을 반복한다.   
    위 방식으로 number를 한 번 순회하고 그럼에도 k>0이라면, `stack`에서 k번 pop을 진행하여 top에 있는 수들을 삭제하고 k-=1을 하여 수를 삭제했음을 표현한다. 이를 k==0이 될때까지 반복한다. (stack에 push할 때, top보다 number의 값이 같거나 컸기 때문에 stack의 인덱스 앞쪽 수가 더 크다.)   
    
    ```python
    def solution(number, k):
        n = list(str(number))
        stack = []
        stack.append(n[0])
        i=0 
    
        while k > 0 and len(stack) != 0 and i <= len(n)-1:
            i+=1
            if stack[-1] < n[i]:
                stack.pop()
                k-=1
            else:
                stack.append(n[i])
    
        while k > 0:
            stack.pop()
            k-=1
            
        answer = ''.join(stack)
        return answer
    ```
    
    위 코드를 실행하니 처음 `stack.append(n[i])` 에서 인덱스 범위 오류가 발생한다.    
    위 코드에서 `i`가 `len(n)-1`보다 작거나 같을 때까지 반복하겠다고 했는데,  `i += 1`이 먼저 실행된 후 `n[i]`에 접근하기 때문에 `i`가 `len(n)`이 되어 `n[i]`에서 `IndexError`가 발생한다. 즉, 리스트의 마지막 요소보다 하나 더 큰 인덱스에 접근하려고 하기 때문에 에러가 발생한다.    
    따라서 아래와 같이 코드를 변경하였다.    
    
    ```python
    def solution(number, k):
        n = list(str(number))
        stack = []
        stack.append(n[0])
        i=1 
    
        while k > 0 and len(stack) != 0 and i <= len(n)-1:
            if stack[-1] < n[i]:
                stack.pop()
                k-=1
            else:
                stack.append(n[i])
            i+=1
    
        while k > 0:
            stack.pop()
            k-=1
            
        answer = ''.join(stack)
        return answer
    ```
    
    number의 첫 숫자를 push하고, i=1로 변경한 상태에서 i+=1의 위치를 반복문에 마지막에 넣어두었다. 인덱스 범위 오류는 사라졌지만, 빈 stack을 pop하는 문제가 발생하였다. 첫 while문에서 number[i]를 push하는 게 `stack[-1] < n[i]` 가 아닌 경우에만 발생하는데, `stack[-1] < n[i]` 인 stack의 top이 나올 때까지 찾아서 pop 해준 후 push를 해주어야, stack에 올바른 값이 담기게 된다. (그렇지 않으면 계속 풀었던 방식인 “앞 인덱스 요소가 뒤 인덱스 요소보다 작으면 삭제”와 다를 게 없음)     
    예를 들어, solution(1924, 2)인 경우, 처응 1이 push 되고 첫 while문에서 1이 pop된 후, while문의 `len(stack) != 0` 조건에 의해 빠져나오게 되고, 두번째 while문에서 k>0이기 대문에 빈 stack을 pop하게 되어 오류가 발생한다. (첫 while문이 끝나고도 stack엔 값이 없어서 두 번째 while문을 수정한다 해도 틀린 값 도출)     
    ⇒ `i += 1` 을 반복문 안에서 하지 말고, 루프 안에서 조건을 비교한 후에 증가시키는 방식으로 수정하고, 인덱스 값인 I가 len(n)을 넘지 않도록 한다.    
    그리고, `stack[-1] < n[i]` 인 stack의 top이 나올 때까지 찾아서 pop 해준 후 push를 해도록 수정한다. (단, 빈 stack을 pop하지 않게 한다.)    
    ⇒ 정답..!    
    아래는 최종코드이다.    
    

## 최종 코드

```python
def solution(number, k):
    n = list(str(number))
    stack = []
    
    for i in range(len(n)):
        while k > 0 and stack and stack[-1] < n[i]:
            stack.pop()
            k -= 1
        stack.append(n[i])

    if k > 0:
        stack = stack[:-k]
        
    answer = ''.join(stack)
    return answer
```
