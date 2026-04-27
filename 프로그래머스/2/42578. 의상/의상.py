def solution(clothes):
    cloth = {}
    for c in clothes:
        cloth[c[1]] = 1
    for c in clothes:
        cloth[c[1]] += 1

    answer = 1
    for i in cloth.keys():
        answer *= cloth[i]
    return answer-1