# [Silver V] 수 정렬하기 2 - 2751 

[문제 링크](https://www.acmicpc.net/problem/2751) 

### 성능 요약

메모리: 8180 KB, 시간: 688 ms

### 분류

정렬

### 제출 일자

2024년 8월 13일 17:36:33

### 문제 설명

<p>N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.</p>

### 출력 

 <p>첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.</p>

## 문제 정의

시간 제한 2초

메모리 제한 256MB

첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

## 문제 해결 아이디어

이 문제의 시간 제한은 2초이므로, 최악의 경우에도 연산횟수가 2억번을 넘어선 안 된다. 

N의 범위는 1 ≤ N ≤ 1,000,000이기 때문에 시간복잡도는 O(N) 또는 O(NlogN)가 적합할 것으로 보인다.

sort()함수가 intro sort의 정렬 방식을 바탕으로 구현되어 있음.

intro sort : quick sort를 기반으로 heap sort와 insertion sort를 섞은 방식으로, (최악의 경우 O(n^2)의 시간복잡도를 가지는 quick sort와 다르게) 최악의 경우에도 O(nlogn)을 보장하는 정렬 알고리즘.

O(n^2)은 사용하기엔 너무 시간복잡도가 큼.  (quick sort 불가)

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    vector<int> number;
    int n, m;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> m;
        number.push_back(m);
    }

    sort(number.begin(), number.end());

    for (auto &n : number)
        cout << n << endl;

    return 0;
}
```

그러나 위 코드로 작성 시 결과는 ‘시간 초과’… 왜 그럴까

이유는 endl 때문..

**endl의 경우 flush()함수를 겸하기 때문에 실행마다 출력 버퍼를 지워주는 과정(flush)이 생겨 “\n”보다 속도가 느리다.**

- 예시 코드
    
    ```cpp
    #include<iostream>
    #include<time.h>
    using namespace std;
    
    int main()
    {
    	clock_t start, end;
    	double time1, time2, time3, time4;
    
    	start = clock(); //시간 측정 시작
    
    	// #time1 "cout << i << endl;"
    	for (int i = 0; i < 10000; i++)
    	{
    		cout << i << endl;
    	}
    
    	end = clock(); //시간 측정 끝
    	time1 = end - start;
    
    	// #time2 "cout << i << "\n";"
    	start = clock(); //시간 측정 시작
    
    	for (int i = 0; i < 10000; i++)
    	{
    		cout << i << '\n';
    	}
    
    	end = clock(); //시간 측정 끝
    	time2 = end - start;
    
    	// #time3 "printf("%d\n", i);"
    	start = clock(); //시간 측정 시작
    
    	for (int i = 0; i < 10000; i++)
    	{
    		printf("%d\n", i);
    	}
    
    	end = clock(); //시간 측정 끝
    	time3 = end - start;
    
    	printf("\n\n");
    	cout << "cout << i << endl : " << time1 << "ms" << endl;
    	cout << "cout << i << '\\n' : " << time2 << "ms" << endl;
    	cout << "printf(\"%d\\n\", i) : " << time3 << "ms" << endl;
    }
    ```
    <img width="515" alt="image" src="https://github.com/user-attachments/assets/52e2b771-11a0-482f-a82b-4b7c66d4ebee">

    

성능면에서 cout << endl 보다는 cout <<"\n" 가,

cout << "\n"보다는 prinft("%d\n") 가 더 빠른것을 알 수 있다.

[참고링크]
[cplusplus.com](https://cplusplus.com/reference/ostream/endl/)

## Input 반례 (해결 과정)

## 최종 코드

```cpp

```
