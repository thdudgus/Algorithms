def solution(s):
    s = list(map(int, s.split()))  # s를 직접 사용
    answer = '{} {}'.format(min(s), max(s))  # 문자열 포맷팅 수정
    return answer
