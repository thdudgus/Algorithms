def solution(n, computers): 
    graph = []
    
    # 인접리스트 만들기
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
    
    visited = [False] * len(computers) # 한 그래프 안에서 각 노드 방문 여부
    visited2 = [False] * len(computers) # 그래프가 여러 개인 경우 노드 방문 여부
    answer = 0
    
    v = True
    while v:
        answer += 1
        idx = visited2.index(False) # 방문하지 않은 그래프 체크
        visited2[idx] = True
        dfs(idx, graph, visited)
        count = 0
        
        # 그래프 여러 개인 경우 방문하지 않은 노드가 있는지 체크
        for i in visited2:
            if i == True:
                count += 1
        if count == len(visited2):
            v = False

    return answer