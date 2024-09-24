from itertools import combinations
def solution(number):
    answer = 0
    numbers = list(number)
    students = list(combinations(numbers, 3))
    for i in students:
        if (sum(i) == 0):
            answer +=1
    return answer