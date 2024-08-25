# [Silver IV] 설탕 배달 - 2839 

[문제 링크](https://www.acmicpc.net/problem/2839) 

### 성능 요약

메모리: 2020 KB, 시간: 0 ms

### 분류

다이나믹 프로그래밍, 그리디 알고리즘, 수학

### 제출 일자

2024년 8월 25일 16:36:07

### 문제 설명

<p>상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.</p>

<p>상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.</p>

<p>상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)</p>

### 출력 

 <p>상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.</p>

 ## 문제 해결 아이디어
시간 제한 1초.
연산 횟수 1초에 1억번 가능. (100,000,000)
3 ≤ N ≤ 5,000
5,000^2 = 25,000,000
⇒ O(N^2) 이하인 알고리즘을 사용할 수 있다.

정확하게 N 킬로그램을 만들 수 없다면 -1을 출력한다.
⇒ 3 또는 5로 나눴을 때 0인 경우는 무조건 가능. (1)
그렇지 않은 경우도 있음 ⇒ 5로 나눴을 때의 나머지가 3의 배수라면 가능 (2)
ex) 23의 경우 5킬로그램 4봉지, 3킬로그램 1봉지로 가능.
위 경우도 아닌 경우도 아니라면 ⇒ 1 출력 
최대한 적은 수의 봉지를 가져가야 한다.
⇒ (1), (2) 중 하나를 충족해야 함. 
(2)인 경우, 몫과 나머지를 3으로 나눈 몫을 더한 후 출력한다.
(1)인 경우, 해당 몫을 출력한다.

## Input 반례 (해결 과정)
- code
    ```cpp
    #include <iostream>
    using namespace std;
    
    int main()
    {
        int N, fr, tr, temp, total;
        scanf("%d", &N);
    
        fr = N % 5;
        tr = N % 3;
    
        if (fr % 3 == 0) // 5로 나눴을 때의 나머지가 3의 배수라면
        {
            temp = N - (fr); // 5로 딱 나누어지도록 나머지를 제거.
            temp = temp / 5; // 5킬로그램 봉지 수
            total = temp;
            temp = temp / 3; // 3킬로드램 봉지 수 (3으로 나눈 몫)
            total += temp;
        }
        else if (fr == 0)
            total = N / 5;
        else if (tr == 0)
            total = N / 3;
        else
            total = -1;
    
        printf("%d", total);
        return 0;
    }
    ```
    11을 입력하면 3이 나와야 하는데 -1이 출력된다.
    ⇒ 5를 뺐을 때 가능한지 경우 넣기   
    ```cpp
        else if ((N - 5) % 3 == 0)
        {
            total = (N - 5) / 3;
            temp = N - (total * 3);
            total = total + temp / 5;
        }
    ```
    11은 해결했지만 전체 경우 커버 불가능.
    - code
        
        ```cpp
        #include <iostream>
        using namespace std;
        
        int main()
        {
            int N, fr, tr, temp, total, total1, total2, total3;
            scanf("%d", &N);
            total = -2;
            total1 = -2;
            total2 = -2;
            total3 = -2;
            fr = N % 5;  // 5로 나눈 나머지
            tr = N % 3;  // 3으로 나눈 나머지
        
            for (int i = 1; i <= (N / 5); i++)
            {
                if ((N - 5*i) % 3 == 0)
                {
                    total1 = (N - 5) / 3;
                    temp = N - (total1 * 3);
                    total1 = total1 + temp / 5;
                }
            }
            for (int i; i <= (N / 3); i++)
            {
                if ((N - 3 * i) % 5 == 0)
                {
                    total2 = (N - 3 * i) / 5;
                    temp = N - (total2 * 5);
                    total2 = total2 + temp / 3;
                }
            }
        
            if (total1 > total2)
                total3 = total1;
            else
                total3 = total2;
        
            if (fr % 3 == 0) // 5로 나눴을 때의 나머지가 3의 배수라면
            {
                temp = N - (fr); // 5로 딱 나누어지도록 나머지를 제거.
                temp = temp / 5; // 5킬로그램 봉지 수
                total = temp;
                temp = temp / 3; // 3킬로드램 봉지 수 (3으로 나눈 몫)
                total += temp;
                if (total > total3)
                    total = total;
                else
                    total = total3;
            }
            else if (fr == 0) // 5로 나누어 떨어지면
            {
                total = N / 5;
                if (total > total3)
                    total = total;
                else
                    total = total3;
            }
            else if (tr == 0) // 3으로 나누어 떨어지면
            {
                total = N / 3;
                if (total > total3)
                    total = total;
                else
                    total = total3;
            }
            else
                total = -1;
        
            if (total > total3)
                total = total;
            else
                total = total3;
        
            printf("%d", total);
            return 0;
        }
        ```
        
## 새로운 접근 방법
5로 나누어 떨어지는지 확인.
N에서 3을 계속 빼면서, 그 수가 5의 배수인지 확인.
3으로 나누어 떨어지는지 확인.
그외는 -1
⇒ 성공! 아래에 최종 코드 첨부.

## 최종 코드
```cpp
#include <iostream>
using namespace std;

int main()
{
    int N, fr, tr, temp, total, total1, total3;
    scanf("%d", &N);
    fr = N % 5; // 5로 나눈 나머지
    tr = N % 3; // 3으로 나눈 나머지

    if (fr == 0) // 5로 나누어 떨어지면
    {
        total = N / 5;
        printf("%d", total);
        return 0;
    }
    else
    {
        for (int i = N / 5; i >= 1; i--)
        {
            if ((N - (5 * i)) % 3 == 0)
            {
                total1 = (N - 5 * i) / 3;
                temp = N - (total1 * 3);
                total = total1 + temp / 5;
                printf("%d", total);
                return 0;
            }
        }
    }
    if (tr == 0) // 3으로 나누어 떨어지면
        total = N / 3;
    else
        total = -1;
    printf("%d", total);
    return 0;
}
```
