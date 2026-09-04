from collections import deque
def solution(priorities, location):
    que = deque(enumerate(priorities))  # (0: 원래 인덱스, 1: 우선순위) 튜플로 저장

    answer = 0
    while len(que) != 0:
        max_value = max(p for k, p in que) # 가장 큰 우선순위

        if que[0][1] != max_value: 
            que.append(que.popleft())
        else: 
            answer += 1
            temp = que.popleft()
            print(temp)
            if temp[0] == location:
                return answer
            
    
    return answer