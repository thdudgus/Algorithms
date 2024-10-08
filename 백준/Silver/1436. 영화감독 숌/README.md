# [Silver V] 영화감독 숌 - 1436 

[문제 링크](https://www.acmicpc.net/problem/1436) 

### 성능 요약

메모리: 31252 KB, 시간: 832 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2024년 9월 22일 21:54:11

### 문제 설명

<p>666은 종말을 나타내는 수라고 한다. 따라서, 많은 블록버스터 영화에서는 666이 들어간 제목을 많이 사용한다. 영화감독 숌은 세상의 종말 이라는 시리즈 영화의 감독이다. 조지 루카스는 스타워즈를 만들 때, 스타워즈 1, 스타워즈 2, 스타워즈 3, 스타워즈 4, 스타워즈 5, 스타워즈 6과 같이 이름을 지었고, 피터 잭슨은 반지의 제왕을 만들 때, 반지의 제왕 1, 반지의 제왕 2, 반지의 제왕 3과 같이 영화 제목을 지었다. 하지만 숌은 자신이 조지 루카스와 피터 잭슨을 뛰어넘는다는 것을 보여주기 위해서 영화 제목을 좀 다르게 만들기로 했다.</p>

<p>종말의 수란 어떤 수에 6이 적어도 3개 이상 연속으로 들어가는 수를 말한다. 제일 작은 종말의 수는 666이고, 그 다음으로 큰 수는 1666, 2666, 3666, .... 이다. 따라서, 숌은 첫 번째 영화의 제목은 "세상의 종말 666", 두 번째 영화의 제목은 "세상의 종말 1666"와 같이 이름을 지을 것이다. 일반화해서 생각하면, N번째 영화의 제목은 세상의 종말 (N번째로 작은 종말의 수) 와 같다.</p>

<p>숌이 만든 N번째 영화의 제목에 들어간 수를 출력하는 프로그램을 작성하시오. 숌은 이 시리즈를 항상 차례대로 만들고, 다른 영화는 만들지 않는다.</p>

### 입력 

 <p>첫째 줄에 N이 주어진다. N은 10,000보다 작거나 같은 자연수이다.</p>

### 출력 

 <p>첫째 줄에 N번째 영화의 제목에 들어간 수를 출력한다.</p>


## 문제 해결 아이디어

N은 10,000보다 작거나 같은 자연수이다.   
O(N^2) 이하인 알고리즘을 사용하면 된다.   
</br>

처음엔 규칙을 찾으려고 n번째 영화의 제목을 쭉 써내려갔는데 규칙이랄 것이 없었다.    
따라서 그냥 처음부터 찾는 방식을 선택하기로 했다.     
</br>

제목을 알아내기 위해 변수 temp를 설정.    
temp를 1씩 증가시키면서,   
n과 count가 같아질때까지 반복.    
temp를 665부터 하나씩 증가시키면서 666을 포함하면 count 세기.    
포함하는 건 temp와 666을 string으로 변환하여 find()함수를 사용하여 처리.     

## Input 반례 (해결 과정)

```python
n = int(input())
count= 0
title = '666'
temp = 665
for i in range(1, ):
    if str(temp+i).find(title):
        count+=1
    if count == n:
        answer = temp+i
        break

print(answer)
```

위 코드에서 무한루프를 할 때 `for i in range(1, ):` 로 설정하였었는데, 이는 범위를 지정하지 않은 것이라서, 무한루프를 표현할 때는 while을 사용해야 한다.     
또한 **find()함수는 찾고자 하는 문자열이 있으면 해당 문자열의 인덱스를 반환하고, 없으면 `-1`을 반환한다.**    
따라서 if문에서의 조건에 ≠-1을 추가해야 한다.    
⇒ 최종 코드는 아래와 같다.     

## 최종 코드

```python
n = int(input())
count= 0
title = '666'
temp = 665
while True:
    temp +=1
    if str(temp).find(title) != -1:
        count+=1
    if count == n:
        answer = temp
        break
print(answer)
```

