# 탐험에 시작에 필요한, 최소 필요 피로도 (탐험 전 갖고 있어야 함)
# 탐험 마친 후 소모되는, 소모 피로도 (탐험 후)

# 현재 피로도 k
# dungeons = [[탐험 전 피로도, 탐험 후 피로도], ...]

# 이렇게 하면 idx가 최적의 경로라는 걸 보장할 수 없음..
# def solution(k, dungeons):
#     temp = k
#     answer = []
    
#     count = 0
#     for d in dungeons:
#         if d[0] <= k:
#             count += 1
#             k -= d[1]
#     answer.append(count)
    
#     k = temp
#     count = 0
#     dungeons.sort(key = lambda x:(x[1], -x[0]))
#     idx = max(range(len(dungeons)), key=lambda i: dungeons[i][0])
    
#     for i in range(len(dungeons)):
#         j = (i+idx)%len(dungeons)
#         if dungeons[j][0] <= k:
#             count += 1
#             k -= dungeons[j][1]
#         else: i -= 1
#     answer.append(count)
#     return max(answer)

def solution(k, dungeons):
    answer = 0

    def dfs(k, count, visited):
        nonlocal answer
        answer = max(answer, count)
        
        for i in range(len(dungeons)):
            if dungeons[i][0] <= k and visited[i] == False:
                visited[i] = True
                dfs(k - dungeons[i][1], count + 1, visited)
                visited[i] = False # 다시 선택하지 않은 상태로 되돌린 다음 → 다른 던전을 선택
                # 되돌려야 하기 때문에, k랑 count도 함께 되돌려야 함.
    
    visited = [False] * len(dungeons)
    dfs(k, 0, visited)
    print(answer)
        
    return answer