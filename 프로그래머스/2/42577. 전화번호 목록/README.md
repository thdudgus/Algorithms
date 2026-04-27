# [level 2] 전화번호 목록 - 42577 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42577) 

### 성능 요약

메모리: 30.8 MB, 시간: 122.26 ms

### 구분

코딩테스트 연습 > 해시

### 채점결과

정확성: 83.3<br/>효율성: 16.7<br/>합계: 100.0 / 100.0

### 제출 일자

2026년 04월 27일 18:08:19

### 문제 설명

<p>전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.<br>
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.</p>

<ul>
<li>구조대 : 119</li>
<li>박준영 : 97 674 223</li>
<li>지영석 : 11 9552 4421</li>
</ul>

<p>전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.</p>

<h5>제한 사항</h5>

<ul>
<li>phone_book의 길이는 1 이상 1,000,000 이하입니다.

<ul>
<li>각 전화번호의 길이는 1 이상 20 이하입니다.</li>
<li>같은 전화번호가 중복해서 들어있지 않습니다.</li>
</ul></li>
</ul>

<h5>입출력 예제</h5>
<table class="table">
        <thead><tr>
<th>phone_book</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>["119", "97674223", "1195524421"]</td>
<td>false</td>
</tr>
<tr>
<td>["123","456","789"]</td>
<td>true</td>
</tr>
<tr>
<td>["12","123","1235","567","88"]</td>
<td>false</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1<br>
앞에서 설명한 예와 같습니다.</p>

<p>입출력 예 #2<br>
한 번호가 다른 번호의 접두사인 경우가 없으므로, 답은 true입니다.</p>

<p>입출력 예 #3<br>
첫 번째 전화번호, “12”가 두 번째 전화번호 “123”의 접두사입니다. 따라서 답은 false입니다.</p>

<hr>

## Input 반례 (해결 과정)

```python
# 전화번호를 담은 배열 phone_book
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false, 그렇지 않으면 true
import statistics
def solution(phone_book):
    phone_book.sort(key=lambda x: len(x), reverse=False)
    answer = True
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
	        if phone_book[i] in phone_book[j] and phone_book[j].index(phone_book[i]) == 0:
		        return False
    return answer
```

예제와 테스트 케이스 모두 맞지만 효율성 테스트에서 50%만 정답이었다… 

아마 for문이 2개 겹쳐져서 O(n^2)이 되었을 것이다. 

생각해봐도 어떻게 해야 시간복잡도를 해소할 수 있을지 감이 잘 안 잡혀서 `i`에 대한 반복문에서 `range`를 `phone_book` 개수의 반만 해보기도 했는데, 사실 딱 봐도 아니긴 하다.

정렬을 length 기준으로 하는 것이 아니라 사전 순으로 하면 가장 인접한 것에만 접두어가 있을 확률이 있다. 즉 ‘123’이면 사전 순으로 정렬했을 때, ‘1234’, ‘12348’ 순으로 정렬되기 때문에 바로 뒤 인덱스의 값과만 비교하면 된다. (만약 사전 순으로 정렬했을 때, ‘123’ 뒤에 ‘294’가 있다면 어차피 그 뒤는 당연히 접두어로 일치하지 않는다.)

그리고 index()는 일치하는 게 없다면 에러를 뱉기 때문에 `if phone_book[i] in phone_book[j] and phone_book[j].index(phone_book[i]) == 0:` 를 조건으로 걸었는데, `if phone_book[i+1].startswith(phone_book[i]):` 와 같이 사용할 수 있는 메서드가 있었다.. 

아래는 정답 코드이다.

## 최종 코드

```python
# 전화번호를 담은 배열 phone_book
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false, 그렇지 않으면 true
import statistics
def solution(phone_book):
    phone_book.sort()
    answer = True
    for i in range(len(phone_book)):
        if i+1 < len(phone_book):
            if phone_book[i+1].startswith(phone_book[i]):
                return False
    return answer
```

<p><strong>알림</strong></p>

<p>2021년 3월 4일, 테스트 케이스가 변경되었습니다. 이로 인해 이전에 통과하던 코드가 더 이상 통과하지 않을 수 있습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
