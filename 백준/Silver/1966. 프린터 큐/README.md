# [Silver III] 프린터 큐 - 1966 

[문제 링크](https://www.acmicpc.net/problem/1966) 

### 성능 요약

메모리: 34924 KB, 시간: 76 ms

### 분류

자료 구조, 구현, 큐, 시뮬레이션

### 제출 일자

2025년 1월 12일 19:35:48

### 문제 설명

<p>여러분도 알다시피 여러분의 프린터 기기는 여러분이 인쇄하고자 하는 문서를 인쇄 명령을 받은 ‘순서대로’, 즉 먼저 요청된 것을 먼저 인쇄한다. 여러 개의 문서가 쌓인다면 Queue 자료구조에 쌓여서 FIFO - First In First Out - 에 따라 인쇄가 되게 된다. 하지만 상근이는 새로운 프린터기 내부 소프트웨어를 개발하였는데, 이 프린터기는 다음과 같은 조건에 따라 인쇄를 하게 된다.</p>

<ol>
	<li>현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.</li>
	<li>나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.</li>
</ol>

<p>예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.</p>

<p>여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다. 예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.</p>

### 입력 

 <p>첫 줄에 테스트케이스의 수가 주어진다. 각 테스트케이스는 두 줄로 이루어져 있다.</p>

<p>테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다. 이때 맨 왼쪽은 0번째라고 하자. 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다. 중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.</p>

### 출력 

 <p>각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력한다.</p>

## 문제 해결 아이디어

시간제한 2초

연산횟수 2억번

N은 100까지의 양수로, 100*100*100 = 1,000,000로 O(N^3) 이하인 알고리즘을 사용해야 함. 

큐의 시간복잡도는

- Insertion O(1)
- Deletion O(1)
- Search O(n)

첫 번째 줄 : 1) 테스트 케이스의 수 (각 테스트 케이스는 두 줄로 이루어져 있음)

2) 문서의 개수 N (1 ≤ N ≤ 100) / 몇번째로 인쇄되었는지 궁금한 문서가 현재 큐에서 몇번째에 놓여있는지를 나타내는 정수 M (0 ≤ M ≤ N)

**맨 왼쪽이 0번째**

두번째 줄 : N개의 문서 중요도. 

중요도는 1이상 9이하의 정수. 중요도가 같은 문서가 여러개 있을 수 있음. 

⇒ 테스트 케이스의 수 문서 개수로 2차원 벡터

출력은 각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력.

**예제 입력**

```cpp
**3  // 테스트 케이스 개수
1 0 // 문서 개수(1), 궁금한 문서의 현재 위치
5   // N(1)개의 문서 중요도
4 2      // 문서 개수(4), 궁금한 문서의 현재 위치
1 2 3 4  // N(4)개의 문서 중요도
6 0         // 문서 개수(6), 궁금한 문서의 현재 위치
1 1 9 1 1 1 // N(6)개의 문서 중요도**
```

**예제 출력**

1

2

5

## Input 반례 (해결 과정)

아래 코드에선 예제 입력에 대한 출력이

- code
    
    ```cpp
    #include <iostream>
    #include <vector>
    #include <algorithm>
    using namespace std;
    
    int main()
    {
        int N, M, paper, input, order; // 테스트케이스 개수, 각 테스트케이스의 문서 개수, 궁금한 문서의 위치
        vector<vector<int>> q;         // 테스트케이스 + u
        vector<int> u;                 // 각 문서 우선순위
        vector<int> p;                 // 각 테스트케이스 우선순위 문서
    
        scanf("%d", &N); // 테스트케이스 개수
    
        for (int i = 0; i < N; i++)
        {
            order = 1;
            u.clear();
            scanf("%d %d", &M, &paper); // 각 테스트케이스의 문서 개수, 궁금한 문서의 위치
            for (int j = 0; j < M; j++)
            { // 각 문서의 우선 순위 입력
                scanf("%d", &input);
                u.push_back(input);
            }
            q.push_back(u); // 테스트케이스에 해당 문서 우선순위 삽입
    
            if (u.size() == 1)
                p.push_back(1);
            else
            {
                for (int k = 0; k < M; k++)
                {
                    if (q[i][k] > q[i][paper])
                    {
                        if (k != paper)
                            order++;
                        
                    }
                }
                p.push_back(order);
            }
        }
    
        for (auto iter : p)
            printf("%d\n", iter);
    
        return 0;
    }
    ```
    

1

2

2

로 출력된다. 그 이유는 우선순위가 같은 것에 대한 처리가 없기 때문. 위 코드는 단순히 궁금한 문서의 우선순위보다 큰 우선순위의 문서 개수만 출력하게 됨.

⇒ 궁금한 문서가 있으면 일단 그 문서의 왼쪽 위치의 문서들을 살펴봐야 함. 

왼쪽 문서 중 더 높은 순위가 없다면, 낮은 문서들은 버림.

더 높은 우선순위가 있다면 뒤로 보냄. 

나도 뒤로 감. 

이를 반복. 더 낮은 애들이 없으면 멈춤.

모든 테스트 케이스가 위 반복이 끝나면 우선순위 출력.

- code
    
    ```cpp
    #include <iostream>
    #include <vector>
    #include <algorithm>
    using namespace std;
    
    int main()
    {
        int N, M, idx, input; // 테스트케이스 개수, 각 테스트케이스의 문서 개수, 궁금한 문서의 위치(idx)
        vector<vector<int>> q;  // 테스트케이스 + u
        vector<int> u;          // 각 문서 우선순위
        vector<int> priority;   // 최종 우선순위를 저장
        vector<bool> big;       // 궁금한 문서 오른쪽에 우선순위가 큰 문서가 있다는 플래그
        int small = 0;
        vector<int> answer; // 각 테스트 케이스 마다의 알고 싶은 문서의 인덱스
        vector<int> ansp;
    
        scanf("%d", &N); // 테스트케이스 개수
    
        for (int i = 0; i < N; i++)
        {
            u.clear();
            scanf("%d %d", &M, &idx); // 각 테스트케이스의 문서 개수, 궁금한 문서의 위치
            answer.push_back(idx);    // 궁금한 문서 위치 인덱스
    
            for (int j = 0; j < M; j++) // 각 문서의 우선 순위 입력
            {
                scanf("%d", &input);
                u.push_back(input);
            }
    
            q.push_back(u); // 테스트케이스에 해당 문서 우선순위 삽입
            small = 0;      //
            int k = answer[i] + 1;
            if (M == 1)
                big.push_back(false);
            while (k <= M - 1)
            {
                if (small == M - answer[i] - 1)
                    big.push_back(false);
                if (q[i][answer[i]] < q[i][k]) // 알고 싶은 문서보다 오른 쪽에 더 큰 문서가 있는지
                {
                    big.push_back(true);
                    break;
                }
                else
                    ++small;
    
                if (small >= M - answer[i] - 1)
                {
                    big.push_back(false);
                    break;
                }
                k++;
            }
    
            int j = 0;
    
            while (j <= q[i].size() - 1)
            {
                if (q[i].size() == 1)
                    break;
                if (answer[i] == 0 && big[i] == true) // 알고 싶은 문서가 맨 처음 + 오른쪽에 큰 문서가 있다면
                {
                    q[i].push_back(q[i][answer[i]]); // 알고 싶은 문서 맨 뒤로
                    q[i].erase(q[i].begin());        // 원래 위치 삭제
                    answer[i] = q[i].size() - 1;     // 알고 싶은 문서 인덱스 조정
                }
                else if (answer[i] == 0 && big[i] == false) // 알고 싶은 문서가 맨 처음 + 오른쪽에 큰 문서가 없다면
                    break;
                else if (j == answer[i])
                {
                    j++;
                    if (j >= q[i].size())
                        break;
                    continue;
                }
                else if (q[i][j] < q[i][answer[i]] && answer[i] > j) // 앞 문서의 우선순위가 더 작음 + 알고싶은 문서가 더 뒤에 있음
                {
                    q[i].erase(q[i].begin() + j); // 작은 문서 삭제
                    --answer[i];                  // 인덱스 한칸 씩 땡김
                }
                else if (q[i][j] == q[i][answer[i]] && answer[i] > j) // 앞 문서와 우선순위 같음 + 알고 싶은 문서가 더 뒤에 있음
                {
                    q[i].push_back(q[i][j]);      // 맨 앞 걸 뒤로 보내기
                    q[i].erase(q[i].begin() + j); // 그 위치 삭제
                    --answer[i];  // 알고 싶은 문서 인덱스 조정
                }
                else if (q[i][j] > q[i][answer[i]] && answer[i] > j) // 앞 문서의 우선순위가 더 큼 + 알고싶은 문서가 더 뒤에 있음.
                {
                    j++;
                    if (j >= q[i].size())
                        break;
                    continue;
                }
                else if (q[i][j] > q[i][answer[i]] && answer[i] < j) // 뒤 문서의 우선순위가 더 큼 + 알고 싶은 문서가 더 앞에 있음
                {
                    q[i].push_back(q[i][answer[i]]);      // 높은 문서 냅두고 알고 싶은 문서를 뒤로
                    q[i].erase(q[i].begin() + answer[i]); // 원래 위치 삭제
                    answer[i] = q[i].size() - 1;          // 알고 싶은 문서 인덱스 조정
                }
                else if (q[i][j] > q[i][answer[i]] && answer[i] < j) // 뒤 문서의 우선순위가 더 작음 + 알고 싶은 문서가 더 앞에 있음.
                {
                    q[i].erase(q[i].begin() + j); // 작은 문서 삭제
                    --answer[i];                  // 인덱스 한칸 씩 땡김
                }
                else if (q[i][j] > q[i][answer[i]] && answer[i] < j) // 뒤 문서의 우선순위와 같음 + 알고 싶은 문서가 더 앞에 있음.
                {
                    q[i].erase(q[i].begin() + j); // 같은 문서 삭제
                    --answer[i];                  // 인덱스 한칸 씩 땡김
                }
            }
    
            priority.push_back(answer[i] + 1);
        }
    
        for (auto iter : priority)
            printf("%d\n", iter);
    
        return 0;
    }
    ```
    

마지막 케이스인 

1 1 9 1 1 1

에서 처음 0이 뒤로 간 후, 9 뒤에 1이 뒤로 가는 현상이 발생함.

아예 새로운 방식을 도입해야할 필요성을 느낌.

궁금한 문서의 우선 순위(paper[i])를 따로 적어두고, 인덱스(answer[i])를 처음부터 하나씩 이동하면서, 아래 조건을 따른다. (j는 q[i].size()번 순회)

1. 탐색하는 인덱스와 궁금한 문서 인덱스가 같으면 ⇒ 탐색 인덱스 +1, continue
    
    answer[i]==j, ++j; continue;
    
2. 궁금한 문서가 탐색 인덱스보다 앞에 있는데, 궁금한 문서 우선순위가 더 큰 경우
    
    궁금한 문서 인덱스 < 탐색 인덱스 && paper[i] ≥ q[i][j] ⇒ continue
    
3. 궁금한 문서가 탐색 인덱스보다 앞에 있는데, 궁금한 문서 우선순위가 더 작은 경우
    
    궁금한 문서 인덱스 < 탐색 인덱스 && paper[i] < q[i][j] ⇒ 순위 +1
    
4. 탐색 인덱스 < 궁금한 문서 인덱스 && paper[i] ≤ q[i][j] ⇒ continue
5. 탐색 인덱스 < 궁금한 문서 인덱스 && paper[i] > q[i][j] ⇒ 순위 +1
6. j가 테스트케이스 길이보다 커지면 중지.
- code
    
    ```cpp
    #include <iostream>
    #include <vector>
    #include <algorithm>
    using namespace std;
    
    int main()
    {
        int N, M, idx, input;  // 테스트케이스 개수, 각 테스트케이스의 문서 개수, 궁금한 문서의 위치(idx)
        vector<vector<int>> q; // 테스트케이스 + u
        vector<int> u;         // 각 문서 우선순위(테스트케이스 저장용)
        vector<int> priority;  // 최종 우선순위를 저장
        vector<int> answer;    // 각 테스트 케이스 마다의 알고 싶은 문서의 인덱스
        vector<int> paper;     // 알고 싶은 문서의 우선순위
        int big = 0;
    
        scanf("%d", &N); // 테스트케이스 개수
    
        for (int i = 0; i < N; i++)
        {
            u.clear();
            scanf("%d %d", &M, &idx); // 각 테스트케이스의 문서 개수, 궁금한 문서의 위치
            answer.push_back(idx);    // 궁금한 문서 위치 인덱스
    
            for (int j = 0; j < M; j++) // 각 문서의 우선 순위 입력
            {
                scanf("%d", &input);
                u.push_back(input);
            }
            paper.push_back(u[idx]); // 궁금한 문서의 우선순위
            q.push_back(u);          // 테스트케이스에 문서들의 우선순위 삽입
    
            input = 1; // 순위 임시 저장용(초기화)
            big = 0;
            for (int j = 0; j < M; j++)
            {
                if (M == 1)
                    break;
                if (j == answer[i])
                    continue;
                else if (answer[i] < j && paper[i] >= q[i][j])
                {
                    if (big==0)
                        continue;
                    else
                        ++input;
                }
                else if (answer[i] < j && paper[i] < q[i][j])
                {
                    ++input;
                    ++big;
                }
                else if (j < answer[i] && q[i][j] >= paper[i])
                    ++input;
                else if (j < answer[i] && q[i][j] < paper[i])
                    continue;
            }
            priority.push_back(input);
        }
    
        for (auto iter : priority)
            printf("%d\n", iter);
    
        return 0;
    }
    ```
    

예제입력은 맞지만 

아래 input에 대해선 반례가 생김

```
1
9 0
1 1 9 1 1 9 6 7 8

// output
8

// answer
6
```

⇒ 문제 이해를 잘못 했던 것 같다. 

찾으려는 문서와 같은 우선순위의 문서가 있고, 그 우선순위보다 높은 우선순위의 다른 문서가 있다면, (예,  8 1 1 ‘1’) 찾으려는 문서와 같은 우선순위의 문서도 뒤로 보내야 한다.

이번엔 새롭게 알고리즘을 설계하여, 찾으려는 문서의 인덱스를 k(m)로 두고, k가 이동하면 계속 업데이트하여 순서를 추적하도록 하겠다. 

맨앞과 뒤의  것들을 비교하고 큰 거 있으면 맨 뒤로 보내고, 없으면 출력(삭제)한다.

또한 문서들이 삭제되는 횟수를 count 변수에 저장하여, 맨앞에 사라졌는데 그게 k면 ++count가 해당 문서의 순서이다.

가장 큰 수를 기준으로 앞 부분은 궁금한 인덱스보다 큰 것만, 뒷 부분은 궁금한 인덱스보다 크거나 같은 걸 모두 세었는데 위 input과 같은 출력을 뱉어 틀렸다.

- code
    
    ```python
    from collections import deque
    n = int(input())
    result = [] 
    for i in range(n):
        total = 1
        number = deque(map(int, input().split())) # 0문서 개수, 1궁금한 위치
        stand = deque(map(int, input().split())) # 0문서들 중요도
        max_idx = stand.index(max(stand))
        if len(stand) == 1:
            result.append(1)
            continue
        if max(stand) == stand[number[1]]:
            max_idx = number[1]
    
        for j in range(len(stand)):
            if j == number[1]: 
                continue
            if j < max_idx and stand[number[1]] < stand[j]:
                total += 1
            if j >= max_idx and stand[number[1]] <= stand[j]:
                total += 1
        if max_idx < number[1]:
            total -= 1
        result.append(total)
    
    print(*result)
    ```
    
    ```
    1
    4 0
    1 2 1 3
    ```
    
    위 입력의 정답은 4인데 3으로 출력된다. 위 코드는 단순히 가장 큰 수를 기준으로 앞 뒤로 궁금한 문서의 우선순위와 비교해 개수를 세는 것이기 때문에 틀린 결과를 내는 것 같다.
    
    즉, 우선순위가 같은 애들끼리의 순서는, 가장 우선순위가 높은 것이 아니라 직전에 출력한 것에 의존한다는 것이다.
    
    ⇒ 따라서 idx 0이 문서들 중 우선순위 max라면 pop하고 찾으려는 문서의 idx를 업데이트 한다. 그리고 order++. 
    max가 아니라면 그 문서는 가장 뒤로 보낸다. 그리고 찾으려는 문서의 idx를 업데이트한다.
    위 과정은 찾으려는 문서가 pop 될 때까지 반복한다.
    
    > deque는 큐라고 생각하여 pop을 하면 가장 앞의 원소가 삭제되는 줄 알았는데 그게 아니었다… 
    **큐의 앞, 뒤에서 삽입, 삭제가 가능한 큐 (double-ended queue의 줄임말)**
    따라서 pop은 그냥 맨 뒤 원소 삭제이기 때문에 popleft를 해주어야 한다.
    > 
    
    이것 때문에 무한반복이 걸려 디버깅해보니 앞이 삭제됐던 문제였다. 
    
    예제도 알맞게 돌아가며 정답..!
    

## 최종 코드

```python
from collections import deque
n = int(input())
result = [] 
for i in range(n):
    total = 1
    number = deque(map(int, input().split())) # 0문서 개수, 1궁금한 위치
    stand = deque(map(int, input().split())) # 0문서들 중요도
    order = 1
    while True:
        if stand[0] == max(stand) and number[1]!=0:
            stand.popleft()
            number[1] -= 1
            order += 1
        elif stand[0] != max(stand):
            stand.append(stand[0])
            stand.popleft()
            if number[1]!=0:   number[1] -= 1
            elif number[1]==0: number[1] = len(stand)-1
        elif stand[0] == max(stand) and number[1]==0:
            break
    result.append(order)

print(*result)

```

