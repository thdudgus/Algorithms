from collections import deque

def solution(bridge_length, weight, truck_weights):
    # bridge_length: 다리에 몇 칸(자리)이 있는지
    # weight: 다리가 버티는 최대 무게
    # truck_weights: 각 트럭들의 무게
    
    passed = deque()  # 다리를 지난 트럭
    passing = deque([0] * bridge_length)  # 다리 위 상태, 처음엔 전부 빈 칸(0)으로 채움
    waiting = deque(truck_weights)  # 대기 트럭
    
    answer = 0
    
    while waiting:
        answer += 1
        
        # 매 tick마다 무조건 맨 앞 트럭(혹은 빈 칸)은 다리를 다 건너서 빠져나감
        passed.append(passing.popleft())
        
        tmp = waiting[0]  # 다음에 태우려는 트럭
        if sum(passing) + tmp <= weight:  # 무게 괜찮으면
            passing.append(waiting.popleft())  # 다리에 올림
        else:  # 무게 안 되면
            passing.append(0)  # 빈 칸으로 채움
    
    # waiting은 다 비었지만, 다리 위(passing)에 남은 트럭들이 마저 건너야 함
    answer += bridge_length
    
    return answer