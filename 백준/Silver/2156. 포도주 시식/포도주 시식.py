n = int(input())
grape = [0]
dp = [0] * (n+1)
for i in range(n):
    grape.append(int(input()))

if n >= 1:
    dp[1] = grape[1]
if n >= 2:
    dp[2] = grape[1] + grape[2]
if n >= 3:
    dp[3] = max(grape[3]+grape[1], grape[3]+grape[2])
if n >= 4:
    for i in range(4, n+1):
        dp[i] = max(grape[i]+grape[i-1]+dp[i-3], grape[i]+dp[i-2], grape[i]+grape[i-1]+dp[i-4])
print(max(dp))