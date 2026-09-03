# https://school.programmers.co.kr/learn/courses/30/lessons/42840#

def solution(answers):
    submits = [[1, 2, 3, 4, 5],  [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    a = []
    
    for s in submits:
        count = 0
        for i in range(len(answers)):
            # 나머지 연산은 반드시 "짧고 반복되는 쪽(s)"의 인덱스에 걸어야 안전하기 때문에 
            # 아래 주석 조건은 안 됨.
            if answers[i] == s[i%len(s)]: # s[i] == answers[i%len(s)]:
                count += 1
        a.append(count)
        
    max_a = max(a)
    answer = [i+1 for i, val in enumerate(a) if val == max_a]
    return answer
