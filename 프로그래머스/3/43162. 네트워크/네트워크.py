def solution(n, computers): 
    graph = []
    
    for i in range(len(computers)):
        tmp = []
        for k in range(len(computers[i])):
            if i == k:
                continue
            if computers[i][k] == 1:
                tmp.append(k)
        graph.append(tmp)

    def dfs(start, graph, visited):
        visited[start] = True
        visited2[start] = True
        for i in graph[start]:
            if not visited[i]:
                dfs(i, graph, visited)
        
        return 0
    
    visited = [False] * len(computers)
    visited2 = [False] * len(computers)
    answer = 0
    
    v = True
    while v:
        answer += 1
        idx = visited2.index(False)
        visited2[idx] = True
        dfs(idx, graph, visited)
        count = 0
        
        for i in visited2:
            if i == True:
                count += 1
        if count == len(visited2):
            v = False

    return answer