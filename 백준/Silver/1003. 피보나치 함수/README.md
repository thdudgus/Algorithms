# [Silver III] 피보나치 함수 - 1003 

[문제 링크](https://www.acmicpc.net/problem/1003) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2025년 2월 16일 15:31:28

### 문제 설명

<p>다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다.</p>

<pre>int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n‐1) + fibonacci(n‐2);
    }
}
</pre>

<p><code>fibonacci(3)</code>을 호출하면 다음과 같은 일이 일어난다.</p>

<ul>
	<li><code>fibonacci(3)</code>은 <code>fibonacci(2)</code>와 <code>fibonacci(1)</code> (첫 번째 호출)을 호출한다.</li>
	<li><code>fibonacci(2)</code>는 <code>fibonacci(1)</code> (두 번째 호출)과 <code>fibonacci(0)</code>을 호출한다.</li>
	<li>두 번째 호출한 <code>fibonacci(1)</code>은 1을 출력하고 1을 리턴한다.</li>
	<li><code>fibonacci(0)</code>은 0을 출력하고, 0을 리턴한다.</li>
	<li><code>fibonacci(2)</code>는 <code>fibonacci(1)</code>과 <code>fibonacci(0)</code>의 결과를 얻고, 1을 리턴한다.</li>
	<li>첫 번째 호출한 <code>fibonacci(1)</code>은 1을 출력하고, 1을 리턴한다.</li>
	<li><code>fibonacci(3)</code>은 <code>fibonacci(2)</code>와 <code>fibonacci(1)</code>의 결과를 얻고, 2를 리턴한다.</li>
</ul>

<p>1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, <code>fibonacci(N)</code>을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 테스트 케이스의 개수 T가 주어진다.</p>

<p>각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.</p>

### 출력 

 <p>각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.</p>


## 문제 해결 아이디어

위 코드에서 print 부분을 count 해보겠다.    

```python
t = int(input())
result = [0, 0]
def fibonacci(n, result):
    if n == 0:
        result[0] += 1
        return 0
    elif n == 1:
        result[1] += 1
        return 1    
    else:
        return fibonacci(n-1, result) + fibonacci(n-2, result)

for _ in range(t):
    n = int(input())
    result = [0, 0]
    fibonacci(n, result)
    print(result[0], result[1])
```

예제 입력들에 대한 답은 모두 맞지만, 역시나 시간초과가 발생한다.   

시간이 0.25초로 매우 짧기 때문에 DP를 이용해서 필요하지 않은 계산을 줄이도록 하겠다.   

0과 1이 호출되는 횟수도, 피보나치 수 0, 1, 2는 [1, 0], [0, 1], [1, 1]로 고정되어 있다. 이후 3부터는 피보나치 수 원리에 따라 1과 2의 호출 횟수의 합이다.   

따라서 피보나치 수 자체는 계산할 필요가 없고 피보나치 수를 3부터 테스트 케이스 중 가장 큰 값까지 반복하면서, 0과 1 호출 횟수를 저장한다. (이전과 그 이전 호출 횟수 값을 더함.)   

⇒ 정답 !   

아래는 최종 코드이다.    

## 최종 코드

```python
t = int(input())
result = [[1, 0], [0, 1], [1, 1]]
case = []
for _ in range(t):
    case.append(int(input()))
m = max(case)
for i in range(3, m+1):
    result.append([result[i-1][0]+result[i-2][0], result[i-1][1]+result[i-2][1]])

for i in case:
    print(result[i][0], result[i][1])
```
