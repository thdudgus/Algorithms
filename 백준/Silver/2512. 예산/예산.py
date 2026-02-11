import sys
n = int(sys.stdin.readline()) # 지방의 수
wants = list(map(int, sys.stdin.readline().split())) # 지방요청들
m = int(sys.stdin.readline()) # 실상한액

        # 시작가능금액, 끝가능금액, 실상한액, 지방요청들
def find_budget(start, end, limit, wantss):
    while start <= end: 
        # 특정 상한액
        mid = (start + end) // 2
        # 특정 상한액으로 자르기
        cutted = [mid if x >= mid else x for x in wantss] 
        
        if sum(cutted) <= limit: # 예산 상한액 보다 합이 작으면 더 최적(최대 합)을 찾아보자
            start = mid + 1
        else: end = mid - 1 # 예산 상한액 보다 합이 크면 특정 상한액을 더 줄이자.
        
    # 이렇게 구해진 start-1이 최대 예산. (한 번 더 확인해보려고 start에 1을 더한 것이었기 때문에 start-1이 최대 예산이 된다.)
    return start-1
           
if sum(wants) <= m:
    print(max(wants))
else:
    wants.sort()
    print(find_budget(1, wants[-1], m, wants)) # 시작가능금액, 끝가능금액, 실상한액, 지방요청들