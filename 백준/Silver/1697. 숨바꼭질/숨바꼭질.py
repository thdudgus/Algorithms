n, k = map(int, input().split())
dp=[100000]*(100000+1)
visited =[False]*(100000+1)
dp[n]=0
def find_dp(v):
    queue=[v]
    visited[v]=True
    while queue:
        temp = queue.pop(0)
        for x in [temp-1, temp+1, temp*2]:
            if 0<=x<=100000 and visited[x]==False:
                visited[x]=True
                dp[x]=dp[temp]+1
                queue.append(x)
                if x==k:
                    return
        
find_dp(n)
print(dp[k])