def solution(n, computers): 
    graph = [[] for _ in range(n)]
    
    # 인접리스트 만들기
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)
                
    visited = [False]*n # 각 노드의 방문 여부
    visited2 = [False]*n # 각 네트워크(라고 가정 시) 방문 여부
    print(visited)
    answer = 0
    
    def dfs(start, graph, visited):
        visited[start] = True
        visited2[start] = True
        
        for i in graph[start]:
            if not visited[i]:
                dfs(i, graph, visited)
                
    
    flag = True
    while flag:
        answer += 1
        idx = visited2.index(False)
        dfs(idx, graph, visited)
        
        if visited2.count(True) == n:
            break
            
    return answer