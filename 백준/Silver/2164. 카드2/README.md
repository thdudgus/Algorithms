# [Silver IV] 카드2 - 2164 

[문제 링크](https://www.acmicpc.net/problem/2164) 

### 성능 요약

메모리: 4044 KB, 시간: 4 ms

### 분류

자료 구조, 큐

### 제출 일자

2024년 9월 3일 17:50:00

### 문제 설명

<p>N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.</p>

<p>이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.</p>

<p>예를 들어 N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다. 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다. 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다. 마지막으로 2를 버리고 나면, 남는 카드는 4가 된다.</p>

<p>N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 정수 N(1 ≤ N ≤ 500,000)이 주어진다.</p>

### 출력 

 <p>첫째 줄에 남게 되는 카드의 번호를 출력한다.</p>


## 문제 해결 아이디어
시간제한 2초   
N의 범위는 1부터 500,000으로 O(NlogN) 이하의 알고리즘을 사용해야 한다.   
가장 위의 수를 없애고, 위에 있는 수를 아래로 보내는 과정 ⇒ 큐 구현   
</br>
vector를 이용하여 길이가 1이 될때까지 반복.
</br>
## Input 반례 (해결 과정)

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n;
    vector<int> card;
    cin >> n;
    for (int i = 0; i < n; i++)
        card.push_back(i + 1);

    while (card.size() > 1)
    {
        card.erase(card.begin());     // 맨앞 요소 삭제
        card.push_back(card.front()); // 그다음 맨앞 요소 맨 뒤로
        card.erase(card.begin());
    }
    cout << card[0];
    return 0;
}
```
큐의 개념만 사용하면 된다고 생각하여 벡터를 활용하였는데, 위 코드에서 시간 초과가 발생하였다.    
vector의 시간복잡도를 살펴보면,    
처음 for문에서 1 * n번,   
그 다음 while문에서 n+1+n = 2n+1, (2n+1)\*n = 4n\*2+4n+1번이다.   
이를 더하면 시간복잡도는 O(n^2)로 예측해볼 수 있고, 여기에서 시간초과가 발생한 것으로 보인다.   
</br>
vector 라이브러리의 함수로 큐 개념을 구현하는 것이 아니라, queue 라이브러리로 연산을 하면 아래와 같다.   
처음 for문에서 1 * n번,   
그 다음 while문에서 1+1+1=3, 3\*n번이다.   
이를 더하면 시간복잡도는 O(n)으로 예측해볼 수 있다.    
#include <queue>로 코드를 다시 작성하였을 때의 최종 코드는 아래와 같고, 정답인 것을 확인할 수 있다.   
</br>
## 최종 코드
```cpp
#include <iostream>
#include <queue>
using namespace std;

int main()
{
    int n;
    queue<int> card;
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
        card.push(i + 1);

    while (card.size() > 1)
    {
        card.pop();
        card.push(card.front());
        card.pop();
    }

    printf("%d", card.front());

    return 0;
}
```
