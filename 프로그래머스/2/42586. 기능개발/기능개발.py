# 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있음.
# 그렇지만 배포는 앞에 있는 기능이 배포될 때 함께 배포됨.

# progresses: 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열
# speeds: 각 작업의 개발 속도가 적힌 정수 배열
# 각 배포마다 몇 개의 기능이 배포되는지를 return해라. (배포는 하루에 한 번. 하루 끝.)
def solution(progresses, speeds):
    answer = []
    i = 0
    while progresses:
        count = 0
        
        # progresses 더해주기
        progresses = [x + y for x, y in zip(progresses, speeds)]
        
        if progresses[0] < 100:
            continue
            
        else: # 배포 될 때 progresses[0] >= 100:
            temp = []
            for progress in progresses:
                if progress >= 100:
                    count += 1
                    temp.append(progress)
                else: break
                
            progresses = progresses[count:]
            speeds = speeds[count:] 
        if count != 0:
            answer.append(count)
    return answer