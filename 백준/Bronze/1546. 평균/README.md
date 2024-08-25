# [Bronze I] 평균 - 1546 

[문제 링크](https://www.acmicpc.net/problem/1546) 

### 성능 요약

메모리: 2024 KB, 시간: 0 ms

### 분류

사칙연산, 수학

### 제출 일자

2024년 8월 25일 20:45:33

### 문제 설명

<p>세준이는 기말고사를 망쳤다. 세준이는 점수를 조작해서 집에 가져가기로 했다. 일단 세준이는 자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.</p>

<p>예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.</p>

<p>세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 시험 본 과목의 개수 N이 주어진다. 이 값은 1000보다 작거나 같다. 둘째 줄에 세준이의 현재 성적이 주어진다. 이 값은 100보다 작거나 같은 음이 아닌 정수이고, 적어도 하나의 값은 0보다 크다.</p>

### 출력 

 <p>첫째 줄에 새로운 평균을 출력한다. 실제 정답과 출력값의 절대오차 또는 상대오차가 10<sup>-2</sup> 이하이면 정답이다.</p>

 ## 문제 해결 아이디어
시간 제한은 2초   
N은 1000보다 작거나 같은 자연수이기 때문에 O(N^2)의 알고리즘을 사용하면 된다.   

## Input 반례 (해결 과정)
sort로 시험점수 정렬 후 (점수/M*100)으로 조작   
그 후 평균을 구한다.   
</br>
코드를 작성하면서 간과했던 부분이 있다.   
자료형을 잘 살펴볼 것.    
작은값에서 큰값을 나눌 때 자료형이 int이면 소수점 부분은 버려지기 때문에 0이 되는 것을 까먹지 말자. 해당 문제에선 0이 되면 안 됐음.   

## 최종 코드
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int N, input;
    scanf("%d", &N);
    vector<float> score;
    float total, temp, temp2;

    for (int i = 0; i < N; i++)
    {
        scanf("%d", &input);
        score.push_back(input);
    }

    sort(score.begin(), score.end());
    temp = score[N-1];
    total = 0;

    for (int i = 0; i < N ; i++)
    {
        temp2 = (score[i] / temp) * 100.0;
        score[i] = temp2;
        total += score[i];
    }

    printf("%.2f", (float)(total/N));

    return 0;
}
```
