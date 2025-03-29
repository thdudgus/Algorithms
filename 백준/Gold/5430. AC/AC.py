import sys
import json
from collections import deque

input_data = sys.stdin.read().split()
n = int(input_data[0])  # 테스트 케이스 개수
op = []  # 계산 개수
numberOfInt = []
integer = []
result = []

for i in range(n):
    op.append(list(input_data[1 + (i * 3)]))  # 문자열을 리스트로 변환
    numberOfInt.append(int(input_data[2 + (i * 3)]))  # 정수 변환
    integer.append(deque(json.loads(input_data[3 + (i * 3)])))  # 문자열을 리스트로 변환 후 deque로 저장
    isReverse = False
    isError = False
    for j in op[i]:
        if j == "R":
            isReverse = not isReverse
        else: # "D"
            if len(integer[i]) == 0:
                result.append("error")
                isError = True
                break
            if isReverse:
                integer[i].pop()
            else:
                integer[i].popleft()
    if isError == True:
        continue
    if isReverse:
        integer[i].reverse() 
        
    # deque를 리스트로 변환한 후, 각 요소를 문자열로 변환하여 출력
    strlist = [str(i) for i in integer[i]]  # deque의 요소를 문자열로 변환
    result.append("[" + ",".join(strlist) + "]")  # 문자열을 합쳐서 출력 포맷에 맞춤

# 결과 출력
for res in result:
    print(res)