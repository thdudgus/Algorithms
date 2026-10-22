from collections import deque
def solution(cards1, cards2, goal):
    q1 = deque(cards1)
    q2 = deque(cards2)
    
    for g in goal:
        if q1 and q1[0] == g:
            q1.popleft()
            continue
        if q2 and q2[0] == g:
            q2.popleft()
            continue
        return "No"
        
    return"Yes"