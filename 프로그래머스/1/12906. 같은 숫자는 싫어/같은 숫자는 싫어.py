# from collections import deque

# def solution(arr):
#     qs = deque()
#     q = deque()
#     answer = []
#     for a in arr:
#         qs.append(a)
#         q.append(a)
#     for i in range(len(arr)):
#         temp = qs.popleft()
#         if i == 0:
#             answer.append(temp)
#         elif i > 0 and (q[i-1] != temp):
#             answer.append(temp)
#     return answer


# from collections import deque

# def solution(arr):
#     answer = []
#     q = deque()
    
#     for a in arr:
#         q.append(a)
        
#     for i in range(len(arr)):
#         temp = q.popleft()
#         if len(answer) == 0:
#             answer.append(temp)
#             continue
#         if i-1 > 0 and (answer[i-1] == temp):
#             answer.append(temp)
#     return answer


def solution(arr):
    answer = []
    for i, a in enumerate(arr):
        if len(answer) == 0:
            answer.append(a)
        elif answer[-1] != a:
            answer.append(a)
    return answer