def solution(citations): 
    # citations: 각 논문의 인용 횟수
    n = len(citations) # 논문 개수
    # h-인덱스가 10이라면, 10번 이상 인용된 논문이 최소 10편 있다.
    sorted_c = sorted(citations)
    print(sorted_c)
    
    # i번 이상 인용된 논문 개수 q
    q = []
    for i in sorted_c:
        q.append(n - sorted_c.index(i))
        
    for i, k in enumerate(q):
        if k <= sorted_c[i]:
            return k    
    return 0