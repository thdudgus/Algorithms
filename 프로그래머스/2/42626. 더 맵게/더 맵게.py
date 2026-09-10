# from collections import deque
# def solution(scoville, K):
# # 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
#     answer = 0
    
#     while min(scoville) < K:
#         tmp = sorted(scoville)
#         q_scoville = deque(tmp)
#         f = q_scoville.popleft()
#         if len(q_scoville) == 0:
#             return -1
#         s = q_scoville.popleft()
#         q_scoville.append(f+(s*2))
#         answer += 1
#         scoville = list(q_scoville)
#     return answer

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)  
    # 리스트를 "힙 구조"로 한 번에 바꿔줌. O(n)
    # (완전히 정렬하는 게 아니라, "최솟값이 맨 앞에 오는" 조건만 만족시키는 재배치)

    answer = 0

    while scoville[0] < K:
        # scoville[0] : 힙에서 항상 "현재 가장 작은 값"이 저장되는 자리
        # → min(scoville) 대신 O(1)로 바로 확인 가능 (별도 탐색 불필요)

        if len(scoville) < 2:
            # 섞을 음식이 1개 이하로 남았는데 아직 K를 못 넘겼다면 불가능
            return -1

        f = heapq.heappop(scoville)
        # 가장 작은 값을 꺼냄. O(log n)

        s = heapq.heappop(scoville)
        # 그다음으로 작은 값을 꺼냄. O(log n)

        mixed = f + (s * 2)
        # 섞은 음식의 스코빌 지수 계산

        heapq.heappush(scoville, mixed)
        # 섞은 값을 다시 힙에 넣음. O(log n)
        # (heapq가 알아서 최솟값이 맨 앞에 오도록 재배치해줌)

        answer += 1

    return answer