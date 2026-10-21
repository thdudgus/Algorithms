def solution(citations): 
    # citations: 각 논문의 인용 횟수
    # 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고, 나머지 논문들이 h번 이하 인용됨.
    # h의 최댓값
    citations.sort()
    n = len(citations)
    # 0, 1, 3, 5, 6
    for i, c in enumerate(citations):
        h = n-i  # 남은 논문 개수 = 현재 논문 포함 c 이상 인용된 논문 수
        # 어차피 h는 n을 넘지 못 함... 논문이 n편이라
        
        if c >= h:
            # 현재 논문(c)이 "남은 논문 수(h)" 이상 인용됨
            # 정렬돼 있으니 오른쪽 h편은 전부 c 이상 → 전부 h 이상
            # h편이 h번 이상 인용됨
            return h
        
    return 0