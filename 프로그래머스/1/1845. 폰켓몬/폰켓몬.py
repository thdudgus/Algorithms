def solution(nums):
    p = set(nums) # 폰켓몬 중복 제거      
    n = len(nums)/2 # 입양할 폰켓몬 수
    
    if len(p) >= n:
        return n
    else:
        return len(p)
