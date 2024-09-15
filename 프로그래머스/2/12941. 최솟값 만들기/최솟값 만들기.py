def solution(A,B):
    A.sort() # 오름차순 정렬
    B.sort(reverse=True) # 내림차순 정렬
    answer = 0
    for i in range(0,len(A)):
        answer = answer + (A[i]*B[i])
    return answer