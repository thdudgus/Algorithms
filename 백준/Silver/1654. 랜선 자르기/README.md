# [Silver II] 랜선 자르기 - 1654 

[문제 링크](https://www.acmicpc.net/problem/1654) 

### 성능 요약

메모리: 2156 KB, 시간: 4 ms

### 분류

이분 탐색, 매개 변수 탐색

### 제출 일자

2024년 9월 11일 23:31:48

### 문제 설명

<p>집에서 시간을 보내던 오영식은 박성원의 부름을 받고 급히 달려왔다. 박성원이 캠프 때 쓸 N개의 랜선을 만들어야 하는데 너무 바빠서 영식이에게 도움을 청했다.</p>

<p>이미 오영식은 자체적으로 K개의 랜선을 가지고 있다. 그러나 K개의 랜선은 길이가 제각각이다. 박성원은 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K개의 랜선을 잘라서 만들어야 한다. 예를 들어 300cm 짜리 랜선에서 140cm 짜리 랜선을 두 개 잘라내면 20cm는 버려야 한다. (이미 자른 랜선은 붙일 수 없다.)</p>

<p>편의를 위해 랜선을 자르거나 만들 때 손실되는 길이는 없다고 가정하며, 기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정하자. 그리고 자를 때는 항상 센티미터 단위로 정수길이만큼 자른다고 가정하자. N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다. 이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에는 오영식이 이미 가지고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N이 입력된다. K는 1이상 10,000이하의 정수이고, N은 1이상 1,000,000이하의 정수이다. 그리고 항상 K ≦ N 이다. 그 후 K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 센티미터 단위의 정수로 입력된다. 랜선의 길이는 2<sup>31</sup>-1보다 작거나 같은 자연수이다.</p>

### 출력 

 <p>첫째 줄에 N개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력한다.</p>


## 문제 해결 아이디어
시간제한 2초. 약 2억번의 계산 가능.   
</br>
첫째줄에는 **이미 가지고 있는 랜선의 개수 k**와 **필요한 랜선의 개수 n**이 입력된다.   
k는 1이상 10,000이하의 정수.   
n은 1이상 1,000,000이하의 정수.   
그리고 항상 k ≤ n이다.   
</br>
그후 k줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 센티미터 단위의 정수로 입력된다.    
랜선의 길이는 2^31-1보다 작거나 같은 자연수이다. ⇒ Int 범위   
</br>
출력은 n개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력.    
 
```
4 11
802
743
457
539
```
예제 입력이 위와 같으면    
이미 가지고 있는 랜선의 개수 k == 4   
필요한 랜선의 개수 n == 11   
k개의 랜선의 길이는 각각 802, 743, 457, 539이다.    
</br>
k가 n보다 크면 랜선들 중 가장 큰 값을 처음 값으로     
n이 k보다 크면 랜선들 중 가장 작은 값을 처음 값으로 잡는다.   
a = 처음 값    
1. 각 랜선에 대해 랜선길이 / a   
2. 몫들이 n보다 크면 처음 평균에서 +1 한다.   
3. 그 몫들을 더했을 때 n이 나오면 멈춘다.     
3의 결과가 나올 때까지 1~3의 과정을 반복한다.   
</br>
## Input 반례 (해결 과정)
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int k, n, input;

    // 이미 가지고 있는 랜선의 개수, 필요한 랜선의 개수
    scanf("%d %d", &k, &n);
    vector<int> lan, temp; // 랜선의 길이, 나눈 몫 저장

    for (int i = 0; i < k; i++)
    {
        scanf("%d", &input);
        lan.push_back(input);
        temp.push_back(input);
    }
    sort(lan.begin(), lan.end());
    int a = (k > n) ? lan[k-1] : lan[0];

    int nsum; // 랜선을 잘랐을 때의 개수 합.
    bool cut = false;

    while (cut == false)
    {
        nsum = 0;
        for (int i = 0; i < k; i++)  // 랜선을 나눈 몫들 (개수 구하기 위함)
        {
            temp[i] = lan[i] / a;  // 랜선들을 a의 길이로 잘랐을 때 나오는 랜선 개수
            nsum += temp[i];
        }

        if (nsum == n)
        {
            cut = true;
            break;
        }
        else if (nsum < n)
            --a;
        else
            ++a;
    }

printf("%d", &a);

    return 0;
}
```
예제입력에 대한 답은 맞지만, 시간초과가 발생한다.   
</br>
`for (int i = 0; i < k; i++)`는 k번 반복하므로 O(k)를 만족한다.   
`sort(lan.begin(), lan.end());`는 k개의 요소를 가진 벡터를 정렬하므로 O(klogk)를 만족한다.   
    `while (cut == false) { ... for (int i = 0; i < k; i++) ...}` cut이 true가 나올 때까지 반복이므로, a의 범위는 랜선 길이의 범위와 같다. 랜선의 길이는 2^31-1보다 작거나 같은 자연수이므로 1부터 2^31-1 만큼 반복할 수 있고, 그 속에서 k번도 반복이 이루어진다. 따라서 O(k*(랜선길이범위=약20억))의 복잡도를 보이는 것으로 예상된다.   
k의 범위는 1이상 10,000이하의 정수이므로 시간제한을 넘어가게 된다.   
</br>
<aside>
💡
따라서 랜선의 길이에 따른 필요없는 반복을 하지 않도록 이를 조절해주어야 한다.    
(O(logn)으로 조정이 필요할 것으로 보인다. ⇒ 이진탐색 활용)
</aside>

```cpp
for (int i = 0; i < lan.back(); i++) // 랜선 자르는 기준 for 이진탐색
        binary.push_back(i + 1);

    int a = binary[(left+right) / 2]; // 랜선 자르는 기준 처음 값
```

mid = (left + right) / 2   
처음 값 a는  binary[mid/2] (랜선들의 길이 합/n)   
1. 각 랜선에 대해 랜선길이 / a   
2. 몫들이 n보다 작으면 left=left, right = mid-1   
3. 몫들이 n보다 크면 left=mid+1, right=right   
4. 그 몫들을 더했을 때 n이 나오면 멈춘다.    

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int k, n, input;
    // 이미 가지고 있는 랜선의 개수, 필요한 랜선의 개수
    scanf("%d %d", &k, &n);
    vector<int> lan, temp; // 랜선의 길이, 나눈 몫 저장
    vector<int> binary;    // 랜선 자르는 기준 for 이진탐색
    int total = 0;
    for (int i = 0; i < k; i++)
    {
        scanf("%d", &input);
        lan.push_back(input);
        temp.push_back(input);
        total += input;
    }
    sort(lan.begin(), lan.end());

    for (int i = 0; i < lan.back(); i++) // 랜선 자르는 기준 for 이진탐색
        binary.push_back(i + 1);

    int nsum; // 랜선을 잘랐을 때의 개수 합.
    int left = 0;
    int right = lan.back() - 1;
    int mid, a;
    for (int j = 0; j < lan.back(); j++)
    {
        mid = (left + right) / 2;
        a = binary[mid];
        nsum = 0;

        for (int i = 0; i < k; i++) // 랜선을 나눈 몫들 (개수 구하기 위함)
        {
            temp[i] = lan[i] / a; // 랜선들을 a의 길이로 잘랐을 때 나오는 랜선 개수
            nsum += temp[i];
        }

        if (nsum < n)
            right = mid - 1;
        else if (nsum > n)
            left = mid + 1;
        else
            break;

        if (left > right)
            break;
    }

    printf("%d", a);

    return 0;
}
```

답은 잘 나오지만 메모리 초과라고 뜬다.   
메모리 제한 기준은 128MB인데,  `vector<int> binary` 에서 오류가 난 것으로 보인다. 이 벡터의 크기는 lan.back()이므로 랜선의 길이 범위 중 정수에 해당한다. 최대 2^31-1까지 벡터의 사이즈가 커질 수 있다. int는 4byte이므로 `(4byte == 4e-6MB)`    
4byte * (2^31-1)는 약 (4e-6)*(2*e+9)이므로 약 8*e+3 mb로 128MB를 넘게 된다.   
int형은 4byte    
1KB는 1024byte   
1MB는 1024KB   
128MB = 128 * 1024KB = 128 * 1024 * 1024byte    
128 * 1024 * 1024 / 4개 = 33554432   
⇒ 128MB는 int 기준으로 vector의 크기는 33,554,432   
<aside>
💡
따라서 이진 탐색은 유지한 채 메모리를 줄여야 할 것으로 보인다.
</aside>
미리 binary vector를 만들지 않게    
랜선들의 길이 합 + k 보다 작은 수 내에서 binary의 사이즈 크기로 설정하려 한다.    
이유는 k≤n이기 때문에 k개의 랜선으로 만들려 할 때가 가장 크게 자르는 것이기 때문에 아래로 변경하였다.   

```cpp
int t = total / k;              // 가장 크게 자르는 수
    for (int i = 0; i < t; i++) // 랜선 자르는 기준 for 이진탐색
        binary.push_back(i + 1);  //1부터 t까지
```

메모리 초과는 해결되었는데 최대값을 출력하는 게 아니라 그냥 되는 값을 최댓값과 관련 없이 출력한다.   
예제 입력에서 답은 200인데 198로 출력된다. 198도 n을 만족하지만 최댓값은 아니다....   
flag를 설정해서 증가하면서 탐색할 때 flag를 true로 설정하고,  nsum==n일 때 flag가 true인 경우 해당 a 값을 임시로 저장한다. 그리고 반복문을 나오는 것이 아니라 계속 한다.     
이때 nsum==n이거나 더 최댓값을 찾을 때 이전값이 최댓값이면 임시저장 값을 출력하도록 해보겠다.   

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int k, n, input; // 이미 가지고 있는 랜선의 개수 // 필요한 랜선의 개수 // (입력값,)랜선을 잘랐을 때의 개수 합.
    scanf("%d %d", &k, &n);
    vector<int> lan;    // 랜선의 길이, 나눈 몫 저장
    vector<int> binary; // 랜선 자르는 기준 for 이진탐색
    long long total = 0;
    for (int i = 0; i < k; i++)
    {
        scanf("%d", &input);
        lan.push_back(input);
        total += (long long)input;
    }
    sort(lan.begin(), lan.end());

    long long t = total / k;        // 가장 크게 자르는 수
    for (int i = 0; i < t + 1; i++) // 랜선 자르는 기준 for 이진탐색
        binary.push_back(i);        // 1부터 t까지

    int max; // 최대값 임시저장
    bool m;  // 자르는 기준이 증가 중인가

    int left = 1;
    int right = binary.size() - 1;
    int mid, a;
    mid = (left + right) / 2;
    max = binary[mid];
    int temp = 0;

    while (left <= right)
    {
        mid = (left + right) / 2;
        a = binary[mid];
        input = 0;

        for (int i = 0; i < k; i++) // 랜선을 나눈 몫들 (개수 구하기 위함)
        {
            temp = lan[i] / a; // 랜선들을 a의 길이로 잘랐을 때 나오는 랜선 개수
            input += temp;
        }

        if (input < n) //  자르는 기준이 너무 커서 줄여야 함.
            right = mid - 1;
        else if (input > n) // 자르는 기준이 너무 작아서 늘려야 함
        {
            left = mid + 1;
            m = true; // 자르는 기준이 증가 중
        }
        else // n개를 만들 수 있는 경우
        {
            if (m == true) // 자르는 기준이 증가하는 중이라면
            {
                max = a;
                left = mid + 1; // 기준 더 높여보기
            }
            else
                break;
        }
    }

    printf("%d", max);

    return 0;
}
```

위 코드는 예제 입력은 해결되었지만, integer overflow가 발생해서 total을 long long으로 변경하고, 메모리 초과도 발생하여 temp 벡터도 없앤 상태이다.    
</br>
메모리 초과된 부분을 예측해보겠다.   
벡터 lan의 최대 사이즈는 k의 최대인 10,000이다. int는 4byte이므로 40,000byte    
벡터 binary의 최대 사이즈는 `long long t = total / k` 이다. t는 최대 (2^31-1)*10000/1 로 매우 크다. 그런데 여기서 어떻게 더 binary의 사이즈를 줄여야할지 잘 판단이 서지 않는다.   
⇒ 굳이 1부터 t까지 1씩 증가하는 수를 저장한 벡터라서 벡터로 할 필요 없이 그냥 수로 하면 된다는 것을 알았다. **이분탐색을 진행할 때 평소 배열 내의 수에서만 답이 나와야하는 상황이었기 때문에 이번 경우도 당연하게, 배열에 넣어 사용했었는데 1씩 증가하는 경우면 벡터가 필요 없다는 것을 알았다.**   
따라서 lan.back()의 수를 right로 1을 left로 단순히 int로만 설정해주고 이분탐색을 진행해주면 된다.   
</br>

최댓값을 임시저장하는 ans을 0으로 초기화하고(처음에 초기화하지 않았더니 ans가 garvage값이었어서 결과가 이상했다.), input > n이거나 nsum==n인 경우에 left의 값을 mid+1해주었다.    
nsum==n을 만족하면서 최댓값이어야 하기 때문에, left의 값을 mid+1한 것이고, mid값과 최댓값을 임시 저장한 ans을 비교하여 큰 값을 ans에 저장해준다.    
nsum==n인 조건에도 left = mid+1을 하고, `max(ans, mid);` 를 사용함으로써 flag를 쓰지 않아도 된다.   
이때 반복문이 계속 반복되다가 left > right가 되면 반복문이 끝나게 되며, 저장했던 ans를 출력하게 된다.    
⇒ 드디어 정답..!   
아래는 최종 코드이다.    
</br>
## 최종 코드

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    unsigned int k, n, input; // 이미 가지고 있는 랜선의 개수 // 필요한 랜선의 개수 // (입력값,)랜선을 잘랐을 때의 개수 합.
    scanf("%d %d", &k, &n);
    vector<int> lan; // 랜선의 길이, 나눈 몫 저장
    for (int i = 0; i < k; i++)
    {
        scanf("%d", &input);
        lan.push_back(input);
    }
    sort(lan.begin(), lan.end());

    unsigned int ans = 0; // 최대값 임시저장 및 답
    unsigned int left = 1;
    unsigned int right = lan.back();
    unsigned int mid = (left + right) / 2;

    while (left <= right)
    {
        mid = (left + right) / 2;
        input = 0; // 랜선을 잘랐을 때의 개수 합.

        for (int i = 0; i < k; i++) // 랜선을 나눈 몫들 (개수 구하기 위함)
            input += lan[i] / mid;  // 랜선들을 a의 길이로 잘랐을 때 나오는 랜선 개수

        if (input < n) //  자르는 기준이 너무 커서 줄여야 함.
            right = mid - 1;
        else  // 자르는 기준이 너무 작아서 늘리거나 nsum==n인 경우
        {
            left = mid + 1;
            ans = max(ans, mid);  // 최댓값을 구하기 위함.
        }
    }

    printf("%d", ans);

    return 0;
}
```

