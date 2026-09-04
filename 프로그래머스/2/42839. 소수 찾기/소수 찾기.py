from itertools import permutations

def solution(numbers):
    number = list(map(str, numbers))
    r = []
    for length in range(1, len(number) + 1):
        for perm in permutations(number, length):
            r.append(int("".join(perm)))
    rr = list(set(r))
    
    answer = 0
    for test in rr:
        count = 0 # 안 나눠진 횟수
        for i in range(2, test):
            if test % i == 0:
                break
            else: 
                count += 1
        if count == test-2: # 1이랑 본인 제외
            answer += 1
                
    return answer
