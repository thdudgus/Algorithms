# [Silver II] 나무 자르기 - 2805 

[문제 링크](https://www.acmicpc.net/problem/2805) 

### 성능 요약

메모리: 143532 KB, 시간: 2136 ms

### 분류

이분 탐색, 매개 변수 탐색

### 제출 일자

2025년 3월 23일 20:24:46

### 문제 설명

<p>상근이는 나무 M미터가 필요하다. 근처에 나무를 구입할 곳이 모두 망해버렸기 때문에, 정부에 벌목 허가를 요청했다. 정부는 상근이네 집 근처의 나무 한 줄에 대한 벌목 허가를 내주었고, 상근이는 새로 구입한 목재절단기를 이용해서 나무를 구할것이다.</p>

<p>목재절단기는 다음과 같이 동작한다. 먼저, 상근이는 절단기에 높이 H를 지정해야 한다. 높이를 지정하면 톱날이 땅으로부터 H미터 위로 올라간다. 그 다음, 한 줄에 연속해있는 나무를 모두 절단해버린다. 따라서, 높이가 H보다 큰 나무는 H 위의 부분이 잘릴 것이고, 낮은 나무는 잘리지 않을 것이다. 예를 들어, 한 줄에 연속해있는 나무의 높이가 20, 15, 10, 17이라고 하자. 상근이가 높이를 15로 지정했다면, 나무를 자른 뒤의 높이는 15, 15, 10, 15가 될 것이고, 상근이는 길이가 5인 나무와 2인 나무를 들고 집에 갈 것이다. (총 7미터를 집에 들고 간다) 절단기에 설정할 수 있는 높이는 양의 정수 또는 0이다.</p>

<p>상근이는 환경에 매우 관심이 많기 때문에, 나무를 필요한 만큼만 집으로 가져가려고 한다. 이때, 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M이 주어진다. (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)</p>

<p>둘째 줄에는 나무의 높이가 주어진다. 나무의 높이의 합은 항상 M보다 크거나 같기 때문에, 상근이는 집에 필요한 나무를 항상 가져갈 수 있다. 높이는 1,000,000,000보다 작거나 같은 양의 정수 또는 0이다.</p>

### 출력 

 <p>적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.</p>



## 문제 해결 아이디어

1. 입력받은 나무 높이들 중 평균 값을 H로 임시 설정 (m)
2. 잘린 나무들의 합(total)으로 M미터 이상을 가져갈 수 있는지 확인.
    
    total ≥ M ⇒ H(m) 늘리기 (H를 늘려 total을 줄일 수 있음 - 너무 많이 자름)
    
    total < M ⇒ H(m) 줄이기 (H를 줄여 total을 늘릴 수 있음 - 너무 적게 자름)
    
    1. 너무 적게 자른 경우(H를 줄이는 경우)라면, total ≥ M이 되는 경우 pass를 true로 변경.
    2. 너무 많이 자른 경우(H를 늘리는 경우)라면, total<M이 되는 경우 pss를 true로 변경.
    

## Input 반례 (해결 과정)

### 코드

```python
tmp = list(map(int, input().split()))
n = tmp[0]
m = tmp[1]
trees = list(map(int, input().split()))
trees.sort()
h = trees[n//2]

def lessTree(h):
    while True:
        h+=1
        total = sum(tree - h for tree in trees if tree > h)
        if total <= m:
            return h-1
def moreTree(h):
    while True:
        h-=1
        total = sum(tree - h for tree in trees if tree > h)
        if total >= m:
            return 0 if h < 0 else h

total = sum(tree - h for tree in trees if tree > h)
if total > m:  # 너무 많이 잘라서 h를 늘려 total(가져가는 나무)을 줄여야 함.
    answer = lessTree(h)
elif total == m:
    answer = h
else: # 너무 적게 잘라 h를 줄여 total(가져가는 나무)을 늘려야 함.
    answer = moreTree(h)

print(answer)
```

1. **input :**
    
    ```
    5 2
    50 51 100 101 102
    ```
    
    **answer :** 100
    ⇒ 100이 정답인데 101이 나옴…    
    
    `lessTree` 함수에서 조건으로 `total <= m`을 사용해버려서, wood가 목표치보다 모자란 경우에도 h를 증가시켜버리는 문제가 있어서, total <= m:인 경우 h를 -1 하려 return하였다.    
    
    해당 반례를 해결하였지만… 시간초과가 발생하였다.   
    
    위 코드에선 h 값을 1씩 변경하면서 매번 모든 나무에 대해 잘려나가는 길이의 총합을 계산한다. 이 과정은 각 반복마다 모든 나무를 순회하므로 O(n)의 시간이 소요되며, h의 조정 범위가 넓을 경우 반복 횟수가 많아져서 전체 알고리즘의 시간 복잡도가 매우 커진다.    
    
    <aside>
    💡
    
    따라서 이진탐색을 이용해 h 값을 빠르게 좁혀가는 방식으로 최적화할 필요가 있다.
    
    </aside>
    
    > 이진탐색이 어떻게 m을 만족하는 최대 h를 보장할 수 있는가?   
    > 
    
    나무를 자르는 높이 h와 잘려나가는 총 나무의 양 total 사이에 단조 감소(monotonic decreasing)  성질이 있기 때문이다.   
    
    monotonic decreasing(단조 감소)    
    
    - 낮은 h
        - h가 낮을수록, 각 나무에서 잘려나가는 양이 커지므로, total은 크게 나온다.
    - 높은 h
        - h가 높을수록, 각 나무에서 잘려나가는 양이 작아져, total은 작게 나온다.
    
    즉 h가 증가하면 total은 점점 작아지는 단조 감소 함수를 이루게 된다.
    
    ### 이진 탐색의 작동 방식
    
    1. 탐색 범위 설정
        
        h의 가능한 최솟값은 0, 가능한 최댓값은 나무들 중 가장 큰 값
        
    2. 중간값 선택
        
        mid = (low+hign) // 2
        
    3. 조건 평가
        1. 만약 total(mid)≥m이라면, 이는 h=mid로 자르면 m 이상의 나무를 얻을 수 있다는 의미
        2. 하지만 문제에서는 최대 h를 원하므로, **더 높은 h에서도 조건을 만족할 가능성이 있는지 확인하기 위해 h를 증가시켜 low를 mid + 1로 조정**
        3. 반대로 total(mid)<m이라면 h가 너무 높아서 조건을 만족하지 못하는 것이므로, h를 낮추기 위해 high를 mid-1로 조정한다.
    4. 결과 
        
        이 과정이 종료되면, high에는 total(high) ≥ m을 만족하면서 가능한 h 중 최대값이 남게 된다.   
        
        (결국 low가 조건을 만족하지 않는 구간으로 넘어가기 전에 high가 조건을 만족하는 마지막 h가 된다.)    
            
    

## 최종 코드

```python
tmp = list(map(int, input().split()))
n = tmp[0]
m = tmp[1]
trees = list(map(int, input().split()))

low = 0
high = max(trees)
result = 0 # m을 만족하는 최대 h

while low <= high:
    mid = (low + high) // 2
    total = sum(tree - mid for tree in trees if tree > mid)
    if total >= m:
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)

```

