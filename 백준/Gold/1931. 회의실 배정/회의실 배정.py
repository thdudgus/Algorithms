n = int(input())
meetings = []  # 시간 정보 입력받기

for i in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

# 종료 시간 기준으로 회의 정렬 (끝나는 시간이 같을 경우 시작 시간이 빠른 순으로)
meetings.sort(key=lambda x: (x[1], x[0]))

last_end_time = 0  # 마지막 회의의 종료 시간
count = 0  # 선택한 회의 개수

# 회의가 지나가면서 가능한 회의를 선택
for start, end in meetings:
    if start >= last_end_time:
        count += 1
        last_end_time = end

# 결과 출력
print(count)
