from itertools import combinations
def solution(numbers, target):
    numbers = list(map(int, numbers))
    answer = 0
    
    for i in range(1, len(numbers)): # 뺄셈의 개수
        minus = list(combinations(numbers, i))
        for j in range(len(minus)):
            total = sum(numbers) - 2*sum(minus[j])
            if total == target:
                answer+=1

    return answer