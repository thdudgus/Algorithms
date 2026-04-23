def solution(nums):
    p = {}
    for i in nums:
        p[i] = 0
    for i in nums: # 폰켓몬 수 세기
        p[i] += 1
        
    n = len(nums)/2 # 입양할 폰켓몬 수
    s = set()
    if len(p) >= n:
        answer = n
    else:
        answer = len(p)
    
    return answer