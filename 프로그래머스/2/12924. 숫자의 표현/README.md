# [level 2] 숫자의 표현 - 12924

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12924)

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

정확성: 75.0
효율성: 25.0
합계: 100.0 / 100.0

### 제출 일자

2024년 10월 03일 22:50:46

### **문제 설명**

Finn은 요즘 수학공부에 빠져 있습니다. 수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다. 예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.

- 1 + 2 + 3 + 4 + 5 = 15
- 4 + 5 + 6 = 15
- 7 + 8 = 15
- 15 = 15

자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.

**제한사항**

- n은 10,000 이하의 자연수 입니다.

**입출력 예 #1**

문제의 예시와 같습니다.

| n | result |
| --- | --- |
| 15 | 4 |

### 입출력 예 설명

입출력 예#1

문제의 예시와 같습니다.

<p>※ 공지 - 2022년 3월 11일 테스트케이스가 추가되었습니다.<\p>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
</br>

## 문제 해결 아이디어

연속된 자연수들로 n을 표현해야 함.   

n을 표현할 수 있는 연속된 자연수들의 개수는 절대 n/2를 넘지 못 함.    

중복된 자연수들로 이루어진 것이기 아니기 때문이다.   

따라서 n/2번 반복하면서 i개의 수 조합을 만들고, 조합이 n이 되는지와 조합이 연속된 자연수인지 판단(정렬했을 때 마지막 수는 가장 작은 수+길이-1여야 함.)하여 count를 센다.   

## Input 반례 (해결 과정)

```python
from itertools import combinations
def solution(n):
    count = 0
    arr = []
    for i in range(1, n+1):
        arr.append(i)
        
    for i in range(1, n//2):
        prob = list(combinations(arr, i))
        for j in prob:
            if j[0] + len(j)-1  == j[-1] :
                if  sum(j)==n:
                    count += 1
    answer = count
    return answer   
```

시간초과와 몇몇 테스트케이스에서 틀렸다.    

⇒ 모든 조합을 다 생성하는 게 아니라 i의 개수만큼 리스트를 슬라이싱하여 계산해보겠다.   

```python
def solution(n):
    count = 0
    arr = []
    arr.append(0)
    for i in range(1, n+1):
        arr.append(i)
        
    for i in range(1, n//2+2): # 자연수 개수
        for j in range(0, n+1):
            prob = arr[j+1:j+i+1]
            if len(prob) != i:
                    break
            if  sum(prob)==n:
                count += 1
                break
    answer = count
    return answer
```

조합을 만들지 않음으로써, 시간초과 없이 모든 테스트케이스를 통과할 수 있었다.    

그러나 효율성 테스트에서 시간초과로 실패했다.    
</br>

위 방식은   
 
1부터 n까지 하나일 때 합 계산     

1, 2/ 2, 3/ 3, 4/ … 두개일 때 합 계산   

1, 2, 3/ 2, 3, 4/ … 세개일 때 합 계산까지     

를 n//2번 반복하였다.   

이렇게 했을 때 중첩적으로 반복되는 부분이 많기 때문에1/ 1, 2/ 1, 2, 3/ 1, 2, 3, 4 ….     

2/ 2, 3/ 2, 3, 4/…. 와 같은 방법으로 코드를 변경하고 sum이 n을 넘으면 break하여 불필요한 반복을 없앴다.     

⇒ 정답..! 아래는 최종 코드이다.    

## 최종 코드
```python
def solution(n):
    count = 0
    arr = []
    arr.append(0)
    for i in range(1, n+1):
        arr.append(i)
        
    for i in range (1, n+1):
        for j in range(0, n//2+1):
            if i+j > n:
                break
            if sum(arr[i:i+j+1]) > n:
                break
            if sum(arr[i:i+j+1])==n:
                count+=1
                break
    answer = count
    return answer
```
