# # 한 명 빼고 모두 마라톤 완주
# # 참여자 participant
# # 완주자 completion
# # 완주하지 못한 선수의 이름을 return

# def solution(participant, completion):
#     p_dict = {}
#     c_dict = {}
#     for i in participant:
#         p_dict[i] = 0
#     for i in completion:
#         c_dict[i] = 0
    
#     # 참여자, 완주자 세기
#     for i in participant:
#         p_dict[i] += 1
#     for i in completion:
#         c_dict[i] += 1

#     # 참여자 중에 완주자 있으면
#     for j in completion:
#         if j in p_dict:
#             p_dict[j] -= c_dict[j]
    
#     answer = []
#     for i in p_dict:
#         if p_dict[i] > 0:
#             answer.append(i)
#     return answer[0]

# 한 명 빼고 모두 마라톤 완주
# 참여자 participant
# 완주자 completion
# 완주하지 못한 선수의 이름을 return

def solution(participant, completion):
    p_dict = {}
    for i in participant:
        p_dict[i] = 0
    
    # 참여자 세기
    for i in participant:
        p_dict[i] += 1
        
    for i in completion:
        p_dict[i] -= 1
    
    answer = []
    for i in p_dict:
        if p_dict[i] > 0:
            answer.append(i)
    return answer[0]


