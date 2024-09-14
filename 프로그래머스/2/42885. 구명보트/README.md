# [level 2] 구명보트 - 42885 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42885) 

### 성능 요약

메모리: 4.67 MB, 시간: 1.78 ms

### 구분

코딩테스트 연습 > 탐욕법（Greedy）

### 채점결과

정확성: 81.5<br/>효율성: 18.5<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 15일 01:47:56

### 문제 설명

<p>무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 <strong>2명</strong>씩 밖에 탈 수 없고, 무게 제한도 있습니다.</p>

<p>예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.</p>

<p>구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.</p>

<p>사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.</p>

<h5>제한사항</h5>

<ul>
<li>무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.</li>
<li>각 사람의 몸무게는 40kg 이상 240kg 이하입니다.</li>
<li>구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.</li>
<li>구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>people</th>
<th>limit</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>[70, 50, 80, 50]</td>
<td>100</td>
<td>3</td>
</tr>
<tr>
<td>[70, 80, 50]</td>
<td>100</td>
<td>3</td>
</tr>
</tbody>
      </table>
<hr>

<p>※ 2023년 07월 31일 테스트 케이스가 추가되었습니다. 기존에 제출한 코드가 통과하지 못할 수 있습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges



## 문제 해결 아이디어
사람들의 몸무게를 담은 배열 people   
구명보트의 무게 제한 limit   
두 정보가 주어진다.   
최대 인당 2명씩 탈 수 있는 구명보트의 개수가 최소가 되어야 한다.   
일단 people 배열을 정렬한다.   
</br>

구명보트에 가장 가벼운 두 명을 태우고, 되면 임시 저장 후에 다른 더 무거운 한 명을 태워본다.   
안 되면 임시 저장한 사람을 태운다. 되면 계속해서 무거운 한 명을 태워보는 식으로 반복한다.
</br>

## Input 반례 (해결 과정)

```cpp
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> people, int limit)
{
    int answer = 0;
    int temp = 0;
    int size = people.size();
    sort(people.begin(), people.end());

    while (people.size() > 1)
    {
        temp = 0;
        for (int j = 1; j < people.size(); j++)
        {
            if (people[0] + people[j] <= limit) // 둘을 넣을 수 있음.
            {
                temp = j; // 임시 저장.
            }
            if (j == people.size() - 1 && people[0] + people[j] <= limit)  // 마지막이랑 더했을 때 가능한 경우
            {
                people.erase(people.begin() + j);
                people.erase(people.begin());
                ++answer;
            }
            else if (people[0] + people[j] > limit) // 둘을 넣을 수 없음.
            {
                if (people[0] + people[temp] <= limit && temp != 0)
                    people.erase(people.begin() + temp);
                people.erase(people.begin());
                ++answer;
            }
        }
    }
    if (people.size() == 1)
        ++answer;

    return answer;
}

int main()
{
    vector<int> s = {10,20,30,40,50,60,70,80,90};
    int limit = 100;
    int answer = solution(s, limit);
    printf("%d", answer);
    return 0;
}
```
처음 생각한 방식으로 실행해보니 테스트 케이스는 맞았지만 제출하니 시간초과와 다른 테스트케이스는 맞지 않았다.    
⇒ 문제 접근법을 바꾸기로 했다.   
원래 방식인   
```cpp
구명보트에 가장 가벼운 두 명을 태우고, 되면 임시 저장 후에 다른 더 무거운 한 명을 태워본다.
안 되면 임시 저장한 사람을 태운다. 되면 계속해서 무거운 한 명을 태워보는 식으로 반복한다. 
```
가 아니라   
```cpp
구명보트에 가장 가벼운 사람과 무거운 사람을 태우고 가능하면 둘을 태우고, 불가능하면 무거운 사람만 태우는 방법
```
으로 바꾸어보겠다.   
```cpp
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> people, int limit)
{

// 구명보트에 가장 가벼운 사람과 무거운 사람을 태우고 가능하면 둘을 태우고, 불가능하면 무거운 사람만 태우는 방법
    int answer = 0;
    sort(people.begin(), people.end());
    while (people.size() >= 2)
    {
        if (people[0] + people[people.size() - 1] <= limit)
        {
            people.erase(people.begin());
            people.erase(people.end() - 1);
            ++answer;
        }
        else
        {
            people.erase(people.end() - 1);
            ++answer;
        }
    }

    if (people.size() == 1)
        ++answer;

    return answer;
}

int main()
{
    vector<int> s = {70, 80, 50, 50};
    int limit = 100;
    int answer = solution(s, limit);
    printf("%d", answer);
    return 0;
}
```
테스트 케이스는 모두 맞았지만, 효율성 테스트에서 1번과 3번이 틀렸다고 한다.   
c++에서 vecotr의 erase연산이 제거 후 원소를 옮겨줘야 하기 때문에 시간복잡도가 O(n)이다. 이에  마지막 원소를 시간복잡도가 O(1)인 pop_back()을 사용하여 제거하고,   
  `people.erase(people.begin());`로 첫 원소를 삭제하던 코드를 인덱스를 하나 증가시키는 방식으로 시간복잡도를 줄였다.     
원래는 삭제하던 첫번째 인덱스를 삭제하지 않고, 인덱스 번호만 증가시킴으로써 while의 조건도 `i < people.size()` 로 수정하였다.     
또한, 원소를 계속 삭제하다가 마지막 원소가 남아 people의 길이가 1이 되면 while을 빠져나오는 것이었기 때문에 구명보트를 +1 해주었었는데, 이 조건도 삭제하였다.     
⇒ 시간복잡도 테스트를 모두 통과할 수 있다!    
아래는 최종 코드이다.     
</br>

## 최종 코드

```cpp
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> people, int limit)
{

    // 구명보트에 가장 가벼운 사람과 무거운 사람을 태우고 가능하면 둘을 태우고, 불가능하면 무거운 사람만 태우는 방법
    int answer = 0;
    int i = 0;
    sort(people.begin(), people.end());
    while (i < people.size())
    {
        if (people[i] + people[people.size() - 1] <= limit)
        {
            ++i;
            people.pop_back();
            ++answer;
        }
        else
        {
            people.pop_back();
            ++answer;
        }
    }

    return answer;
}

int main()
{
    vector<int> s = {70, 80, 50, 50};
    int limit = 100;
    int answer = solution(s, limit);
    printf("%d", answer);
    return 0;
}
```
