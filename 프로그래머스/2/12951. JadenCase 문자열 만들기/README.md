# [level 2] JadenCase 문자열 만들기 - 12951 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12951?language=cpp) 

### 성능 요약

메모리: 4.21 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 25일 01:36:28

### 문제 설명

<p>JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)<br>
문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.</p>

<h5>제한 조건</h5>

<ul>
<li>s는 길이 1 이상 200 이하인 문자열입니다.</li>
<li>s는 알파벳과 숫자, 공백문자(" ")로 이루어져 있습니다.

<ul>
<li>숫자는 단어의 첫 문자로만 나옵니다.</li>
<li>숫자로만 이루어진 단어는 없습니다.</li>
<li>공백문자가 연속해서 나올 수 있습니다.</li>
</ul></li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>s</th>
<th style="text-align: center">return</th>
</tr>
</thead>
        <tbody><tr>
<td>"3people unFollowed me"</td>
<td style="text-align: center">"3people Unfollowed Me"</td>
</tr>
<tr>
<td>"for the last week"</td>
<td style="text-align: center">"For The Last Week"</td>
</tr>
</tbody>
      </table>
<hr>

<p>※ 공지 - 2022년 1월 14일 제한 조건과 테스트 케이스가 추가되었습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges


## 문제 해결 아이디어

받은 문자열을 split()으로 공백을 기준으로 나눈 뒤, 첫 인덱스가 숫자면 그 단어는 모두 소문자로 바꾸고, 숫자가 아니면 title()함수를 사용하여 첫글자만 대문자로 바꿔준다.    

## Input 반례 (해결 과정)

```python
def solution(s):
    str = s.split()
    answer = []
    
    for i in str:
        if i[0].isdigit():
             answer.append(i.lower())
        else:
            answer.append(i.title())
    answer = ' '.join(answer)
    return answer
```

입력이 "for the what  1what”인 경우 what과 1what 사이의 공백 2개가 1개로 줄어드는 바람에 틀린다는 것을 알게 되었다.     
⇒ split()을 사용하는 게 아니라, 모든 문자열을 소문자로 바꾸고, 공백 다음에 알파벳은 대문자로 변환하고, 공백 다음에 숫자가 오면 그냥 넘어가도록 변경하기로 했다.    
c++로 언어를 변경하였다.    
`tolower()` 과 `toupper()`는 문자열 전체가 아니라 단일 문자에만 적용되는 함수이다. 또한 변환된 결과가 저장되려면 함수만 호출하지 말고 결과를 다른 문자열에 저장해주어야 한다.     
아래는 최종 코드이다.     

## 최종 코드

```cpp
#include <string>
#include <cctype> 

using namespace std;

string solution(string s) {
    bool capitalize = true;  // 단어의 시작을 알리는 플래그
    bool digit = false; // 숫자인가?
    
    for (int i = 0; i < s.length(); i++) 
        s[i] = tolower(s[i]);
    
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == ' ') {
            capitalize = true;  // 공백 판별
                    } 
        else if (capitalize && isdigit(s[i])) {  // 공백 다음에 숫자면 
            capitalize = false;  // 대문자로 x
        }
        else if (capitalize && isalpha(s[i])) { // 공백 다음이면 
            s[i] = toupper(s[i]);  // 대문자로
            capitalize = false;
            }
        else {
            s[i] = tolower(s[i]);  // 그 외의 경우는 소문자로 유지
        }
    }
    return s;
}

```
