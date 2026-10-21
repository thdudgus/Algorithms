def solution(numbers, target):
    answer = 0

    def dfs(idx, total):
        nonlocal answer

        # 모든 숫자를 다 사용했다면
        if idx == len(numbers):
            if total == target:
                answer += 1
            return

        # 현재 숫자를 더하는 경우
        dfs(idx + 1, total + numbers[idx])

        # 현재 숫자를 빼는 경우
        dfs(idx + 1, total - numbers[idx])

    dfs(0, 0)

    return answer