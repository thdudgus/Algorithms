def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)
    answer = ''.join(numbers)

    # 모든 숫자가 0인 경우 처리
    return str(int(answer))