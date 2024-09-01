# [Silver V] 나이순 정렬 - 10814 

[문제 링크](https://www.acmicpc.net/problem/10814) 

### 성능 요약

메모리: 9732 KB, 시간: 88 ms

### 분류

정렬

### 제출 일자

2024년 9월 1일 22:52:01

### 문제 설명

<p>온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 온라인 저지 회원의 수 N이 주어진다. (1 ≤ N ≤ 100,000)</p>

<p>둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다. 나이는 1보다 크거나 같으며, 200보다 작거나 같은 정수이고, 이름은 알파벳 대소문자로 이루어져 있고, 길이가 100보다 작거나 같은 문자열이다. 입력은 가입한 순서로 주어진다.</p>

### 출력 

 <p>첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순, 나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력한다.</p>
 

## 문제 해결 아이디어
시간제한 3초, 약 3억번의 계산 가능.   
N은 1부터 100,000의 자연수.      
=> 시간 복잡도가 `O(NlogN)` 이하인 알고리즘을 설계해야 한다.   
</br>
첫줄에 N이 주어진다.    
둘째줄부터 N개의 줄에 회원의 나이, 이름이 주어진다. (가입 순으로 입력)    

## Input 반례 (해결 과정)
예제 입력은 정상적으로 작동하는데 2%에서 틀렸다는 결과가 나왔다.   
c++ algorithm에서 일반 sort는 퀵정렬이라서 unstable sort라서 같은 키값일 경우 순서가 보장되지 않다는 것을 알게 되었다.   
C++ 표준 라이브러리에는 정렬 함수로서 std::sort()와 **std::stable_sort()**가 존재한다. 이 두 함수는 기본적으로 배열 또는 벡터의 시작과 끝 위치를 인자로 받으며, 선택적으로 비교 함수를 추가하여 사용할 수 있다.    
둘 모두 시간 복잡도는 평균적으로 O(n log n)으로, 대략적으로 n log n 번의 비교를 수행한다.    
하지만 std::stable_sort()는 동일한 값들 사이의 상대적인 순서를 유지하는 추가적인 작업이 필요하므로, 실제 실행 시간은 std::sort()보다 약간 더 길게 나올 수 있다.   
따라서 이 두 함수는 각각의 적절한 상황에서 사용해야 한다. 특히, 동일한 값들 사이의 상대적인 순서를 유지해야 하는 상황에서는 std::stable_sort()를 사용하는 것이 바람직하다.   
**참고사이트**
[[C++] sort vs stable_sort with C++](https://maloveforme.tistory.com/194)

## 최종 코드

```cpp
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool comp(pair<int, string> a, pair<int, string> b)
{
    return a.first < b.first;
}

int main()
{
    int n, age;
    string name;
    vector<pair<int, string>> people;

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> age >> name;
        people.push_back(make_pair(age, name));
    }

    stable_sort(people.begin(), people.end(), comp); // 나이 오름차순 정렬

    for (const auto &p : people)
        cout << p.first << ' ' << p.second << '\n';
				// printf("%d %s\n", people[i].first, (people[i].second).c_str()); 로도 적을 수 있음.
    return 0;
}

```

