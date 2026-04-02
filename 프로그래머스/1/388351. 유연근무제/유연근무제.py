# 일주일동안 출근 희망 시각에 늦지 않고 출근한 직원에게 상품을 준다
# 출근 희망 시각 + 10분까지 어플로 출근해야 한다.  (토, 일 제외)
# 모든 시각은 시에 100을 곱하고 분은 더한 정수로 표현된다. 
# 예를 들어 10시 13분은 1013이 되고 9시 58분은 958이 됩니다.

# 직원 n명이 설정한 출근 희망 시각을 담은 1차원 정수 배열 schedules
# 직원들이 일주일 동안 출근한 시각을 담은 2차원 정수 배열 timelogs (행: 직원, 열: 출근 시각)
# 이벤트를 시작한 요일을 의미하는 정수 startday
# 월요일(1)이면 5, 6 버리고 
# 화요일(2)이면 4, 5 버리고
# 수요일(3)이면 3, 4 버리고
# 목요일(4)이면 2, 3 버리고
# 금요일(5)이면 1, 2 버리고
# 토요일(6)이면 0, 1 버리고
# 일요일(7)이면 6, 0 버리고
def solution(schedules, timelogs, startday):
    count = 0 # 상품 받는 직원 수
    weekendDay = weekend(startday) # 주말 인덱스
    
    for k, schedule in enumerate(schedules): # 직원마다
        success = 0 # 출근 성공횟수
        if (schedule + 10) % 100 >= 60:
            schedule += 110
            schedule -= 60
        else: schedule += 10
        for i, timelog in enumerate(timelogs[k]): # 출근시간마다
            print(schedule)
            if i not in weekendDay and schedule >= timelog:
                success += 1
        if success >= 5:
            count += 1
                
    return count  # 상품을 받은 직원의 수를 return

def weekend(s):
    if s == 1:
        return [5, 6]
    elif s == 2:
        return [4, 5]
    elif s == 3:
        return [3, 4]
    elif s == 4:
        return [2, 3]
    elif s == 5:
        return [1, 2]
    elif s == 6:
        return [0, 1]
    elif s == 7:
        return [6, 0]


