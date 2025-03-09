import sys

# 한 번에 입력을 받아 리스트로 변환
input_data = sys.stdin.read().split()

# 첫 번째 줄에서 n, m 가져오기
n = int(input_data[0])
m = int(input_data[1])

# 두 번째 줄에서 숫자 리스트 가져오기
number = list(map(int, input_data[2:n+2]))

# 누적합 배열 생성 (0번 인덱스를 추가하여 초기값 0으로 설정)
addSum = [0] * (n + 1)
for i in range(1, n + 1):
    addSum[i] = addSum[i - 1] + number[i - 1]

# m개의 쿼리 처리
index = n + 2
result = []
for _ in range(m):
    i = int(input_data[index])
    j = int(input_data[index + 1])
    index += 2

    # 구간 합 계산
    result.append(str(addSum[j] - addSum[i - 1]))

# 결과 출력 (sys.stdout.write 사용)
sys.stdout.write("\n".join(result) + "\n")