# [Silver III] 통계학 - 2108 

[문제 링크](https://www.acmicpc.net/problem/2108) 

### 성능 요약

메모리: 5504 KB, 시간: 176 ms

### 분류

구현, 수학, 정렬

### 제출 일자

2024년 9월 1일 21:21:28

### 문제 설명

<p>수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.</p>

<ol>
	<li>산술평균 : N개의 수들의 합을 N으로 나눈 값</li>
	<li>중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값</li>
	<li>최빈값 : N개의 수들 중 가장 많이 나타나는 값</li>
	<li>범위 : N개의 수들 중 최댓값과 최솟값의 차이</li>
</ol>

<p>N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.</p>

### 출력 

 <p>첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.</p>

<p>둘째 줄에는 중앙값을 출력한다.</p>

<p>셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.</p>

<p>넷째 줄에는 범위를 출력한다.</p>


## 문제 해결 아이디어
첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다.      
⇒ 시간 제한은 2초로, 시간복잡도 O(nlogn)을 넘지 않는다.     
</br>
그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.      
</br>
첫째줄에는 산술평균 출력. 소수점 이하 첫째 자리에서 반올림한 값 출력   
둘째줄에는 중앙값 출력   
셋째줄에는 최빈값 출력. 여러개 있다면 최빈값 중 두 번째로 작은 값 출력   
넷째줄에는 범위 출력   

## Input 반례 (해결 과정)
셋째줄에는 최빈값 출력하는데, 여러개 있다면 최빈값 중 두 번째로 작은 값 출력하기 위해 map을 활용하였다.     
key 값엔 입력받은 정수, value값엔 해당 정수가 얼마나 입력되었는지를 세어 value값을 기준으로 내림차순으로 정렬하였다.     
이때 최빈값들 중에 같은 게 있다면 same을 true로 설정하여     
```cpp
 printf("%d\n", same ? v[1].first : v[0].first); // true면 최빈값 중 두 번째로 작은 값을 출력하고, false면 최빈값 그대로 출력하게 하였다.     
```

**반올림 방법**    
```cpp
#include <cmath>

    double avg = round((sum / (double)n));
    if (avg == -0)
        avg = 0;
```
위처럼 round()를 이용하여 반올림을 하였다. -0.333과 같은 경우엔 반올림을 하면 -0이 출력되어 오류가 생겼었기 때문에, 이를 조건문으로 처리해주었다.      
</br>
산술평균을 구하기 위한 sum과 avg과 int로 구현할 수 없어 double을 사용하였다.
</br>
## 최종 코드

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
using namespace std;

static bool comp(pair<int, int> &a, pair<int, int> &b)
{
    return a.second > b.second;
}

int main()
{
    int n;
    double input;
    vector<int> number;
    double sum = 0;
    scanf("%d", &n);
    map<int, int> frequency;

    for (int i = 0; i < n; i++)
    {
        scanf("%lf", &input);
        number.push_back((int)input);                       // 수 입력
        sum += input;                                  // 수들의 총합
        frequency.insert({(int)input, frequency[input]++}); // 최빈값 구하기 위한 map
    }

    sort(number.begin(), number.end()); // 오름차순 정렬

    vector<pair<int, int>> v(frequency.begin(), frequency.end()); // 최빈값 구하기 위한 map을 vector로 변환
    sort(v.begin(), v.end(), comp);                                  // 최빈값 내림차순 정렬
    bool same = false;                                               // 최빈값이 여러개인가
    for (int i = 1; i < v.size(); i++)
    {
        if (v[0].second == v[i].second)
        {
            same = true;
            break;
        }
    }

    double avg = round((sum / (double)n));
    if (avg == -0)
        avg = 0;

    printf("%.0lf\n", avg);                            // 산술평균
    printf("%d\n", number[n / 2]);                  // 중앙값
    printf("%d\n", same ? v[1].first : v[0].first); // 최빈값
    printf("%d\n", number.back() - number.front()); // 범위

    return 0;
}
```
