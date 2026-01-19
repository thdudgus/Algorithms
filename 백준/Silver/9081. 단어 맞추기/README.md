# [Silver I] 단어 맞추기 - 9081 

[문제 링크](https://www.acmicpc.net/problem/9081) 

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

수학, 구현, 문자열, 조합론

### 제출 일자

2026년 1월 19일 20:12:28

### 문제 설명

<p>BEER라는 단어를 이루는 알파벳들로 만들 수 있는 단어들을 사전 순으로 정렬하게 되면</p>

<pre>BEER
BERE
BREE
EBER
EBRE
EEBR
EERB
ERBE
EREB
RBEE
REBE
REEB</pre>

<p>와 같이 된다. 이러한 순서에서 BEER 다음에 오는 단어는 BERE가 된다. 이와 같이 단어를 주면 그 단어를 이루는 알파벳들로 만들 수 있는 단어들을 사전 순으로 정렬할 때에 주어진 단어 다음에 나오는 단어를 찾는 프로그램을 작성하시오.</p>
⇒ 해당 알파벳으로 만들 수 있는 조합들에서 해당 알파벳 다음으로 나오는 단어를 출력하는 것.

### 입력 

 <p>입력의 첫 줄에는 테스트 케이스의 개수 T (1 ≤ T ≤ 10)가 주어진다. 각 테스트 케이스는 하나의 단어가 한 줄로 주어진다. 단어는 알파벳 A~Z 대문자로만 이루어지며 항상 공백이 없는 연속된 알파벳으로 이루어진다. 단어의 길이는 100을 넘지 않는다.</p>

### 출력 

 <p>각 테스트 케이스에 대해서 주어진 단어 바로 다음에 나타나는 단어를 한 줄에 하나씩 출력하시오. 만일 주어진 단어가 마지막 단어이라면 그냥 주어진 단어를 출력한다.</p>

## 문제 해결 아이디어

처음 들어오는 숫자 만큼 반복하여 실행한다.   
단어가 들어오면, 한 글자씩 분해하여 순열을 통해 단어 조합 리스트를 얻고, set을 통해 중복을 제거한다. 이를 sorting한 후, 찾는 단어 다음 순서의 단어를 출력한다.   


## Input 반례 (해결 과정)

```python
from itertools import permutations

n = int(input())
for i in range(n):
    w_input = input()
    word = list(w_input)
    tmp = set(permutations(w_input))
    tmp = [''.join(p) for p in tmp]
    tmp.sort()
    idx = tmp.index(w_input)
    if idx == len(tmp)-1:
        print(w_input)
    else:
        print(tmp[idx+1])
```

permutaion 연산이, 입력 문자열의 길이가 100일 때, 최대 O(100!)이 되기 때문에 시간 초과가 발생하는 것으로 보인다.   
이 경우엔 어떻게 하면좋을까…     
permutaition을 사용하지 않고, 사전 순서를 찾아야 한다.    

<aside>
💡

**[ 1단계: 바꿀 자리 찾기 ]**

숫자로 생각을 해보면, (1, 3, 5, 4, 2)로 예시를 들어보겠다. 이 다음 수는 (1, 4, 2, 3, 5)이다.   

여기서 더 큰 수를 만들겠다고 (1, 3, 5, 4, 2)에서 1과 3을 바꿔버리면, 갑자기 숫자가 확 커지게 된다.  ⇒ 맨 앞이 아니라 뒤에서부터 건드려야 바로 다음 사전순을 찾을 수 있다.    

2 → 4 → 5 순으로 수가 커지고 있는데, 갑자기 5에서 3으로 작아진다. (3<5)   

그리고 뒤에서부터 2, 4, 5는 이미 내림차순(1, 2, **5, 4, 2**)으로 가장 큰 조합이다. 여기서 사전순으로 다음 건 못 찾는다. 따라서 그 앞인 3을 바꿔줘야 한다. pivot!   

**[ 2단계: pivot과 바꿀 요소 찾기 ]**   
이제 pivot인 3 자리에 다른 숫자를 넣어야 하는데, 원래 있던 3보다 커야 다음 사전순(큰 수)이 된다. 대신 너무 큰 수가 아니라, 3보다 크면서 가장 작은 수를 뒤쪽인 5, 4, 2에서 찿아야 한다.   

2 < 3 ⇒ 2 탈락(사전 순이 더 앞쪽으로 가게 됨)   

5 or 4 > 3 ⇒ 5, 4 후보   

5 > 4 ⇒ 4 당첨 (5라면 사전 순이 바로 다음이 아닌 더 뒤쪽이 됨)   

**[ 3단계: pivot과 swap ]**   
찾은 3과 4를 swap   

**[ 4단계: pivot 뒤를 정리 ]**   
바꾼 위치 4의 뒤인 5, 3, 2를 보면 내림차순으로 되어있다. (큼→작음)   

앞 쪽을 기존보다 큰 걸로 바꿨으니까 뒤쪽을 가장 작게 바꿔주어야, 오름차순(작음→큼)으로 바꿔주어야 사전순으로 바로 다음이 된다.    

이미 내림차순은 건 reverse로 오름차순으로 바꿔준다.   

</aside>

#### 예제에 적용
(`E`>`H`>`L`>`O` 가 사전 순, 각 5, 8, 12, 15라고 편의상 부르겠다.)   

즉, `HELLO`(8, 5, 12, 12, 15)라면, `HELLO`다음의 사전순은  `HELOL`(8, 5, 12, 15, 12)이다.   

여기서 `HELLO` 다음의 사전순을 찾아야 하는데, 앞자리인 `H`(8)와 `O`(15)을 바꿔버리면 숫자가 갑자기 확 커지게 된다.    

⇒ 따라서 최대한 뒤쪽부터 건드려야 바로 다음 순열을 찾을 수 있다.   

`HELLO`(8, 5, 12, 12, 15)에서 뒤부터 읽어보면,  15→12→12 순으로 오름차순인데, 이 경우 앞까지 가지 않아도 뒤에서 바꿔도 가능하다.   

따라서 가장 뒤의 15와 12만 바꿔주면 된다. ⇒ `HELOL` (8, 5, 12, 15, 12)   

> [정리]
> 
> - "뒤에서부터 꺾이는 지점 찾기"
> - "그 값보다 큰 값 찾아서 바꾸기"
> - "뒷부분 뒤집기"

```python
n = int(input())

for i in range(n):
    w_input = input()
    word = list(w_input)
    tmp = ""
    for i in range(len(word)-1, 0, -1):
        if word[i-1] < word[i]: # 뒤에서 가장 큰 것 찾기
            tmp = word[i-1]
            pivot = i-1
            break
    for i in range(len(word)-1, 0, -1):
        if tmp <= word[i]: # swap: pivot 뒤쪽에 더 큰 거 찾아서 바꾸기
            word[pivot], word[i] = word[i], word[pivot]
            break
    # pivot 뒤쪽 reverse
    word[pivot:len(word)] = word[pivot:len(word)][::-1] 
    print(word)
```

분명 잘 구현한 것 같은데 예제가 틀린다…    

⇒ pivot은 빼고 reverse를 해야 하는데.. 포함해버렸다. 그리고 같으면 교환할 필요가 없어서 부등호에서 등호를 뺀다. 그리고 예외로 pivot을 못 찾은 경우도 있기 때문에 이 경우엔 그대로 출력해야 한다. (flag 추가)   

그리고 출력 형식에 맞게 join도 사용해야 한다.   

```python
n = int(input())

for i in range(n):
    w_input = input()
    word = list(w_input)
    tmp = ""
    flag = False
    for i in range(len(word)-1, 0, -1):
        if word[i-1] < word[i]: # 뒤에서 가장 큰 것 찾기
            tmp = word[i-1]
            pivot = i-1
            flag = True
            break
    for i in range(len(word)-1, 0, -1):
        if tmp < word[i]: # swap: pivot 뒤쪽에 더 큰 거 찾아서 바꾸기
            word[pivot], word[i] = word[i], word[pivot]
            break
    # pivot 뒤쪽 reverse
    if flag:
        word[pivot+1:len(word)] = word[pivot+1:len(word)][::-1] 
    print(''.join(word))
```

예제는 다 맞았는데 뭘까.. . 25%에서 틀린다.   

⇒ flag를 넣는 건 좋았지만, pivot이 있을 때만 swap과 reverse를 해야하기 때문에 reverse  쪽에만 flag를 넣을 게 아니라 swap과 reverse를 포함하여 if flag를 넣어야 한다.    
reverse에만 flag 조건을 주면, 억지로 두번째 for문이 실행되어 글자가 바뀔 수 있다. 예를 들어 pivot이 없어 flag가 false라면 tmp가 빈 문자열 상태가 되고, if tmp < word[i]: ("" < 'X')가 참이 되어 이상한 결과가 나올 수 있다.    
   
최종 코드는 아래와 같다. 겉인 `for i in range(n):`과 안쪽의 반복문이 같은 i 글자이기 때문에 바깥쪽을 k로 변경해주었다. 또한 pivot도 flag처럼 단어마다 초기화(0)되도록 해주었다.

## 최종 코드
```python
n = int(input())

for k in range(n):
    w_input = input()
    word = list(w_input)
    tmp = ""
    flag = False
    pivot = 0
    for i in range(len(word)-1, 0, -1):
        if word[i-1] < word[i]: # 뒤에서 가장 큰 것 찾기
            tmp = word[i-1]
            pivot = i-1
            flag = True
            break
    if flag: # pivot을 찾았을 때만 수행.
        for i in range(len(word)-1, 0, -1):
            if tmp < word[i]: # swap: pivot 뒤쪽에 더 큰 거 찾아서 바꾸기
                word[pivot], word[i] = word[i], word[pivot]
                break
        # pivot 뒤쪽 reverse
        word[pivot+1:] = word[pivot+1:][::-1] 
    print(''.join(word))
```
