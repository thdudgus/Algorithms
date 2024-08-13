# Algorithms
This is an auto push repository for Baekjoon Online Judge created with [BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub).

일반적인 CPU 기반의 PC나 채점용 컴퓨터에서 **1초**에 실행될 수 있는 최대 연산 횟수는 **약 1억 번**.

> ex) 문제에서 주어진 N의 최대값이 10만이며, 주어진 제한시간이 1초라면?
⇒ 시간 복잡도가 O(N^2)인 알고리즘의 연산 횟수는 100,000 * 100,000 = 10,000,000,000이므로 사용할 수 없다. 
⇒ 100초
> 

### 1초에 최대 연산 횟수(최대 입력 크기)

| 시간 복잡도 | 최대 연산 횟수 |
| --- | --- |
| O(N) | 약 1억번 |
| O(N^2) | 약 1만번 |
| O(N^3) | 약 500번 |
| O(2^N) | 약 20번 |
| O(N!) | 10번 |

### 제한 시간이 1초 일 경우, N의 범위에 따른 시간 복잡도 선택

- **N의 범위가 500:** 시간 복잡도가 `O(N^3)` 이하인 알고리즘을 설계
- **N의 범위가 2,000:** 시간 복잡도가 `O(N^2)` 이하인 알고리즘을 설계
- **N의 범위가 100,000:** 시간 복잡도가 `O(NlogN)` 이하인 알고리즘을 설계
- **N의 범위가 10,000,000:** 시간 복잡도가 `O(N)` 이하인 알고리즘을 설계
- **N의 범위가 10,000,000,000:** 시간 복잡도가 `O(logN)` 이하인 알고리즘을 설계

<img width="523" alt="image" src="https://github.com/user-attachments/assets/e9ac22cb-b66e-4af6-99d0-cf7c5deb7cd5">

