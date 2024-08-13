# [Silver V] 단어 정렬 - 1181 

[문제 링크](https://www.acmicpc.net/problem/1181) 

### 성능 요약

메모리: 6628 KB, 시간: 560 ms

### 분류

정렬, 문자열

### 제출 일자

2024년 8월 7일 18:50:38

### 문제 설명

<p>알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.</p>

<ol>
	<li>길이가 짧은 것부터</li>
	<li>길이가 같으면 사전 순으로</li>
</ol>

<p>단, 중복된 단어는 하나만 남기고 제거해야 한다.</p>

### 입력 

 <p>첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.</p>

### 출력 

 <p>조건에 따라 정렬하여 단어들을 출력한다.</p>
</p>

**예제 입력**

```
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
```
   
**예제 결과**

```
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate
```
</br>

## 문제 해결 아이디어   

`입력은 첫째줄에 단어 개수 N (1 ≤ N ≤ 20,000) ⇒ 단어 개수는 int형 사용 가능`

문자열 길이 제한

조건 1. **길이가 짧은 것부터**

조건2. **길이가 같으면 사전 순으로**

단, 중복되는 단어는 하나만 남기고 제거.

`중복되는 단어는 하나만 사용 ⇒ set 이용`

: set에 추가하여 중복 체크, set은 중복을 허용하지 않고 자동정렬 해주기 때문.

문자열의 길이를 기준으로 정렬 ⇒ quick sort 이용

- quick sort 설명
    
    ```cpp
    quickSort(word, 0, word.size() - 1);
    
    ------------------------------------------------------
    
    void quickSort(vector<string> &data, int start, int end) // start, end : vector의 시작과 끝 인덱스 번호
    {
        // start가 end보다 크거나 같으면, 
        // 즉 부분 벡터에 요소가 하나 이하이면 정렬이 완료된 것으로 간주하고 함수를 종료
        if (start >= end)
            return;  
    
        int pivot = start; // 기준 값
        int i = start + 1;  // 왼쪽에서 오른쪽으로 이동하며 피벗보다 큰 값을 찾는 인덱스
        int j = end;  // 오른쪽에서 왼쪽으로 이동하며 피벗보다 작은 값을 찾는 인덱스
    
        while (i <= j)  // i가 j보다 작거나 같을 동안 반복
        {
            while (i <= end && data[i].length() <= data[pivot].length()) 
                i++;
            while (j > start && data[j].length() >= data[pivot].length()) 
                j--;
            if (i > j) // 현재 엇갈린 상태면 pivot 값 교체
            {
                swap(data[j], data[pivot]);
            }
            else
            {
                swap(data[i], data[j]);
            }
        }
    
        // 재귀 호출
        quickSort(data, start, j - 1);
        quickSort(data, j + 1, end);
    }
    ```
    
    **엇갈린 상태** 
    
    i는 왼쪽에서 오른쪽으로 이동하면 pivot보다 큰 값을 찾고, j는 오른쪽에서 왼쪽으로 이동하면서 pivot보다 작은 값을 찾는다. 이 과정에서 i와 j가 서로 지나치게 되는 순간
    
    ⇒ 이 때 pivot의 값을 j와 교환하면 pivot을 기준으로 작은 값들은 pivot의 왼쪽으로, 큰 값들은 오른쪽으로 이동하게 됨.
    
    ⇒ 만약 i와 j가 엇갈리지 않았다면(i ≤ j), i와 j가 가리키는 값을 교환하여 작은 값은 왼쪽으로, 큰 값은 오른쪽으로 이동시킨다.
    

`문자열의 길이는 50을 넘지 않기 때문에 배열을 만들어서` 

`문자열 개수 == 배열 인덱스`

`ex) 인덱스 3이라면 문자열 개수가 3인 단어의 개수가 들어있음.`

인덱스가 1이상인(문자열이 있음) 부분만 사전식 정렬

## Input 반례 (해결 과정)   
</br>

### 코드   

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
using namespace std;

void quickSort(vector<string> &data, int start, int end);

int main()
{
    int n;
    cin >> n;
    string w;
    set<string> wordSet; // 중복 체크를 위한 set
    int wordSize[50] = {0};

    cin.ignore();
    for (int i = 0; i < n; i++)
    {
        getline(cin, w);
        if (wordSet.find(w) == wordSet.end()) // 중복이 아닐 경우에만 벡터에 추가
        {
            ++wordSize[w.size() - 1];
            wordSet.insert(w); // set에 추가하여 중복 체크, set은 중복을 허용하지 않고 자동정렬 해줌.
        }
    }
    vector<string> word(wordSet.begin(), wordSet.end());

    // 길이 기준 정렬
    quickSort(word, 0, word.size() - 1);

    int begin = 0;
    for (int i = 0; i < word.size(); i++) // 문자열이 담긴 배열을 하나씩 순회
    {
        if (wordSize[i] == 0)
            continue;

        begin = begin + wordSize[i]; // 정렬을 시작할 인덱스

        // wordSize의 각 배열 크기가 1 초과일 때만 사전식 정렬.
        if (wordSize[i] > 1)
            sort(word.begin() + begin, word.begin() + begin + wordSize[i]);
    }

    cout << "\n입력받은 문자열:" << endl;
    for (const auto &w : word) // word 벡터에 저장된 모든 문자열을 출력합니다.
        cout << w << endl;

    return 0;
}

void quickSort(vector<string> &data, int start, int end) // strat:시작 인덱스, end:끝 인덱스
{
    // start가 end보다 크거나 같으면,
    // 즉 부분 벡터에 요소가 하나 이하이면 정렬이 완료된 것으로 간주하고 함수를 종료
    if (start >= end)
        return;

    int pivot = start; // 기준 값
    int i = start + 1; // 왼쪽에서 오른쪽으로 이동하며 피벗보다 큰 값을 찾는 인덱스
    int j = end;       // 오른쪽에서 왼쪽으로 이동하며 피벗보다 작은 값을 찾는 인덱스

    while (i <= j) // i가 j보다 작거나 같을 동안 반복
    {
        while (i <= end && data[i].length() <= data[pivot].length())
            i++;
        while (j > start && data[j].length() >= data[pivot].length())
            j--;
        if (i > j) // 현재 엇갈린 상태면 pivot 값 교체
        {
            swap(data[j], data[pivot]);
        }
        else
        {
            swap(data[i], data[j]);
        }
    }

    // 재귀 호출
    quickSort(data, start, j - 1);
    quickSort(data, j + 1, end);
}

```

input

```
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
```

output

```
// 위 코드 output
i
no
it
im
but
more
wait
wont
cannot
hesitate
yours

// 정답 output
i
im
it
no
but
more
wait
wont 
yours
cannot
hesitate
```

> **이유 예측**
i가 2일 때, 문자열 길이가 2인 문자들이 정렬돼야 하는데 3인 문자들이 정렬됨.
i가 4일 때, 문자열 길이가 4인 문자들이 정렬돼야 하는데 5인 문자부터 정렬이 시작되었고, 문자열 길이가 4인 문자들의 개수만큼 정렬되어 5이상의 문자열 길이를 가진 문자들도 함께 정렬이 됨. 또한, vector의 index 범위를 초과하는 문제점 발생.
> 

<aside>
💡 따라서 i가 n일 때 문자열 길이가 n인 것들만 정렬이 되도록, 정렬이 시작되는 인덱스를 땡겨야함. (정렬 시작 위치 조정)

</aside>

```cpp
int begin = 0;
for (int i = 0; i < word.size(); i++) // 문자열이 담긴 배열을 하나씩 순회
{
	~~//if (wordSize[i] == 0) wordSize[i]가 0이면 어차피 sorting안 하므로 필요 없는 코드.
		  //continue;~~

	~~// 정렬하기도 전에 정렬 시작 인덱스가 갱신되어서 정렬 후로 옮김.
  // begin = begin + wordSize[i]; // 정렬을 시작할 인덱스~~

  // wordSize의 각 배열 크기가 1 초과일 때만 사전식 정렬.
	  if (wordSize[i] > 1)
		    sort(word.begin() + begin, word.begin() + begin + wordSize[i]);
		    
		begin = begin + wordSize[i];
}   
```

그러나 OutOfBound 런타임 에러 발생…

⇒ `begin`이 `word` 벡터의 범위를 넘어갈 수 있으며, 잘못된 인덱스를 참조하게 될 수 있다.

- 해결코드1
    
    for (int i = 0; i < word.size(); i++)의 조건으로 반복을 하여 길이 기준 정렬을 하게 되는 경우, 입력받은 문자열의 개수만큼 반복을 하는 걸로 위 코드가 짜여져 있음. 그러나 위 코드의 경우, i는 입력받은 문자열의 개수만큼 반복을 하고, 반복문 안에서 정렬하는 조건에서 문자열의 개수가 문자 길이보다 작으면, 정렬이 실행되지 않는 문제가 있다. (i가 wordSize의 값이 있는 인덱스 값까지 가지 못 할 수 있음.) 
    
    따라서 아래와 같이 wordSize[i]대신 wordSize[word[i].size()]로 인덱스를 고칠 수 있다. 
    
    ```cpp
    #include <iostream>
    #include <vector>
    #include <string>
    #include <algorithm>
    #include <set>
    using namespace std;
    
    bool compare(string a, string b);
    
    int main()
    {
        int n; // 입력받는 문자의 개수
        cin >> n;
        string w;
        set<string> wordSet;    // 중복 체크를 위한 set
        int wordSize[51] = {0}; // 문자열의 길이는 최대 50, wordSize[0]은 필요 x
    
        cin.ignore();
        for (int i = 0; i < n; i++)
        {
            getline(cin, w);
            if (wordSet.find(w) == wordSet.end()) // 중복이 아닐 경우에만 벡터에 추가
            {
                ++wordSize[w.size()];
                wordSet.insert(w); // set에 추가하여 중복 체크, set은 중복을 허용하지 않고 자동정렬 해줌.
            }
        }
    
        vector<string> word(wordSet.begin(), wordSet.end());
    
        sort(word.begin(), word.end(), compare);
    
        int begin = 0;
        for (int i = 0; i < word.size(); i++) // 문자열이 담긴 배열을 하나씩 순회
        {
            if (wordSize[word[i].size()] > 1)   // wordSize의 각 배열 크기가 1 초과일 때만 사전식 정렬.
                sort(word.begin() + begin, word.begin() + begin + wordSize[word[i].size()]);
    
            begin = begin + wordSize[word[i].size()]; // 정렬을 시작할 인덱스 갱신
        }
    
        for (const auto &w : word) // word 벡터에 저장된 모든 문자열을 출력합니다.
            cout << w << endl;
    
        return 0;
    }
    
    bool compare(string a, string b)
    {
        return a.size() < b.size();
    }
    ```
    
    ⇒ OutOfBound가 아니라 SefFault가 발생.
    
- 해결코드2
    - `for (int i = 0; i < word.size(); i++)`에서 `i`는 `word` 벡터의 크기와 비교되고 있다. 하지만 `wordSize` 배열은 문자열 길이별로 개수를 저장하고 있어, `i`는 0부터 50까지 순회해야한다.
    - 예를 들어, `word.size()`가 3이라면, 루프는 `i`가 0, 1, 2일 때까지만 실행되며, 이는  `wordSize` 배열의 전체 범위를 고려하지 않게 된다.
    
    해결코드1의 코드처럼 wordSize[word[i].size()]로 정렬 파라미터를 변경한 게 아니라 for (int i = 0; i < word.size(); i++) 조건을 for (int i = 0; i <= 51; i++)로 변경하여 모든 문자열별 길이 순회.
    
    ```cpp
    #include <iostream>
    #include <vector>
    #include <string>
    #include <algorithm>
    #include <set>
    using namespace std;
    
    bool compare(string a, string b);
    
    int main()
    {
        int n; // 입력받는 문자의 개수
        cin >> n;
        string w;
        set<string> wordSet;    // 중복 체크를 위한 set
        int wordSize[51] = {0}; // 문자열의 길이는 최대 50, wordSize[0]은 필요 x
    
        cin.ignore();
        for (int i = 0; i < n; i++)
        {
            getline(cin, w);
            if (wordSet.find(w) == wordSet.end()) // 중복이 아닐 경우에만 벡터에 추가
            {
                ++wordSize[w.size()];
                wordSet.insert(w); // set에 추가하여 중복 체크, set은 중복을 허용하지 않고 자동정렬 해줌.
            }
        }
    
        vector<string> word(wordSet.begin(), wordSet.end());  // set을 vector<string>으로 복사.
    
        sort(word.begin(), word.end(), compare);  // 문자열 길이 기준 정렬
    
        int begin = 0;
        int end = 0;
        for (int i = 0; i <= 51; i++) // 가질 수 있는 문자열 길이 배열만큼 반복
        {
            if (wordSize[i] > 1)   // wordSize의 각 배열 크기가 1 초과일 때만 사전식 정렬.
                sort(word.begin() + begin, word.begin() + begin + wordSize[i]);
    
            begin = begin + wordSize[i]; // 정렬을 시작할 인덱스 갱신
        }
    
        for (const auto &w : word) // word 벡터에 저장된 모든 문자열을 출력.
            cout << w << endl;
    
        return 0;
    }
    
    bool compare(string a, string b)
    {
        return a.size() < b.size();
    }
    ```
    
</br>

## 최종 코드   

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
using namespace std;

bool compare(string a, string b);

int main()
{
    int n; // 입력받는 문자의 개수
    cin >> n;
    string w;
    set<string> wordSet;    // 중복 체크를 위한 set
    int wordSize[51] = {0}; // 문자열의 길이는 최대 50, wordSize[0]은 필요 x

    cin.ignore();
    for (int i = 0; i < n; i++)
    {
        getline(cin, w);
        wordSet.insert(w); // set에 추가하여 중복 체크, set은 중복을 허용하지 않고 자동정렬 해줌.
    }

    vector<string> word(wordSet.begin(), wordSet.end()); // set을 vector<string>으로 복사.

    for (int i = 0; i < word.size(); i++)
        ++wordSize[word[i].size()];

    sort(word.begin(), word.end(), compare); // 문자열 길이 기준 정렬

    int begin = 0;
    for (int i = 0; i <= 51; i++) // 가질 수 있는 문자열 길이 배열만큼 반복
    {
        if (wordSize[i] > 1) // wordSize의 각 배열 크기가 1 초과일 때만 사전식 정렬.
            sort(word.begin() + begin, word.begin() + begin + wordSize[i]);

        begin = begin + wordSize[i]; // 정렬을 시작할 인덱스 갱신
    }

    for (const auto &w : word) // word 벡터에 저장된 모든 문자열을 출력.
        cout << w << endl;

    return 0;
}

bool compare(string a, string b)
{
    return a.size() < b.size();
}
```

