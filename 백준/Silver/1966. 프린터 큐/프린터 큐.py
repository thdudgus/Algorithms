from collections import deque
n = int(input())
result = [] 
for i in range(n):
    total = 1
    number = deque(map(int, input().split())) # 0문서 개수, 1궁금한 위치
    stand = deque(map(int, input().split())) # 0문서들 중요도
    order = 1
    while True:
        if stand[0] == max(stand) and number[1]!=0:
            stand.popleft()
            number[1] -= 1
            order += 1
        elif stand[0] != max(stand):
            stand.append(stand[0])
            stand.popleft()
            if number[1]!=0:   number[1] -= 1
            elif number[1]==0: number[1] = len(stand)-1
        elif stand[0] == max(stand) and number[1]==0:
            break
    result.append(order)

print(*result)

