N, M, V = map(int, input().split())
edge=[[] for _ in range(N+1)]
visited =[False]*(N+1)
path1=[V]
path2=[V]
for _ in range(M):
    x,y = map(int, input().split())
    edge[x].append(y)
    edge[y].append(x)
for i in range(1,N+1):
    edge[i].sort()
def dfs(k):
    visited[k]=True
    for i in edge[k]:
        if visited[i]==False:
            path1.append(i)
            dfs(i)
def bfs(V):
    queue=[V]
    visited2=[False]*(N+1)
    visited2[V]=True
    while queue:
        k=queue.pop(0)
        for i in edge[k]:
            if visited2[i]==False:
                visited2[i]=True
                path2.append(i)
                queue.append(i)
            
dfs(V)
bfs(V)
print(*path1)
print(*path2)