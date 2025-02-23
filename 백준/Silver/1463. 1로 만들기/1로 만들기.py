n = int(input())
dp = [0] * (n + 1)

for i in range(2, n+1):
    # 1 빼는 경우
    dp[i] = dp[i-1] + 1
    # 2로 나누어 떨어지면, 2로 나눈 경우와 비교
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    # 3으로 나누어 떨어지면, 3으로 나눈 경우와 비교
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])
