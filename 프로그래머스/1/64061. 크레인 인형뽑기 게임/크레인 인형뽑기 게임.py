from collections import deque
def solution(board, moves):
    dolls = [deque() for _ in range(len(board))]
    answer = 0
    basket = [0]
    
    # 세로로 재배열하기 + 가장 위에 있는 인형이 가장 아래로. popleft로 뺄 거임.
    for line in board:
        for i, doll in enumerate(line):
            if doll != 0:
                dolls[i].append(doll)
    
    for move in moves:
        if not dolls[move-1]:
            continue
        d = dolls[move-1].popleft()
        
        if basket[-1] == d:
            basket.pop()
            answer += 2
            continue
        basket.append(d)
        
    return answer