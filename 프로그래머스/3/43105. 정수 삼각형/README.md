# [level 3] 정수 삼각형 - 43105 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/43105) 

### 성능 요약

메모리: 14.6 MB, 시간: 39.92 ms

### 구분

코딩테스트 연습 > 동적계획법（Dynamic Programming）

### 채점결과

정확성: 64.3<br/>효율성: 35.7<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 11월 24일 22:20:14

### 문제 설명

<p><img src="https://grepp-programmers.s3.amazonaws.com/files/production/97ec02cc39/296a0863-a418-431d-9e8c-e57f7a9722ac.png" title="" alt="스크린샷 2018-09-14 오후 5.44.19.png"></p>

<p>위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다. 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.</p>

<p>삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.</p>

<h5>제한사항</h5>

<ul>
<li>삼각형의 높이는 1 이상 500 이하입니다.</li>
<li>삼각형을 이루고 있는 숫자는 0 이상 9,999 이하의 정수입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>triangle</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]</td>
<td>30</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges      

## 문제 해결 아이디어 

거쳐간 숫자를 저장할 list를 route라고 하여 저장한다.       

n번째 줄에서의 경우의 수는 [각 줄의 윗 요소의 개수*2]를 모두 곱한 수이다. 예를 들어 [7], [3, 8], [8, 1, 0], [2, 7, 4, 4]이면 1*(1*2)*(2*2)*(3*2)로 총 8개의 경우의 수가 있을 것이고, 일반항으로 생각하면 ∑(n*2^(n-1))이다. 이때 n이 1에서 500이하이므로 생각해야할 경우의 수가 약 2의 500제곱으로 지나치게 커지게 된다.     

따라서 거쳐간 숫자를 저장하는 DP가 효율적일 것으로 보인다.     

길이 맨 위 꼭짓점에서 두 갈래로 나뉘고, 그 아래에서 대각선 두 개 중 큰 것만 골라서 내려오기 때문에 결과적으로는 마지막에 두개의 경우가 남게 되고, 그 두개 중 큰 것이 answer가 된다. (처음에 둘 중에 고를 때 작은 쪽이 결과가 더 클 수 있다.)     

그리고 경로(index)를 route에 저장한다.     

route는 triangle의 두번째 요소들 2개가 지나온 triangle의 경로(tiangle의 행 idx)이다.     

입력 예시로 설명하면 route의 0번 행은 3부터 시작하는 경로, 1번 행은 8부터 시작하는 경로이다.      

route[0,0], route[0,1]은 0으로 초기화.     

route[1,0], route[1,1]은 triangle의 인덱스 0을 지나왔기 때문에 0으로 초기화.     

route [2, 0]은 위 요소 route[1, 0]의 값인 0을 가져와 triangle의 [2, 0(=route[1,0])]과 [2, 1]을 비교한다. 여기서 더 큰 값은 8이므로 triangle의 인덱스인 0을 route[2,0]에 저장한다. 그 다음 route[3,0]은 route[2,0]에 저장된 값을 가져와 triangle[3,0], [3,1]을 비교하고, 더 큰 값이 인덱스 값을 route[3,0]에 적는다.     

이렇게 route[4,0]까지 적으면 반복을 완료한다.     

최종적으로 route[4, 1]까지 채워졌으면 각 행에 담긴 인덱스 값들에 대한 triangle 값을 더해 더 큰 값을 answer로 반환한다.     

## Input 반례 (해결 과정)

```python
def solution(triangle):
    route = [[0, 0], [0, 1]]
    total1 = total2 = 0

    if (len(triangle) > 1):
        for i in range(2, len(triangle)):   
            preIdx = route[i-1][0]
            preIdx2 = route[i-1][1]
            route[i][0] = triangle.index(max(triangle[i][preIdx], triangle[i][preIdx+1]))
            route[i][1] = triangle.index(max(triangle[i][preIdx2], triangle[i][preIdx2+1]))
            
    for i in range(len(triangle)):
        total1 += triangle[route[i][0]]
        total2 += triangle[route[i][1]]

    return max(total1, total2)

# test
s = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
a = solution(s)
print(a) 
```

out of range 오류 발생.    

route 초기화는 [[0, 0], [0, 1]]만 존재하고, i=2 이상의 값에 대해 route[i]가 없으므로 route[i][0] 또는 [i][1]에 접근하려 해서 오류가 발생한 것으로 보인다.     

코드에서 route[i][0]과 [i][1]에 값을 할당하려면, 미리 route의 크기를 늘려두거나 `.append()` 를 사용해야 한다.      

```python
route.append([
              triangle.index(max(triangle[i][preIdx], triangle[i][preIdx+1])),
              triangle.index(max(triangle[i][preIdx2], triangle[i][preIdx2+1]))
                            ])
```

그러나 triangle에서 value error가 발생했다. preIdx가 len(triangle[i]-1)일 경우 preIdx+1은 범위를 초과하기 때문에 이와 관련하여 코드를 추가하여 수정하였다.     

```python
 nextIdx = preIdx + 1 if preIdx + 1 < len(triangle[i]) else preIdx
 nextIdx2 = preIdx2 + 1 if preIdx2 + 1 < len(triangle[i]) else preIdx2
```

아직도 value error가 발생하였는데 `triangle.index(max(triangle[i][preIdx], triangle[i][preIdx+1]))`처럼 2차원 list인데 행을 지정해주지 않고 인덱스를 반환하려 해서 오류가 발생했었다. 아래와 같이 수정하고 올바른 값이 도출되었다.      

```python
route.append([
              triangle[i].index(max(triangle[i][preIdx], triangle[i][nextIdx])),
              triangle[i].index(max(triangle[i][preIdx2], triangle[i][nextIdx2]))
                            ])
```

⇒ 2차원 list를 작성할 때는 같은 행으로 취급하는 부분을 추가할 때 [ ]로 묶자    
</br>

```python
def solution(triangle):
    route = [[0, 0], [0, 1]]
    total1 = total2 = 0

    for i in range(2, len(triangle)):   
        preIdx = route[i-1][0]
        preIdx2 = route[i-1][1]
        nextIdx = preIdx + 1 if preIdx + 1 < len(triangle[i]) else preIdx
        nextIdx2 = preIdx2 + 1 if preIdx2 + 1 < len(triangle[i]) else preIdx2

        route.append([
            triangle[i].index(max(triangle[i][preIdx], triangle[i][nextIdx])),
                        triangle[i].index(max(triangle[i][preIdx2], triangle[i][nextIdx2]))
                        ])
    for i in range(len(triangle)):
        total1 += triangle[i][route[i][0]]
        total2 += triangle[i][route[i][1]]        

    return max(total1, total2)

# test
s = [[7], [3, 8], [1, 2, 3], [5, 6, 7, 8], [9, 10, 12, 0, 1], [0, 2, 0, 5, 2, 7]]
a = solution(s)
print(a) 
```

예제 입력에 대한 출력은 맞았지만 제출하면 틀렸다고 한다… 왜지…    
</br>

⇒ 처음에 생각한 방식을 적용하면 된다.        

> 길이 맨 위 꼭짓점에서 두 갈래로 나뉘고, 그 아래에서 대각선 두 개 중 큰 것만 골라서 내려오기 때문에 결과적으로는 마지막에 두개의 경우가 남게 되고, 그 두개 중 큰 것이 answer가 된다. (처음에 둘 중에 고를 때 작은 쪽이 결과가 더 클 수 있다.)   
> 

라고 위에 적었었는데, 처음에 고를 때만 작은 쪽이 실제론 더 클 수 있다는 분석이 첫 줄 뿐 아니라 **삼각형 어디에서든 일어날 수 있다.**     

<aside>
💡

따라서 아래에서부터 큰 걸 찾아가자..!   

</aside>

triangle의 맨 아래는 더할 게 없으니 그 윗줄부터 계산한다.    

triangle[i][j] = triangle[i][j] + max(triangle[i+1][j], triangle[i+1][j+1])    
![SmartSelect_20241124_222406_Samsung Notes](https://github.com/user-attachments/assets/bb851fb0-479e-4398-902d-f398c4e6a20c)   

## 최종 코드
```python
def solution(triangle):
    for i in range(len(triangle) -2, -1, -1):
        for j in range (len(triangle[i])):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]
```
