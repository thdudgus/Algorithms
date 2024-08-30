# [Silver II] 스택 수열 - 1874 

[문제 링크](https://www.acmicpc.net/problem/1874) 

### 성능 요약

메모리: 3056 KB, 시간: 24 ms

### 분류

자료 구조, 스택

### 제출 일자

2024년 8월 30일 23:27:03

### 문제 설명

<p>스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.</p>

<p>1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.</p>

### 입력 

 <p>첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 물론 같은 정수가 두 번 나오는 일은 없다.</p>

### 출력 

 <p>입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다. push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO를 출력한다.</p>


## 문제 해결 아이디어
1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다.   
이때 스택에 push 하는 순서는 반드시 오름차순 (ex. 1, 2, 3, 4, …)    
⇒ 이 뜻이 1부터 n까지의 수를 스택에 오름차순으로 push하고, pop을 하면서 첫번째 입력 다음인 두번째 입력한 수열(예제입력1 : n = 8, 나타낼 수열 = 4 3 6 8 7 5 2 1)을 나타낼 수 있냐는 문제.    
⇒ 가장 큰 수 기준, 왼쪽은 오름차순, 왼쪽은 내림차순이어야 push, pop 가능.    
</br>
vector 4개 사용.   
1. target vector (주어진 수열 저장)   
2. 1~n을 담을 vector
   가장 큰 수를 pop 했는데 그 2번 vector의 back() 수와 수열의 다음 수가 같지 않으면 NO 출력.   
4. push, pop 연산을 담을 결과 vector   
 </br>
시간 제한 2초. 약 2억번의 연산.   
첫 줄에 n이 주어진다. 1 ≤ n ≤ 100,000    
O(nlogn) 이하의 시간복잡도를 가져야 한다.    
</br>
둘째줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 같은 정수가 두 번 나오는 일은 없다.
</br>
필요한 연산은 한 줄에 한 개씩 출력. push는 +로, pop은 -로 출력. 불가능은 NO로 출력.

## Input 반례 (해결 과정)
- code
    
    ```cpp
    #include <iostream>
    #include <vector>
    using namespace std;
    
    int main()
    {
        int n, temp;
        vector<int> sequence; // 목표 수열
        vector<int> st;       // 1~n 저장할 벡터
        vector<char> result;  // +, -를 저장할 벡터
    
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
        {
            scanf("%d", &temp);
            sequence.push_back(temp); // 주어진 수열 저장
        }
        int j = 1;
        for (int i = 0; i < n; i++)
        { // 수열 하나씩 탐색
            while (sequence[i] >= j)
            {
                st.push_back(j);
                result.push_back('+');
                j++;
            }
            if (sequence[i] == j-1)
            {
                st.pop_back();
                result.push_back('-');
                if (j - 1  == n)
                {
                    if (sequence[i + 1] != st.back())
                    {
                        printf("NO");
                        return 0;
                    }
                }
                j--;
            }
        }
    
        for (int i = 0; i < result.size(); i++)
            printf("%d : %c\n", i+1, result[i]);
    
        return 0;
    }
    
    ```
    
    예제입력1에 대한 결과로    
    
    ```
    1 : +
    2 : +
    3 : +
    4 : +
    5 : -
    6 : -
    7 : +
    8 : +
    9 : +
    10 : +
    11 : -
    12 : +
    13 : +
    14 : +
    15 : -
    16 : -
    ```
    
    위와 같은 결과가 나옴.
    </br>
    확인 결과, j가 pop될 때 -1 되면서 이미 스택에 담겼던 수가 또 담기게 되어 다음과 같은 결과가 생김.   
    예를 들어 스택에 1, 2, 3, 4까지 담겼다가 4, 3이 pop 되면 5부터 담겨야 하는데 다시 3부터 담기게 됨.     
    ⇒ j를 줄이는 대신 조건문의 조건을 아래 코드처럼 변경
    
    ```cpp
    for (int i = 0; i < n; i++)
        { // 수열 하나씩 탐색
            while (sequence[i] >= temp)
            {
                st.push_back(temp); // 1~n 스택에 push
                result.push_back('+');
                temp++; // 마지막으로 push한 수 기억.
            }
            if (sequence[i] == st.back())
            {
                st.pop_back();
                result.push_back('-');
    
                if (sequence[i] == n && i + 1 < n)
                {
                    if (sequence[i + 1] > st.back())
                    {
                        printf("NO");
                        return 0;
                    }
                }
            }
        }
    ```
    
    예제입력1과 예제입력2는 모두 맞으나 출력 초과가 생김.. n  
    ⇒ 이유가 뭘까…   
    고민하다가 출력초과는 나오지 말아야할 게 나왔을 때 생기는 오류로, NO가 출력되어 생기는 오류이다. 따라서 NO가 출력되는 알고리즘을 살펴본 결과, sequence[i] == n 부분이 잘못된 것을 알 수 있었다.  
    sequence[i]이 수열에서 가장 큰 수인 n과 같지 않아도, sequence[i+1]은 스택에 가장 위(마지막 원소)에 남아있는 수보다 클 수 없기 때문에 이 부분을 삭제하였다.     
    ⇒ 정답!!!!       
    최종 코드는 아래와 같다.    
    

## 최종 코드

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n, temp;
    vector<int> sequence; // 목표 수열
    vector<int> st;       // 1~n 저장할 벡터
    vector<char> result;  // +, -를 저장할 벡터

    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &temp);
        sequence.push_back(temp); // 주어진 수열 저장
    }

    temp = 1; // 1~n 스택에 푸시한 후, 값 저장.(pop한 후, pop한 수의 다음부터 push하기 위함.)

    for (int i = 0; i < n; i++)
    { // 수열 하나씩 탐색
        while (sequence[i] >= temp)
        {
            st.push_back(temp); // 1~n 스택에 push
            result.push_back('+');
            temp++; // 마지막으로 push한 수 기억.
        }
        if (sequence[i] == st.back())
        {
            st.pop_back();
            result.push_back('-');

            if (i + 1 < n && sequence[i + 1] < st.back())
            {
                printf("NO");
                return 0;
            }
        }
    }

    for (int i = 0; i < result.size(); i++)
        printf("%c\n", result[i]);

    return 0;
}
```

