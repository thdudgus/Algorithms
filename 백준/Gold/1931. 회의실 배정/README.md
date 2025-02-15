<img width="649" alt="image" src="https://github.com/user-attachments/assets/974c1821-127b-4ace-adef-8d072f0ccf5a" /># [Gold V] 회의실 배정 - 1931 

[문제 링크](https://www.acmicpc.net/problem/1931) 

### 성능 요약

메모리: 54216 KB, 시간: 2792 ms

### 분류

그리디 알고리즘, 정렬

### 제출 일자

2025년 2월 16일 05:47:57

### 문제 설명

<p>한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.</p>

### 입력 

 <p>첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다. 시작 시간과 끝나는 시간은 2<sup>31</sup>-1보다 작거나 같은 자연수 또는 0이다.</p>

### 출력 

 <p>첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.</p>


## 문제 해결 아이디어

제한시간은 2초로 약 2억번의 계산이 가능하다.   

회의의 수가 10만개이기 때문에 O(nlogn) 정도의 알고리즘을 사용해야 한다.   
</br>

최대 개수의 회의를 배정해야 하기 때문에, 짧은 시간의 회의 별로 정렬한다.

~~정렬한 리스트의 회의부터 시작시간과 끝시간까지의 인덱스 값에 1을 더한다.~~ 

~~ex) 3 5면 인덱스 3, 4, 5에 1을 더한다.~~

~~만약 해당 인덱스의 값이 이미 1인 경우, flag를 Ture로 변경하고, 다음 인덱스도 겹친다면 해당 시간은 더하지 않고 빠져나온다.~~

~~겹치지 않고 더해진 회의라면 count를 1 올린다.~~

<aside>
💡

킥은 끝나는 시간 순으로 정렬하는 게 아니라 시작 시간 순으로 정렬하는 것이었다.

처음 내가 생각한대로 적은 시간이 걸리는 회의를 기준으로 정렬을 하는 것은 맞았다. 그러고 끝나는 시간이 아니라 시작하는 시간으로 정렬을 하면, 그 시작 시간부터 배치한 후 끝나는 시간을 last_end_time으로 저장한 후, 그 다음 시작 시간이 last_end_time보다 같거나 클 때 회의를 시작할 수 있는 것이다…

이렇게 되면 자동적으로 배치한 회의 다음 회의들은 회의들이 겹치는지 걱정할 필요가 없다..(어차피 이전 회의가 끝난 후 시작하게 되니…)

</aside>

## Input 반례 (해결 과정)

```python
n = int(input())
time = []
maxTime = 0
for i in range(n):
    time.append(list(map(int, input().split())))
    if maxTime < time[i][1]:
        maxTime = time[i][1]

time.sort(key=lambda x:(x[1]-x[0], x[0]))
table = [0]*(maxTime+1)

count = 0
for i in range(n): # 회의 마다
    flag = False
    next = False
    k = time[i][1] - time[i][0] + 1
    for j in range(k): # 회의의 시간 마다
        stime = time[i][0]+j
        if stime > len(table)-1: # 범위를 벗어났을 때
            break
        if table[stime] >= 1: # 이미 찬 시간일 때
            flag = True
            if stime+1 < len(table) and table[stime+1] >= 1: 
                next = True 
        if flag and next and j+1<k: 
            for b in range(j):
                table[stime-b-1] -=1
            count -= 1
            break
        table[stime] += 1
    count += 1
print(count)
```

예를 들어 0(0) 1(1) 1(2) 0(3) 1(4) 1(5)로 회의 시간이 차 있는 경우 2, 3, 4도 가능하다. 그러나 2, 3, 4, 5는 불가능하다. 따라서 next를 만들어서 현재 시간도 차있고(flag) 다음 시간도 차 있다면(next), 앞으로 반복문이 끝난다면 count를 세고, 끝나지 않는다면 count를 세지 않도록 했다.   

그러나 아래 예시에서    

```python
4
1 1
1 2
2 2
2 3
```

4가 나와야 하는데 3이 나왔다.   

디버깅 결과 1과 2는 1 1과 2 2로 인해 차있지만, 시작하자 마자 끝난 것이라 그 사이에 1 2가 들어갈 수 있기 때문이다.   

따라서 회의 시간이 2시간인 경우는 count를 세지 않는 것에서 제외하도록 하겠다.   

`if flag and next and j+1<k and k>2:` 로 변경하고, 4가 올바르게 나왔다.    

- 반례 확인용 예시
    
    ```python
    4
    1 4
    2 3
    3 5
    4 6
    2
    
    5
    1 5
    1 5
    1 5
    1 5
    1 5
    1
    
    6
    1 10
    2 3
    4 4
    4 5
    5 6
    7 8
    5
    
    6
    1 2
    2 3
    3 4
    4 5
    5 6
    6 7
    6
    
    5
    1 3
    3 5
    0 1
    5 7
    7 9
    5
    
    7
    1 4
    3 5
    0 6
    5 7
    3 8
    5 9
    6 10
    2
    
    2
    1 1
    2 2
    2
    
    3
    2 5
    3 4
    4 5
    2
    
    5
    1 3
    1 4
    4 4
    4 4
    4 5
    4
    
    5
    1 100
    2 3
    3 4
    4 5
    5 6
    4
    
    2
    2 3
    3 3
    2
    
    8
    1 3
    2 3
    3 3
    4 4
    5 5
    6 6
    7 7
    3 6
    6
    
    5
    1 100
    100 300
    99 101
    199 300
    199 201
    2
    
    4
    1 1
    1 2
    2 2
    2 3
    4
    
    29
    1 2
    2 3
    3 4
    4 5
    5 6
    6 7
    7 8
    8 9
    9 10
    10 11
    11 12
    12 13
    13 14
    14 15
    15 16
    16 17
    17 18
    18 19
    19 20
    20 21
    21 22
    22 23
    23 24
    24 25
    25 26
    26 27
    27 28
    28 29
    29 30
    29
    
    2
    1 1
    0 1
    2
    
    5
    0 3
    1 2
    2 5
    5 7
    7 10
    4
    
    4
    2 10
    1 2
    3 4
    4 5
    3
    
    1
    0 0
    1
    
    5
    1 10
    2 3
    4 5
    6 7
    8 9
    4
    
    4
    1 10
    2 5
    6 8
    9 12
    3
    
    2
    1 2
    1 1
    2
    ```
위 예시는 모두 정답을 도출했지만, 제출했을 때 계속 2%에서 틀렸다고 나온다… 정확한 이유를 찾기가 힘들어 알고리즘을 좀 더 간소화 해보겠다…   
</br>

⇒ 회의 시간 순 짧은 데로 정렬하고, 회의 시간이 같다면, 끝나는 시간이 짧도록 정렬한다. 만약 놓으려는 시간의 첫시간과 끝시간이 이미 있는 시간대들의 중간이라면 count하지 않는다. (+ 중간 시간도 확인)

```python
n = int(input())
time = []
maxTime = 0
for i in range(n):
    time.append(list(map(int, input().split())))
    if maxTime < time[i][1]:
        maxTime = time[i][1]

time.sort(key=lambda x:(x[1]-x[0], x[1]))
table = []
count = 0

for i in range(n): # 회의 마다
    flag = False
    k = time[i][1] - time[i][0] + 1
    if len(table) == 0:
        table.append(time[i])
        count += 1
    else:
        for j in range(len(table)):
            if (table[j][0] < time[i][0] < table[j][1]) or (table[j][0] < time[i][1] < table[j][1]) or table[j][0] < (time[i][0] + (k//2)) < table[j][1]:
                flag = True
                break
        if not flag:
            table.append(time[i])
            count += 1
print(count)
```
시간초과…   

for문이 두 번 있어서 그런 것 같다…   
</br>

for문을 어떻게 풀어야 하나 계속 고민했지만, 답이 나오지 않았고… 지피티 코드를 참고해보았다.    

<aside>
💡

킥은 끝나는 시간 순으로 정렬하는 게 아니라 시작 시간 순으로 정렬하는 것이었다.

처음 내가 생각한대로 적은 시간이 걸리는 회의를 기준으로 정렬을 하는 것은 맞았다. 그러고 끝나는 시간이 아니라 시작하는 시간으로 정렬을 하면, 그 시작 시간부터 배치한 후 끝나는 시간을 last_end_time으로 저장한 후, 그 다음 시작 시간이 last_end_time보다 같거나 클 때 회의를 시작할 수 있는 것이다…

이렇게 되면 자동적으로 배치한 회의 다음 회의들은 회의들이 겹치는지 걱정할 필요가 없다..(어차피 이전 회의가 끝난 후 시작하게 되니…)

</aside> 

문제 예제입력1에 대한 과정이다.    

<img width="649" alt="image" src="https://github.com/user-attachments/assets/b4e52b72-b1a1-494a-a6e3-f4a0009340f2" />


최종 코드는 아래와 같다.    

## 최종 코드

```python
n = int(input())
meetings = []  # 시간 정보 입력받기

for i in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

# 종료 시간 기준으로 회의 정렬 (끝나는 시간이 같을 경우 시작 시간이 빠른 순으로)
meetings.sort(key=lambda x: (x[1], x[0]))

last_end_time = 0  # 마지막 회의의 종료 시간
count = 0  # 선택한 회의 개수

# 회의가 지나가면서 가능한 회의를 선택
for start, end in meetings:
    if start >= last_end_time:
        count += 1
        last_end_time = end

# 결과 출력
print(count)
```
