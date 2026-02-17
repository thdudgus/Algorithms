import sys
n = int(sys.stdin.readline())
consults = [[0, 0]]  # 상담시작일, 수익
for _ in range(n):
    consults.append(list(map(int, sys.stdin.readline().split())))
dp = [0] * (n + 2)  # dp[i] = i일부터 퇴사일까지 벌 수 있는 최대 수익

for i in range(n, 0, -1):
    if i + consults[i][0] > n + 1:  # 오늘 상담이 퇴사일을 넘기는 경우
        dp[i] = dp[i+1]   # 오늘 수익이 없어 내일의 최대값을 가져옴.
    else:  # 오늘 상담이 퇴사일을 넘기지 않는 경우
        # 오늘 상담을 하지 않는 경우와 하는 경우 중 최대값을 가져옴.
        dp[i] = max(dp[i+1], consults[i][1] + dp[i+consults[i][0]])

print(dp[1])