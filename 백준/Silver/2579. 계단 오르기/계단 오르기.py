n = int(input())
stair = [0]
for i in range(n):
    stair.append(int(input()))

dp = [0] * (n + 1)
if n == 1:
    print(stair[1])
    exit(0)
elif n == 2:
    print(stair[1] + stair[2])
    exit(0)

elif n >= 3:
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2]
    dp[3] = max(stair[1] + stair[3], stair[2] + stair[3])
if n >= 4:
    for i in range(4, n + 1):
        dp[i] = max(stair[i]+stair[i-1]+dp[i-3], stair[i]+dp[i-2])

print(dp[n])